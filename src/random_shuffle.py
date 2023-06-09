import sys
import os
from collections import defaultdict
import random

random.seed(2022)

lines = []
for line in open(sys.argv[1]):
    lines.append(line.strip())
    random.shuffle(lines)

for line in lines: print(line)
