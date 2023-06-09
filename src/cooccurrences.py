import sys
import os
from collections import defaultdict
import argparse

def main(annotated_article_file, drugs=False):
    if drugs: cooccurrences_drugs_genes(annotated_article_file)
    else: cooccurrences_genes_only(annotated_article_file)

def cooccurrences_drugs_genes(annotated_article_file):
  for line in open(annotated_article_file):
    lineData = line.strip("\n").split("\t")
    pmid = lineData[0]
    title = lineData[1]
    abstract = lineData[2]
    genes = lineData[3].split("|")
    drugs = lineData[4].split("|")
    for sentence in (title + ". " + abstract).split(". "):
      genes_in_sentence = []
      for gene in genes:
        if gene in sentence: genes_in_sentence.append(gene)
      drugs_in_sentence = []
      for drug in drugs:
        if drug in sentence and drug.strip() != "": drugs_in_sentence.append(drug)
      if len(genes_in_sentence) < 2: continue
      for i in range(len(genes_in_sentence)):
        for j in range(len(drugs_in_sentence)):
          drugfirst = True
          istartindex = sentence.index(genes_in_sentence[i])
          iendindex = istartindex + len(genes_in_sentence[i])
          jstartindex = sentence.index(drugs_in_sentence[j])
          jendindex = jstartindex + len(drugs_in_sentence[j])
          if iendindex < jstartindex:
            drugfirst = False
            firstWord = genes_in_sentence[i]
            secondWord = drugs_in_sentence[j]
            intermediate = sentence[iendindex+1:jstartindex].strip()
            prefirstword = sentence[:istartindex].strip()
            postsecondword = sentence[jendindex+1:].strip()
          elif jendindex < istartindex:
            firstWord = drugs_in_sentence[j]
            secondWord = genes_in_sentence[i]
            intermediate = sentence[jendindex+1:istartindex].strip()
            prefirstword = sentence[:jstartindex].strip()
            postsecondword = sentence[iendindex+1:].strip()
          else: continue
          print(pmid + "\t" + firstWord + "\t" + secondWord + "\t" + intermediate + "\t" + prefirstword + "\t" + postsecondword + "\t" + str(drugfirst))


def cooccurrences_genes_only(annotated_article_file):
  for line in open(annotated_article_file):
    lineData = line.strip("\n").split("\t")
    pmid = lineData[0]
    title = lineData[1]
    abstract = lineData[2]
    genes = lineData[3].split("|")
    drugs = lineData[4].split("|")
    for sentence in (title + ". " + abstract).split(". "):
      genes_in_sentence = []
      for gene in genes:
        if gene in sentence: genes_in_sentence.append(gene)
      #drugs_in_sentence = []
      #for drug in drugs:
      #  if drug in sentence: drugs_in_sentence.append(drug)
      if len(genes_in_sentence) < 2: continue
      for i in range(len(genes_in_sentence) - 1):
        for j in range(i + 1, len(genes_in_sentence)):
          istartindex = sentence.index(genes_in_sentence[i])
          iendindex = istartindex + len(genes_in_sentence[i])
          jstartindex = sentence.index(genes_in_sentence[j])
          jendindex = jstartindex + len(genes_in_sentence[j])
          if iendindex < jstartindex:
            firstWord = genes_in_sentence[i]
            secondWord = genes_in_sentence[j]
            intermediate = sentence[iendindex+1:jstartindex].strip()
            prefirstword = sentence[:istartindex].strip()
            postsecondword = sentence[jendindex+1:].strip()
          elif jendindex < istartindex:
            firstWord = genes_in_sentence[j]
            secondWord = genes_in_sentence[i]
            intermediate = sentence[jendindex+1:istartindex].strip()
            prefirstword = sentence[:jstartindex].strip()
            postsecondword = sentence[iendindex+1:].strip()
          else: continue
          print(pmid + "\t" + firstWord + "\t" + secondWord + "\t" + intermediate + "\t" + prefirstword + "\t" + postsecondword)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Split a list of shell commands across multiple nodes.')
  parser.add_argument('annotated_article_file', type=str, help='The annotated article table file')
  parser.add_argument('-d', action='store_true', help='Identify drug-gene relationships instead of gene-gene relationships')
  args = parser.parse_args()
  main(args.annotated_article_file, args.d)


