import sys
import os
from collections import defaultdict
import re

URL_PREFIX = 'http://www.gene2function.org/search/get_ortholog/9606/'


def main(entrez):
  url = URL_PREFIX + entrez + "/best_match"
  humanSymbol = None
  for line in os.popen("curl " + url + " | awk '$1 != \"\"' | paste -sd$'\\t' | sed 's/term=/\\n/g' | awk 'NR > 1'"):
    line = line.strip()
    symbol = line.split(">")[4].split("<")[0].strip()
    model = line.split("<small>(")[0].split(">")[-2].split("<")[0].strip()
    speciesid = re.sub(" ", "", line.split("a href")[1].split(">")[1].split("<")[0])
    if model == "Human":
      humanSymbol = symbol
      continue
    speciesid = re.sub(" ", "", line.split("a href")[1].split(">")[1].split("<")[0])
    dioptScore = line.split("<td style=\"background-color:")[0].split("$")[-2].split(" ")[-1].split("<")[0]
    best = line.split("<td style=\"background-color:")[1].split(" ")[1].split("<")[0]
    bestr = line.split("<td style=\"background-color:")[2].split(" ")[1].split("<")[0]
    confidence = " ".join(line.split("<td style=\"background-color:")[2:]).split("$")[1].split(">")[1].split("<")[0]
    print "\t".join([humanSymbol, symbol, model, speciesid, dioptScore, best, bestr, confidence])

if __name__ == "__main__":
  main(sys.argv[1])


