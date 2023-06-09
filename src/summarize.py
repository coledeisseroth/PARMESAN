import sys
import os
from collections import defaultdict
import vocabulary

def main(splitfile):
  predicates = set(vocabulary.find_words(["predicate"]))
  actions = set(vocabulary.find_words(["action"]))
  problems = set(vocabulary.find_words(["problem"]))
  for line in open(splitfile):
    lineData = line.strip("\n").split("\t")
    pmid = lineData[0]
    modifier = lineData[1]
    target = lineData[2]
    predicate = lineData[3]
    subj = lineData[4]
    obj = lineData[5]
    presubj = lineData[6]
    postsubj = lineData[7]
    preobj = lineData[8]
    postobj = lineData[9]
    if len(postsubj) >= 4 and postsubj[-4:] == " and": continue
    if postsubj == "and": continue
    if set(preobj.lower().split(" ")) & predicates: continue
    preSubjectWords = presubj.lower().split(" ")
    preSubjectActions = set(preSubjectWords) & actions
    preSubjectWords.reverse()
    action = None
    actionIndex = None
    for word in preSubjectActions:
      if not word: continue
      index = preSubjectWords.index(word)
      if action is None or index < actionIndex:
        action = word
        actionIndex = index
    postSubjectWords = postsubj.lower().split(" ")
    postSubjectActions = set(postSubjectWords) & actions
    for word in postSubjectActions:
      if not word: continue
      index = postSubjectWords.index(word)
      if action is None or index < actionIndex: 
        action = word
        actionIndex = index
    if not action: action = "."
    problem = None
    problemIndex = None
    postobjectWords = postobj.lower().split(" ")
    postobjectProblems = set(postobjectWords) & problems
    for word in postobjectProblems:
      index = postobjectWords.index(word)
      if problem is None or index < problemIndex:
        problem = word
        problemIndex = index
    preobjectWords = preobj.lower().split(" ")
    preobjectProblems = set(preobjectWords) & problems
    preobjectWords.reverse()
    for word in preobjectProblems:
      index = preobjectWords.index(word)
      if problem is None or index < problemIndex:
        problem = word
        problemIndex = index
    if not problem: problem = "."
    wholesentence = set(" ".join([presubj, postsubj, preobj, postobj]).lower().split(" "))
    model = "."
    print("\t".join([pmid, modifier, predicate, problem, target, action, model]))


if __name__ == "__main__":
  main(sys.argv[1])


