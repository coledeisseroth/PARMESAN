mkdir 0_pubmed
mkdir 1_annotated_articles

while [ $(ls ../../ground_truth/pubmed/ | grep PUBMED_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done

for file in $(ls ../../ground_truth/pubmed/baseline/*); do
python3 ../../src/parse_pubmed_xml.py $file > 0_pubmed/$(echo $file | rev | cut -d'/' -f1 | rev | sed 's/\.xml\.gz/.txt/g')
done

while [ $(ls ../../ground_truth/pubtator/ | grep PUBTATOR_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done

for file in $(ls 0_pubmed/*); do
while [ $(jobs | grep 'Running\|Done' | wc -l) -gt 40 ]; do jobs; sleep 1; done
cat $file | sort -k1,1 | join -t$'\t' - ../../ground_truth/pubtator/combined_genes_and_chemicals.txt > 1_annotated_articles/$(echo $file | rev | cut -d'/' -f1 | rev) &
done
while [ $(jobs | grep 'Running\|Done' | wc -l) -gt 0 ]; do jobs; sleep 1; done

for file in $(ls 1_annotated_articles); do python3 ../../src/cooccurrences.py 1_annotated_articles/$file; done > 2_cooccurrences.txt

python3 ../../src/subject_object.py 2_cooccurrences.txt <(cat ../../src/vocabulary.py | grep -v "#" | grep 'positive\|negative' | grep predicate | cut -d'"' -f2) > 3_subject_object_split.txt

cd 4_parmesan
bash BUILD
cd ../5_hypotheses
bash BUILD
cd ..

