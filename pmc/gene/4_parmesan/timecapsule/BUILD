cat ../../../../ground_truth/pubmed/dates/pmid_to_date.txt | cut -f1,2 | sort -t$'\t' -k1,1 | join -t$'\t' <(cat ../directionality_abstracts/directionality.txt | sort -t$'\t' -k1,1) - > directionality_date.txt

for year in 2012 2022; do
cat directionality_date.txt | awk 'BEGIN {FS = "\t"} $5 < '$year | cut -f-4 | sort -u > ${year}_directionality.txt
cat ${year}_directionality.txt | cut -f2- | awk '{print $1 "_" $2 "\t" $3}' | sort -k1,1 | awk 'BEGIN {rel = ""; pos = 0; neg = 0} {if($1 != rel && rel != ""){print rel "\t" pos "\t" neg; pos = 0; neg = 0} rel = $1; if($2 > 0){pos += $2} if($2 < 0){neg -= $2}} END {print rel "\t" pos "\t" neg}' | sed 's/_/\t/g' > ${year}_consensus_sums.txt
cat ${year}_consensus_sums.txt | awk '{print $1 "\t" $2 "\t" ($3 - $4) * sqrt(($3 - $4) ** 2) / ($3 + $4)}' | awk '$3 != 0' | awk '$1 != $2' > ${year}_consensus_directionality.txt
done

cd example
bash BUILD
cd ..

