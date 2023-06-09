for file in $(ls ../genes/1_annotated_articles); do python3 ../../src/cooccurrences.py ../genes/1_annotated_articles/$file -d; done > 2_cooccurrences.txt
python3 ../../src/subject_object.py 2_cooccurrences.txt <(cat ../../src/vocabulary.py | grep -v "#" | grep 'positive\|negative' | grep predicate | cut -d'"' -f2) -d > 3_subject_object_split.txt
cd 4_parmesan
bash BUILD
cd ../5_hypotheses
bash BUILD
cd ..

