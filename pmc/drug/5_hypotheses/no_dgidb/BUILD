mkdir pergene
for gene in $(cat ../../../gene/4_parmesan/directionality/consensus_directionality.txt | cut -f2 | sort -u); do
while [ $(jobs | grep 'Running\|Done' | wc -l) -gt 40 ]; do jobs; sleep 1; done
cat ../../../gene/4_parmesan/directionality/consensus_directionality.txt | awk '$2 == '$gene | sort -k1,1 | join -t$'\t' -1 2 -2 1 <(cat ../../4_parmesan/no_dgidb/consensus_directionality.txt | sort -k2,2) - | awk '{print $2 "_" $4 "\t" $1 "\t" ($3 * $5) / (sqrt($3 * $3) + sqrt($5 * $5))}' | sort -u | sort -k1,1 | awk 'BEGIN {cur=""; p=0; n=0} {if($1 != cur){if(cur != "" && p + n > 0){print cur "\t" (p - n) * sqrt((p - n) ** 2) / (p + n)} cur = $1; p = 0; n = 0} if($3 > 0){p += $3} else if($3 < 0){n -= $3}} END {if(p + n > 0){print cur "\t" (p - n) * sqrt((p - n) ** 2) / (p + n)}}' | awk '$2 != 0' | sed 's/_/\t/g' > pergene/$gene &
done
while [ $(jobs | grep 'Running\|Done' | wc -l) -gt 0 ]; do jobs; sleep 1; done

for file in $(ls pergene); do cat pergene/$file | awk '{print $1 "_" $2 "\t" $3}' | sort -k1,1 | join -t$'\t' - <(cat ../../../../ground_truth/dgidb/mod_to_entrez.txt | awk '$2 == "'$file'" {print $1 "_" $2 "\t" $3}' | sort -k1,1); done > raw_dgidb_comparison.txt
for i in 0 $(seq 100); do cat raw_dgidb_comparison.txt | awk 'sqrt($2 ** 2) > '$i | awk '{print $2 * $3}' | awk 'BEGIN {p = 0; n = 0} {if($1 > 0){p += 1} else{n += 1}} END {print "'$i'\t" p "\t" n "\t" p / (p + n)}'; done > dgidb_raw_scoretable.txt

for file in $(ls pergene); do cat pergene/$file | cut -f3 | awk '{print int(sqrt($1 ^ 2))}' | sort | uniq -c | awk '{print $2 "\t" $1}'; done | sort -k1,1gr | awk 'BEGIN {n = ""; t = 0} {if(n != "" && n != $1) {print n "\t" t} n = $1; t += $2} END {print n "\t" t}' > score_to_count.txt

for i in $(cat dgidb_raw_scoretable.txt | cut -f1); do cat dgidb_raw_scoretable.txt | awk '$1 <= '$i | cut -f4 | sort -gr | head -1 | awk '{print "'$i'\t" $0}'; done | sort -k1,1 | join -t$'\t' - <(cat score_to_count.txt | sort -k1,1) | cut -f2- | sort -k2,2gr | sort -k1,1gr -u > raw_accuracy_distribution.txt

for gene in $(ls pergene); do cat pergene/$gene | cut -f3 | awk 'BEGIN {max=0} {$1 = sqrt($1 ^ 2); if($1 > max){max = $1}} END {if(max > 0){print max}}'; done | sort -gr | awk 'BEGIN {t = 0} {t += 1; print $1 "\t" t}' | sort -k2,2gr | sort -k1,1g -u > minscore_to_no_genes.txt


for file in $(ls pergene); do cat pergene/$file | cut -f3 | awk '{print sqrt($1 ^ 2)}' | sort | uniq -c | awk '{print $2 "\t" $1}'; done | sort -k1,1gr | awk 'BEGIN {n = ""; t = 0} {if(n != "" && n != $1) {print n "\t" t} n = $1; t += $2} END {print n "\t" t}' > score_to_count_exact.txt

totalgenes=$(ls pergene | wc -l); for entry in $(cat minscore_to_no_genes.txt | sed 's/\t/,/g'); do minscore=$(echo $entry | cut -d, -f1); recall=$(echo $entry | cut -d, -f2 | awk '{print $1 / '$totalgenes'}'); precision=$(cat raw_dgidb_comparison.txt | awk 'BEGIN {FS = "\t"; p = 0; n = 0} sqrt($2 ^ 2) >= '$minscore' {if($2 * $3 > 0){p += 1} else if($2 * $3 < 0){n += 1}} END {print p / (p + n)}'); echo $precision$'\t'$recall; done > precision_recall_raw.txt
cat precision_recall_raw.txt | sort -k2,2gr | awk 'BEGIN {FS = "\t"; pprev = ""; rprev = ""} pprev == "" || ($1 > pprev || $2 > rprev) {print; pprev = $1; rprev = $2}' > precision_recall_curve.txt

#Get AUC
bash ../../../../src/auc.sh <(echo $'0\t1'; cat precision_recall_curve.txt; echo $'1\t0')



