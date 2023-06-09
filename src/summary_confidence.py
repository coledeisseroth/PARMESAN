import sys
import os
from collections import defaultdict
import evaluate_sentence as es
import gene_aliases as ga
import argparse


GENE_WEIGHT = 0.2
MODIFIER_WEIGHT = 0.2
PROBLEM_WEIGHT = 0.2
TREATMENT_WEIGHT = 0.2
MODEL_WEIGHT = 0.2


def gene_confidence(summary):
  conf = 1.0
  objLen = summary[10]
  conf /= objLen
  return conf

def modifier_confidence(summary):
  modifier = summary[1]
  conf = 1.0
  if es.is_number(modifier): return 0.0
  if len(modifier) < 2: return 0.0
  if len(modifier) < 3: conf *= 0.1
  conf *= (1.0 - (1.0 / len(modifier)))
  if modifier == modifier.lower(): conf *= 0.5
  if modifier[0] != modifier[0].upper(): conf *= 0.5
  if modifier != modifier.upper(): conf *= 0.75
  return conf

def problem_confidence(summary):
  conf = 1.0
  problem = summary[3]
  if not problem: return 0.0
  return conf

def treatment_confidence(summary):
  conf = 1.0
  treatment = summary[5]
  if not treatment: return 0.0
  treatDist = summary[9]
  treatDist += 1
  if treatDist < 1: return 0.0
  conf /= treatDist
  conf /= 2.0
  conf += 0.5
  return conf

def model_confidence(summary):
  conf = 1.0
  model = summary[6]
  if not model: return 0.0
  if "(" in model: conf *= 0.5
  return conf

def summary_confidence(summary, modifier_to_confidence=None):
  conf = 0.0
  conf += GENE_WEIGHT * gene_confidence(summary)
  if modifier_to_confidence is None: conf += MODIFIER_WEIGHT * modifier_confidence(summary)
  else: conf += MODIFIER_WEIGHT * modifier_to_confidence[summary[1].lower()]
  conf += PROBLEM_WEIGHT * problem_confidence(summary)
  conf += TREATMENT_WEIGHT * treatment_confidence(summary)
  conf += MODEL_WEIGHT * model_confidence(summary)
  return conf

model_indicators = ['d', 'm']
def remove_model_indicators(targets):
  words = targets.strip().split(" ")
  returnList = []
  for word in words:
    returnList.append(word)
    if len(word) < 2: continue
    if word[0] not in model_indicators: continue
    if word[1] != word[1].upper(): continue
    returnList.append(word[1:])
  return " ".join(returnList)

def load_summaries(summaries, gene, synonyms=''):
  syns = [gene.upper()]
  if synonyms:
    for syn in synonyms.split(','): syns.append(syn.upper())
  aliases = set(syns) | ga.find_aliases(syns)[0]
  returnList = []
  shell_open_cmd = "cat " + summaries + " | grep -wi '" + '\|'.join(aliases) + "'"
  for line in os.popen(shell_open_cmd):
    lineData = line.strip().split("\t")
    pmid = lineData[0]
    modifier = lineData[1]
    predicate = lineData[2]
    problem = lineData[3]
    lineData[4] = remove_model_indicators(lineData[4])
    targetsUpper = lineData[4].upper().strip().split(" ")
    treatment = lineData[5]
    model = lineData[6]
    subjLen = int(lineData[7])
    nModifiers = int(lineData[8])
    treatDist = int(lineData[9])
    objLen = int(lineData[10])
    foundaliases = list(aliases & set(targetsUpper))
    if not foundaliases: continue
    #if geneUpper not in targetsUpper: continue
    #if modifier.upper() == geneUpper: continue
    if modifier.upper() in aliases: continue
    summary = (pmid, modifier, predicate, problem, foundaliases[0], treatment, model, subjLen, nModifiers, treatDist, objLen)
    returnList.append(summary)
  return returnList

def find_common_modifiers(summaries):
  modifier_to_paper_to_confidence = defaultdict(lambda: defaultdict(float))
  for summary in summaries:
    pmid = summary[0]
    modifier = summary[1].lower()
    confidence = modifier_confidence(summary)
    if confidence > modifier_to_paper_to_confidence[modifier][pmid]: modifier_to_paper_to_confidence[modifier][pmid] = confidence
  modifier_to_confidence = {}
  for modifier in modifier_to_paper_to_confidence.keys():
    inverse_confidence = 1.0
    for pmid in modifier_to_paper_to_confidence[modifier].keys(): inverse_confidence *= (1.0 - modifier_to_paper_to_confidence[modifier][pmid])
    confidence = 1.0 - inverse_confidence
    modifier_to_confidence[modifier] = confidence
  return modifier_to_confidence

def print_summaries(summaries, modifier_to_confidence=None):
  summaries.sort(key=(lambda x: summary_confidence(x, modifier_to_confidence)), reverse=True)
  for summary in summaries:
    pmid = summary[0]
    modifier = summary[1]
    predicate = summary[2]
    problem = summary[3]
    gene = summary[4]
    treatment = summary[5]
    model = summary[6]

    if modifier_to_confidence is None: modif_conf = modifier_confidence(modifier)
    else: modif_conf = modifier_to_confidence[modifier.lower()]

    if model: model = "in " + model
    sentence = " ".join([pmid + ":", treatment, modifier, predicate, gene, problem, model])
    #print sentence
    print "\t".join([sentence, str(treatment_confidence(summary)), str(modif_conf), str(gene_confidence(summary)), str(problem_confidence(summary)), str(model_confidence(summary)), str(summary_confidence(summary, modifier_to_confidence))])

def main(summaryFile, gene, synonyms=''):
  summaries = load_summaries(summaryFile, gene, synonyms)
  #print_summaries(summaries)
  modifier_to_confidence = find_common_modifiers(summaries)
  print_summaries(summaries, modifier_to_confidence)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Check a summary list for modifiers of a given gene')
  parser.add_argument('summaryFile', type=str, help='Path to the file containing abstract summaries')
  parser.add_argument('gene', type=str, help='Target gene for which to find modifiers')
  parser.add_argument('-s', type=str, help='Any synonyms to look for as well (comma separated, e.g. SYN1,SYN2,SYN3)')
  args = parser.parse_args()
  main(args.summaryFile, args.gene, args.s)

