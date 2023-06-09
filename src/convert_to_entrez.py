import sys
import os
from collections import defaultdict


def load_entrez(entrezfile):
  symbol_to_entrez = defaultdict(set)
  for line in open(entrezfile):
    lineData = line.upper().strip().split("\t")
    entrez = lineData[0]
    symbols = lineData[1].split(" ")
    for symbol in symbols: symbol_to_entrez[symbol].add(entrez)
  return symbol_to_entrez

def load_aliases(aliasfile):
  symbol_to_aliases = defaultdict(set)
  for line in open(aliasfile):
    lineData = line.upper().strip().split("|")
    symbols = set(lineData)
    for symbol in symbols: symbol_to_aliases[symbol] |= symbols
  return symbol_to_aliases

def get_entrez(symbol, symbol_to_entrez, symbol_to_aliases):
  symbol = symbol.upper()
  primary_entrez = symbol_to_entrez[symbol]
  secondary_entrez = set()
  for alias in symbol_to_aliases[symbol]: secondary_entrez |= symbol_to_entrez[alias]
  secondary_entrez -= primary_entrez
  return ", ".join(list(primary_entrez)) + " (" + ", ".join(secondary_entrez) + ")"

def parse_summaries(summaryfile, symbol_to_entrez, symbol_to_aliases):
  #print "Summary_sentence\tPMID\tAction\tModifier\tPredicate\tTarget\tProblem\tModel\tModifier_Entrez\tTarget_Entrez"
  target = summaryfile.split("/")[-1].split(".")[0]
  target_entrez = get_entrez(target, symbol_to_entrez, symbol_to_aliases)
  for line in open(summaryfile):
    line = line.strip().split("\t")[0]
    lineData = line.split(" ")
    pmid = lineData[0].strip(":")
    action = lineData[1]
    mod = lineData[2]
    mod_entrez = get_entrez(mod, symbol_to_entrez, symbol_to_aliases)
    pred = lineData[3]
    literal_target = lineData[4]
    problem = lineData[5]
    if len(lineData) < 8: model = lineData[6]
    else: model = lineData[7]
    print "\t".join([line, pmid, action, mod, pred, literal_target, problem, model, target_entrez, mod_entrez])

def main(entrezfile, aliasfile, summaryfile):
  symbol_to_entrez = load_entrez(entrezfile)
  symbol_to_aliases = load_aliases(aliasfile)
  parse_summaries(summaryfile, symbol_to_entrez, symbol_to_aliases)

if __name__ == "__main__":
  main(sys.argv[1], sys.argv[2], sys.argv[3])
