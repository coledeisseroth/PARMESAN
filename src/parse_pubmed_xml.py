import sys
import os
from collections import defaultdict

def main(xmlfile):
  pmid = ""
  title = ""
  abstract = ""
  for line in os.popen("zcat " + xmlfile):
    line = line.strip().strip(" ")
    if line == "</PubmedArticle>":
      if pmid and title and abstract: print("\t".join([pmid, title, abstract]))
      pmid = ""
      title = ""
      abstract = ""
      continue
    if "</PMID>" in line:
      if not pmid: pmid = line.split(">")[1].split("<")[0]
      continue
    if "</ArticleTitle>" in line:
      if not title: title = "<".join(">".join(line.split(">")[1:]).split("<")[:-1])
      continue
    if "</AbstractText>" in line:
      abstract += "<".join(">".join(line.split(">")[1:]).split("<")[:-1])
      continue
  print("\t".join([pmid, title, abstract]))


if __name__ == "__main__":
  main(sys.argv[1])

