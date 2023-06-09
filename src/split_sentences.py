import sys
import os
from collections import defaultdict
import re

def split_sentences(text):
  return re.split("\. |; | and ", text)

def main(passagefile):
  for line in open(passagefile):
    lineData = line.strip().split("\t")
    index = lineData[0]
    text = ". ".join(lineData[1:])
    sentences = split_sentences(text)
    for sentence in sentences: print index + "\t" + sentence

if __name__ == "__main__":
  main(sys.argv[1])

