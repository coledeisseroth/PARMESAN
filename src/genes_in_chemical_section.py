import sys
import os
from collections import defaultdict

def load_gene_aliases(aliasfile):
  aliases = set()
  for line in open(aliasfile):
    gene = line.strip().split("|")[0]
    aliases.add(gene.upper())
  return aliases

def parse_chemicals(chemicalfile, aliases):
  for line in open(chemicalfile):
    line = line.strip()
    lineData = line.split("\t")
    chemical = lineData[1]
    if chemical.upper() not in aliases: continue
    print line

def main(aliasfile, chemicalfile):
  aliases = load_gene_aliases(aliasfile)
  parse_chemicals(chemicalfile, aliases)

if __name__ == "__main__":
  main(sys.argv[1], sys.argv[2])

