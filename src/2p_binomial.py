import sys
import os
from collections import defaultdict
from statsmodels.stats.proportion import test_proportions_2indep

countmatrix = []
for line in open(sys.argv[1]):
    line = line.strip().split("\t")
    for i in range(len(line)): line[i] = int(line[i])
    countmatrix.append(line)

print(test_proportions_2indep(countmatrix[0][1], countmatrix[0][0], countmatrix[1][1], countmatrix[1][0]))

