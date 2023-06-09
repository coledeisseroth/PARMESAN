import sys
import os
from collections import defaultdict

def main(inputfile):
  gene_to_score = defaultdict(float)
  for line in os.popen("cat " + inputfile + " | cut -f3,4,8 | sort -u | cut -f1,3,4"):
    lineData = line.strip().split("\t")
    gene = lineData[0]
    score = float(lineData[1])
    gene_to_score[gene] += score
  for gene in gene_to_score.keys(): print gene + "\t" + str(gene_to_score[gene])

if __name__ == "__main__":
  main(sys.argv[1])

