mkdir 2_cooccurrences
for dir in $(ls ../gene/0_pmc | grep -v '.txt'); do
for file in $(ls ../gene/0_pmc/$dir); do
while [ $(jobs | wc -l) -gt 80 ]; do jobs; sleep 0.1; done
for x in $(ls ../gene/annotations_only/annotations/$file); do
python3 ../../src/cooccurrences.py <(cat ../gene/0_pmc/$dir/$file ../gene/annotations_only/annotations/$file | paste -sd$'\t') -d > 2_cooccurrences/$file &
done
done
done
while [ $(jobs | wc -l) -gt 0 ]; do   sleep 1; done

mkdir 3_subject_object
for file in $(ls ../gene/annotations_only/split); do
python3 ../../src/subject_object.py <(for pmcid in $(cat ../gene/annotations_only/split/$file | cut -f1); do cat 2_cooccurrences/$pmcid.txt; done) <(cat ../../src/vocabulary.py | grep -v "#" | grep 'positive\|negative' | grep predicate | cut -d'"' -f2) > 3_subject_object/$file &
done
while [ $(jobs | wc -l) -gt 0 ]; do jobs; sleep 1; done
cat 3_subject_object/* > 3_subject_object_split.txt


cd 4_parmesan
bash BUILD
cd ../5_hypotheses
bash BUILD
cd ../6_hypotheses_with_pubmed
bash BUILD

