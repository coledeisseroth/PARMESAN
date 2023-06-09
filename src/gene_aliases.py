import sys
import os
from collections import defaultdict
import pprint
import json
import requests
import pandas as pd
import argparse

myPath = os.path.realpath(__file__)
myDir = "/".join(myPath.split("/")[:-1])
ALIASES = myDir + "/../hgnc/aliases.txt"
MODEL_ORGANISMS = ["worm", "buddingYeast", "drosophila", "fissionYeast", "mouse", "rat"]

def find_aliases(genes):
  genePattern = "\\|".join(genes)
  aliases = []
  for gene in genes: aliases.append(set([gene.upper()]))
  for line in os.popen("cat " + ALIASES + " | grep -wi '" + genePattern + "'"):
    symbols = set(sym for sym in line.upper().strip().split("|") if sym)
    for i, gene in enumerate(genes):
      if gene.upper() in symbols: aliases[i] |= symbols
  return aliases

def load_aliases():
  aliases = set()
  for line in open(ALIASES):
    aliases |= set(line.upper().strip().split(", "))
  return aliases

def get_homologs(gene_id):
  for s in MODEL_ORGANISMS:
    url = "http://marrvel.org/data/homolog/{}".format(s)
    req = requests.get(url, params = {"geneSymbol": gene_id})
    dat = json.loads(req.text)
    for row in dat:
      row["species"] = s
      print(row['species'], row['geneSymbol'])

def homolog_table():
  returnTbl = [["#gene"] + MODEL_ORGANISMS]
  aliases = load_aliases()
  for alias in aliases:
    species_to_homolog = defaultdict(str)
    species_dicts = get_homologs(alias)
    if not species_dicts: continue
    for species_dict in species_dicts:
      species = species_dict['species']
      homolog = species_dict['geneSymbol']
      species_to_homolog[species] = homolog
    print(species_to_homolog)
    entry = [alias]
    for species in MODEL_ORGANISMS: entry.append(speices_to_homolog[species])
    #print entry
    returnTbl.append(entry)
  return returnTbl

def main(gene):
  if gene:
    aliases = find_aliases([gene])[0]
    #print "Aliases: " + ", ".join(aliases)
    get_homologs(gene)
  else:
    homolog_table()
    #for entry in homolog_table(): print "\t".join(entry)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Process some integers.')
  parser.add_argument('-g', type=str, default='', help='Lookup a gene')
  args = parser.parse_args()
  main(args.g)

