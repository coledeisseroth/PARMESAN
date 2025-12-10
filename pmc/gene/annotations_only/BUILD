cat ../../../ground_truth/pubtator/combined_genes_and_chemicals.txt | sort -t$'\t' -k1,1 | join -t$'\t' -1 2 -2 1 <(cat ../../../ground_truth/pmc/pmc_to_pmid.txt | sort -t$'\t' -k2,2) - | cut -f2- > pmc_annotations.txt

mkdir split
cd split
split -l $(cat ../pmc_annotations.txt | wc -l | awk '{print int($1 / 40)}') ../pmc_annotations.txt
cd ..

mkdir annotations
for file in $(ls split); do
cat split/$file | awk 'BEGIN {FS = "\t"} {print $2 "\t" $3 > "annotations/" $1 ".txt"}' &
done
while [ $(jobs | wc -l) -gt 0 ]; do jobs; sleep 1; done



