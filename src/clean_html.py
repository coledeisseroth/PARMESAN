import sys
import os
from collections import defaultdict
import re

cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def main(htmlfile):
  lines = []
  for line in open(htmlfile): lines.append(line.strip())
  htmlfile = "\n".join(lines)
  cleanfile = cleanhtml(htmlfile)
  print cleanfile

if __name__ == "__main__": main(sys.argv[1])

