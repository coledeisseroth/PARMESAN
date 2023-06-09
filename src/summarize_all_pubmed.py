import sys
import os
from collections import defaultdict
import evaluate_sentence_bak as es
import split_sentences as ss
import find_models_bak as fm
import gene_aliases as ga
import re
import multiprocessing as mp
import argparse
import vocabulary as vocab

myPath = os.path.realpath(__file__)
myDir = "/".join(myPath.split("/")[:-1])

PMID_TO_GENE = "/home/deissero/hdd/gene_modifiers/pubtator/genes/ndhub_pmid_to_genes.txt"
PMID_TO_CHEMICAL = "/home/deissero/hdd/gene_modifiers/pubtator/chemicals/pmid_to_ndhub_chemicals.txt"


pmid_to_gene = None
pmid_to_chemical = None
targetDir = None
gm = False
gt = False
cm = False
sii = False

def main(abstracts):
  summaries = []
  for line in open(abstracts):
    global pmid_to_gene
    global pmid_to_chemical
    lineData = line.strip().split("\t")
    if len(lineData) < 3: continue
    pmid = lineData[0]
    title = lineData[1]
    abstract = lineData[2]
    search_chemicals = None
    search_genes = None
    if sii:
      search_genes = set(lineData[3].lower().split("|"))
      search_chemicals = set(lineData[4].lower().split("|"))
    sentences = [title] + ss.split_sentences(abstract)
    models = fm.get_models(sentences)
    if targetDir is None: outfile = None
    else: outfile = open(os.path.join(targetDir, abstracts.split("/")[-1]), "w")
    for sentence in sentences:
      sentence = es.clean_sentence(sentence)
      model = es.find_model(sentence)
      if models and not model: model = "(" + models[0] + ")"
      for verb in vocab.find_words(["predicate"]):
        subject_object_pairs = es.subject_object(sentence, verb)
        for subj, obj in subject_object_pairs:
          if not subj: continue
          modifier_lookup = set()
          if sii:
            if cm: modifier_lookup |= search_chemicals
            if gm: modifier_lookup |= search_genes
          else:
            if cm: modifier_lookup |= pmid_to_chemical[pmid]
            if gm: modifier_lookup |= pmid_to_gene[pmid]
          if not cm and not gm and not sii: modifier_lookup = None
          elif not modifier_lookup: continue
          poss_mods = es.find_possible_modifiers(subj, modifier_lookup)
          modifier = es.pick_best_modifier(poss_mods)
          if not modifier: continue
          modifier_dist = subj.index(modifier) + 1
          if subj[0] not in vocab.find_words(["passive"]): modifier_dist = len(subj) + 1 - modifier_dist
          problem = es.find_problem(obj)
          if sii and gt: obj = [word for word in obj if word.lower() in search_genes]
          elif gt: obj = [word for word in obj if word.lower() in pmid_to_gene[pmid]]
          else: obj = [word for word in obj if word != word.lower() and len(word) > 1]
          if not obj: continue
          modifier_treatment, treatment_dist = es.find_modifier_treatment(subj, modifier)
          summary_line = "\t".join([pmid, modifier, verb, problem, " ".join(obj), modifier_treatment, model, str(len(subj)), str(len(poss_mods)), str(treatment_dist), str(len(obj)), str(modifier_dist)])
          if outfile is None: print summary_line
          else: outfile.write(summary_line + "\n")
    if not(outfile is None): outfile.close()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Crunch the entirety of Pubmed into a few quick summaries. File must be tab-separated, featuring PMID, title, abstract, and (optionally) the terms to search for.')
  parser.add_argument('-f', type=str, default='', help='Single file to parse')
  parser.add_argument('-d', type=str, default='', help='Directory of files to parse')
  parser.add_argument('-t', type=str, default=None, help='Target directory')
  parser.add_argument('--prefix', type=str, default='pubmed', help='All files in the directory parsed must have a name starting with this.')
  parser.add_argument('-p', type=int, default=1, help='Number of threads to split the job across')
  parser.add_argument('-cm', action='store_true', help='Look up chemicals (as modifiers)')
  parser.add_argument('-gm', action='store_true', help='Look up genes (as modifiers)')
  parser.add_argument('-gt', action='store_true', help='Look up genes (as target genes)')
  parser.add_argument('-v', action='store_true', help='Verbose: Print status updates')
  parser.add_argument('-sii', action='store_true', help='Search items included in column 4')
  args = parser.parse_args()
  targetDir = args.t
  cm = args.cm
  gm = args.gm
  gt = args.gt
  sii = args.sii
  if (not args.sii) and args.cm:
    if args.v: print "Loading chemicals..."
    pmid_to_chemical = es.load_pmid_map(PMID_TO_CHEMICAL)
  if (not args.sii) and (args.gm or args.gt):
    if args.v: print "Loading genes..."
    pmid_to_gene = es.load_pmid_map(PMID_TO_GENE)
  if not args.f and not args.d: quit()
  if args.v: print "Compiling summaries..."
  if args.f:
    targetDir = None
    main(args.f)
  if args.d:
    if targetDir is None: raise Exception("Must specify target directory (use '-t' flag).")
    pool = mp.Pool(args.p)
    abstractfiles = []
    for abstractfile in os.listdir(args.d):
      abstractfiles.append(os.path.join(args.d, abstractfile))
    pool.map(main, abstractfiles)


