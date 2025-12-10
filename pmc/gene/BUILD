mkdir 0_pmc

while [ $(ls ../../ground_truth/pmc/ | grep PMC_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done

for distdir in $(ls ../../ground_truth/pmc/unzipped/); do
for zipdir in $(ls ../../ground_truth/pmc/unzipped/$distdir); do
mkdir 0_pmc/${zipdir}_${distdir}
for pmcid in $(ls ../../ground_truth/pmc/unzipped/$distdir/$zipdir | cut -d. -f1); do
while [ $(jobs | grep 'Running\|Done' | wc -l) -gt 40 ]; do jobs; sleep 0.1; done
(echo -n $(cat ../../ground_truth/pmc/pmc_to_pmid.txt | awk '$1 == "'$pmcid'"' | head -1 | cut -f2); echo -n $'\t.\t'; cat ../../ground_truth/pmc/unzipped/$distdir/$zipdir/$pmcid.txt | sed 's/\t/ . /g' | paste -sd' . ') > 0_pmc/${zipdir}_${distdir}/${pmcid}.txt &
done
done
done
while [ $(jobs | grep Running | wc -l) -gt 0 ]; do jobs; sleep 1; done

for dir in $(ls 0_pmc); do for file in $(ls 0_pmc/$dir); do wc -l 0_pmc/$dir/$file; done; done
for dir in $(ls 0_pmc); do for file in $(ls 0_pmc/$dir); do wc -l 0_pmc/$dir/$file; done; done | awk '$1 < 1 {print $2}' > missed_files.txt

while [ $(ls ../../ground_truth/pubtator/ | grep PUBTATOR_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done

cd annotations_only
bash BUILD
cd ..

mkdir 2_cooccurrences
for dir in $(ls 0_pmc | grep -v '.txt'); do
for file in $(ls 0_pmc/$dir); do
while [ $(jobs | wc -l) -gt 80 ]; do jobs; sleep 0.1; done
for x in $(ls annotations_only/annotations/$file); do
python3 ../../src/cooccurrences.py <(cat 0_pmc/$dir/$file annotations_only/annotations/$file | paste -sd$'\t') > 2_cooccurrences/$file &
done
done
done
while [ $(jobs | wc -l) -gt 0 ]; do jobs; sleep 1; done

mkdir 3_subject_object
for file in $(ls annotations_only/split); do
python3 ../../src/subject_object.py <(for pmcid in $(cat annotations_only/split/$file | cut -f1); do cat 2_cooccurrences/$pmcid.txt; done) <(cat ../../src/vocabulary.py | grep -v "#" | grep 'positive\|negative' | grep predicate | cut -d'"' -f2) > 3_subject_object/$file &
done
while [ $(jobs | wc -l) -gt 0 ]; do jobs; sleep 1; done
cat 3_subject_object/* > 3_subject_object_split.txt

rm -r 2_cooccurrences

cd 4_parmesan
bash BUILD
cd ..
cd 5_hypotheses
bash BUILD
cd ..
cd 6_hypotheses_with_pubmed
bash BUILD

