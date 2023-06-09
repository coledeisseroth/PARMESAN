import argparse
import sys
import os
from collections import defaultdict

negators = ["failed", "fails", "fail", "failing", "not", "cannot", "no"]

def load_predicates(predicates):
  returnList = set()
  for line in open(predicates): returnList.add(line.strip().lower())
  return returnList

def last_predicate(intermediate, predicates):
  iwords = intermediate.lower().split(" ")
  possible_predicates = list(set(iwords) & predicates)
  iwords.reverse()
  for word in iwords:
    if word in possible_predicates: return word
  return None

def main(sentencefile, predicatefile, druggene):
  predicates = load_predicates(predicatefile)
  for line in open(sentencefile):
    lineData = line.strip("\n").split("\t")
    pmid = lineData[0]
    gene1 = lineData[1]
    gene2 = lineData[2]
    intermediate = lineData[3]
    iwords = intermediate.split(" ")
    predicate = last_predicate(intermediate, predicates)
    if not predicate: continue
    beginning = lineData[4]
    end = lineData[5]
    predicateindex = intermediate.lower().split(" ").index(predicate)
    passivevoice = (predicateindex < len(iwords) - 1) and iwords[predicateindex + 1].lower() in ["by", "in"]
    if druggene and ((lineData[-1] == 'True') == passivevoice): continue
    if passivevoice:
      subjectgene = gene2
      objectgene = gene1
      postsubject = end
      presubject = " ".join(iwords[predicateindex+2:])
      preobject = beginning
      postobject = " ".join(iwords[:predicateindex])
      if len(postobject.split(" ")) > 5: continue
      if len(presubject.split(" ")) > 5: continue
      if set(negators) & set(postobject.split(" ")): continue
    else:
      subjectgene = gene1
      objectgene = gene2
      presubject = beginning
      postsubject = " ".join(iwords[:predicateindex])
      preobject = " ".join(iwords[predicateindex+1:])
      postobject = end
      if len(preobject.split(" ")) > 5: continue
      if len(postsubject.split(" ")) > 5: continue
      if postsubject[-2:] == ", ": continue
      if set(negators) & set(postsubject.split(" ")): continue
    subj = " ".join([x for x in [presubject, subjectgene, postsubject] if x != ""])
    obj = " ".join([x for x in [preobject, objectgene, postobject] if x != ""])
    print("\t".join([pmid, subjectgene, objectgene, predicate, subj, obj, presubject, postsubject, preobject, postobject]))

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Discern the subject and object in a cooccurrences file')
  parser.add_argument('sentencefile', type=str, help='The file containing the sentences')
  parser.add_argument('predicatefile', type=str, help='The file containing the predicates to use')
  parser.add_argument('-d', action='store_true', help='Identify drug-gene relationships instead of gene-gene relationships')
  args = parser.parse_args()
  main(args.sentencefile, args.predicatefile, args.d)


