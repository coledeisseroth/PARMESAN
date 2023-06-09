import sys
import os
from collections import defaultdict

absolute = False
if "-a" in sys.argv:
    absolute = True
    sys.argv.remove("-a")

def commit(rate, rates):
    returnRates = []
    for rate2 in rates:
        if rate2[0] >= rate[0] and rate2[1] <= rate[1]:
            return rates
        if rate2[0] <= rate[0] and rate2[1] >= rate[1]:
            continue
        returnRates.append(rate2)
    returnRates.append(rate)
    return returnRates


tp = 0
tn = 0
fp = 0
fn = 0
rates = []
prev = None
curRate = None
for line in open(sys.argv[1]):
    line = line.strip().split("\t")
    pred = float(line[0])
    truth = int(line[1])
    if truth > 0 and pred > 0: tp += 1
    elif truth > 0 and pred < 0: fn += 1
    elif truth < 0 and pred > 0: fp += 1
    elif truth < 0 and pred < 0: tn += 1
    elif truth > 0 and pred < 0: fn += 1
    pred = float(line[0])
    if absolute: pred = abs(pred)
    if curRate and prev and pred != prev: rates = commit(curRate, rates)
    prev = pred
    if tp + fn: tpr = 1.0 * tp / (tp + fn)
    else: tpr = 0
    if fp + tn: fpr = 1.0 * fp / (fp + tn)
    else: fpr = 0
    curRate = [tpr, fpr]
rates = commit(curRate, rates)
rates = [[0, 0]] + rates + [[1, 1]]

rates.sort(key=(lambda x: x[1]))

prevRate = None
areasum = 0
for rate in rates:
    if prevRate:
        areasum += prevRate[0] * (rate[1] - prevRate[1])
        areasum += (rate[0] - prevRate[0]) * (rate[1] - prevRate[1]) * 0.5
    prevRate = rate
    #print(str(rate[1]) + "\t" + str(rate[0]))
print(areasum)

