import sys
import os
from collections import defaultdict

wordfile = sys.argv[1]
textfile = sys.argv[2]


complete_terms = defaultdict(set)
incomplete_terms = defaultdict(set)
for line in open(wordfile):
    line = line.strip().split(" ")
    lastword = line[-1]
    line = line[:-1]
    complete_terms[' '.join(line)].add(lastword)
    while line:
        lastword = line[-1]
        line = line[:-1]
        incomplete_terms[' '.join(line)].add(lastword)
        
for line in open(textfile):
    line = line.strip()
    words = line.split(' ')
    incompletes = set()
    for word in words:
        if word in complete_terms['']:
            print(line)
            break
        found = False
        new_incompletes = set()
        for incomplete in incompletes:
            if word in complete_terms[incomplete]:
                found = True
                break
            if word in incomplete_terms[incomplete]: new_incompletes.add(incomplete + " " + word)
            else: incompletes.remove(incomplete)
            if word in incomplete_terms['']: new_incompletes.add(word)
        if found:
            print(line)
            break
        incompletes |= new_incompletes


