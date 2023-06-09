import sys
import os
from collections import defaultdict

def process_info(curPmid, summaries):
  blacklist = []
  for i in range(len(summaries)):
    summary1 = summaries[i]
    m1 = summary1[1]
    p1 = summary1[2]
    t1 = summary1[4]
    a1 = summary1[5]
    for j in range(i+1, len(summaries)):
      summary2 = summaries[j]
      m2 = summary2[1]
      p2 = summary2[2]
      t2 = summary2[4]
      a2 = summary2[5]
      if p1 != p2 or a1 != a2: continue
      if m1 == m2:
        if t1 == t2: continue
        if t1 in t2: blacklist.append(summary1)
        if t2 in t1: blacklist.append(summary2)
      elif t1 == t2:
        if m1 in m2: blacklist.append(summary1)
        if m2 in m1: blacklist.append(summary2)
  for summary in blacklist: print("\t".join(summary))
      

def main(findingfile):
  curPmid = None
  summaries = []
  for line in os.popen("cat " + findingfile + " | sort -k1,1"):
    line = line.strip()
    lineData = line.split("\t")
    pmid = lineData[0]
    if curPmid is None: curPmid = pmid
    elif curPmid != pmid:
      process_info(curPmid, summaries)
      curPmid = pmid
      summaries = []
    summaries.append(lineData)
  process_info(curPmid, summaries)

if __name__ == "__main__":
  main(sys.argv[1])

