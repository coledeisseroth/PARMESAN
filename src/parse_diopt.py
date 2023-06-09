import sys
import os
from collections import defaultdict
import re

INFO_PREFIX = '</td> <td>  <a href="https://www.flyrnai.org/tools/diopt/web/feedback/'

def main(dioptFile):
  for line in open(dioptFile):
    line = line.strip()
    if len(line) < len(INFO_PREFIX): continue
    if line[:len(INFO_PREFIX)] != INFO_PREFIX: continue
    line = re.sub("</td>", "", line)
    line = re.sub(" ", "", line)
    print line
    line = line.split("<td>")
    line = [item for item in line if "<ahref=" not in item and item not in [""]]
    bestScoreIndex = len(line) - 1
    while True:
      if ">Yes" in line[bestScoreIndex] or ">No" in line[bestScoreIndex]: break
      bestScoreIndex -= 1
    hentrez = line[bestScoreIndex - 5]
    hgene = line[bestScoreIndex - 4]
    model = line[bestScoreIndex - 3]
    mgene = line[bestScoreIndex - 2]
    score = line[bestScoreIndex - 1]
    bestScore = line[bestScoreIndex].split(">")[-2].split("<")[0]
    bestScoreReverse = line[bestScoreIndex].split(">")[-1]
    print "\t".join([hgene, model, mgene, score, bestScore, bestScoreReverse, hentrez])

if __name__ == "__main__":
  main(sys.argv[1])

