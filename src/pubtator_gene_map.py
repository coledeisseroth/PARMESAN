import sys
import os
from collections import defaultdict
import argparse



def onetoone(pubtatorgenefile):
  for line in open(pubtatorgenefile):
    lineData = line.strip().split("\t")
    pmid = lineData[0]
    genes = lineData[1].split("|")
    for gene in genes: print(pmid + "\t" + gene)

def oneperline(pubtatorgenefile):
  cur_pmid = None
  cur_findings = set()
  for line in (os.popen("cat " + pubtatorgenefile + " | sort -k1,1g")):
    lineData = line.strip().split("\t")
    pmid = lineData[0]
    if cur_pmid != pmid:
      if cur_pmid: print(cur_pmid + "\t" + "|".join(list(cur_findings)))
      cur_pmid = pmid
      cur_findings = set()
    findings = lineData[1].split("|")
    cur_findings |= set(findings)
  if cur_pmid: print(cur_pmid + "\t" + "|".join(list(cur_findings)))

def main(mapfile, opl=False):
  if opl: oneperline(mapfile)
  else: onetoone(mapfile)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Reformat the pubtator article/finding map file")
  parser.add_argument("mapfile", type=str, help="Pubtator map file")
  parser.add_argument("-l", action="store_true", help="One article and all of its findings per line")
  args = parser.parse_args()
  main(args.mapfile, args.l)

