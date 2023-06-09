import sys
import os
from collections import defaultdict

pmcdir = "~/Parmesan2/full_articles/raw/pmc/"

def main():
  for articledir in os.popen("ls " + pmcdir + " | grep -v tar"):
    articledir = articledir.strip()
    for articlefile in os.popen("ls " + pmcdir + "/" + articledir):
      articlefile = articlefile.strip()
      articlepath = pmcdir + "/" + articledir + "/" + articlefile
      for line in os.popen("cat " + articlepath + " | awk '$1 != \"\"' | grep -wi 'ATXN1\|ATAXIN-1\|ATAXIN 1\|SCA1'"):
        print articlepath + "\t" + line.strip()

if __name__ == "__main__": main()

