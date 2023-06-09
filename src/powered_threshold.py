import sys
import os
from collections import defaultdict
from statsmodels.stats.proportion import power_proportions_2indep
from statsmodels.stats.proportion import test_proportions_2indep
from statsmodels.stats.proportion import samplesize_proportions_2indep_onetail

for line in open(sys.argv[1]):
    line = line.strip().split("\t")
    proportion = float(line[1])
    if line[0] == "0":
        baseline = proportion
        continue
    print(line[0] + "\t" + str(samplesize_proportions_2indep_onetail(proportion - baseline, baseline, 0.8)))

