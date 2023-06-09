mkdir pergene
mkdir completion
for gene in $(cat ../../4_parmesan/timecapsule/2012_consensus_directionality.txt | cut -f2 | sort -u); do
while [ $(jobs | wc -l) -gt 40 ]; do sleep 1; done
(cat ../../4_parmesan/timecapsule/2012_consensus_directionality.txt | awk '$2 == '$gene | sort -k1,1 | join -t$'\t' -1 2 -2 1 <(cat ../../4_parmesan/timecapsule/2012_consensus_directionality.txt | sort -k2,2) - | awk '{print $2 "_" $4 "\t" $1 "\t" ($3 * $5) / (sqrt($3 * $3) + sqrt($5 * $5))}' | sort -u | sort -k1,1 | awk 'BEGIN {cur=""; p=0; n=0} {if($1 != cur){if(cur != "" && p + n > 0){print cur "\t" (p - n) * sqrt((p - n) ** 2) / (p + n)} cur = $1; p = 0; n = 0} if($3 > 0){p += $3} else if($3 < 0){n -= $3}} END {if(p + n > 0){print cur "\t" (p - n) * sqrt((p - n) ** 2) / (p + n)}}' | awk '$2 != 0' | sed 's/_/\t/g' > pergene/$gene; touch completion/$gene) &
done

while [ $(ls completion | wc -l) -lt $(cat ../../4_parmesan/timecapsule/2012_consensus_directionality.txt | cut -f2 | sort -u | wc -l) ]; do sleep 1; done

for file in $(ls pergene); do cat pergene/$file | awk '{print $1 "_" $2 "\t" $3}' | sort -k1,1 | join -t$'\t' - <(cat ../../../../no_text_mining/reactome_entrez.txt | awk '$2 == "'$file'" {print $1 "_" $2 "\t" $3}' | sort -k1,1); done > raw_reactome_comparison.txt
for i in 0 $(seq 100); do cat raw_reactome_comparison.txt | awk 'sqrt($2 ** 2) > '$i | awk '{print $2 * $3}' | awk 'BEGIN {p = 0; n = 0} {if($1 > 0){p += 1} else{n += 1}} END {print "'$i'\t" p "\t" n "\t" p / (p + n)}'; done > reactome_raw_scoretable.txt

for file in $(ls pergene); do cat pergene/$file | cut -f3 | awk '{print int(sqrt($1 ^ 2))}' | sort | uniq -c | awk '{print $2 "\t" $1}'; done | sort -k1,1gr | awk 'BEGIN {n = ""; t = 0} {if(n != "" && n != $1) {print n "\t" t} n = $1; t += $2} END {print n "\t" t}' > score_to_count.txt

for i in $(cat reactome_raw_scoretable.txt | cut -f1); do cat reactome_raw_scoretable.txt | awk '$1 <= '$i | cut -f4 | sort -gr | head -1 | awk '{print "'$i'\t" $0}'; done | sort -k1,1 | join -t$'\t' - <(cat score_to_count.txt | sort -k1,1) | cut -f2- | sort -k2,2gr | sort -k1,1gr -u > raw_accuracy_distribution.txt

for gene in $(ls pergene); do cat pergene/$gene | cut -f3 | awk 'BEGIN {max=0} {$1 = sqrt($1 ^ 2); if($1 > max){max = $1}} END {print max}'; done | sort -gr | awk 'BEGIN {t = 0} {t += 1; print $1 "\t" t}' | sort -k2,2gr | sort -k1,1g -u > minscore_to_no_genes.txt

for year in 2012 2022; do
cat pergene/* | awk 'BEGIN {FS = "\t"}{print $1 "_" $2 "\t" $3}' | sort -k1,1 | join -t$'\t' - <(cat ../../4_parmesan/timecapsule/${year}_consensus_directionality.txt | awk 'BEGIN {FS = "\t"} {print $1 "_" $2 "\t" $3}' | sort -k1,1) > ${year}_comparison.txt
for i in 0 $(seq 100); do cat ${year}_comparison.txt | awk 'sqrt($2 ** 2) > '$i | awk '{print $2 * $3}' | awk 'BEGIN {p = 0; n = 0} {if($1 > 0){p += 1} else{n += 1}} END {print "'$i'\t" p "\t" n "\t" p / (p + n)}'; done > ${year}_scoretable.txt
n1=$(cat score_to_count.txt | awk '$1 == 0' | head -1 | cut -f2)
c1=$(cat ${year}_scoretable.txt | awk '$1 == 0' | cut -f2)
for i in $(seq 100); do
n2=$(cat score_to_count.txt | awk '$1 >= '$i | sort -k1,1g | head -1 | cut -f2)
c2=$(cat ${year}_scoretable.txt | awk '$1 == '$i | cut -f2)
python3 ../../../../src/2p_binomial.py <(echo $n1$'\t'$c1; echo $n2$'\t'$c2) | grep pvalue | awk '{print "'$i'\t" $3}'
done > ${year}_pvalues_versus_zero.txt
done

n1=$(cat score_to_count.txt | awk '$1 == 0' | head -1 | cut -f2)
c1=$(cat 2012_scoretable.txt | cut -f-2 | sort -k1,1 | join -t$'\t' - <(cat 2022_scoretable.txt | cut -f-2 | sort -k1,1) | awk '{print $1 "\t" $3 - $2}' | sort -k1,1 | awk '$1 == 0' | cut -f2)
for i in $(seq 100); do
n2=$(cat score_to_count.txt | awk '$1 >= '$i | sort -k1,1g | head -1 | cut -f2)
c2=$(cat 2012_scoretable.txt | cut -f-2 | sort -k1,1 | join -t$'\t' - <(cat 2022_scoretable.txt | cut -f-2 | sort -k1,1) | awk '{print $1 "\t" $3 - $2}' | sort -k1,1 | awk '$1 == '$i | cut -f2)
python3 ../../../../src/2p_binomial.py <(echo $n1$'\t'$c1; echo $n2$'\t'$c2) | grep pvalue | awk '{print "'$i'\t" $3}'
done > interval_pvalues_versus_zero.txt

bestthreshold=$(cat 2012_scoretable.txt | cut -f-2 | sort -k1,1 | join -t$'\t' - <(cat 2022_scoretable.txt | cut -f-2 | sort -k1,1) | awk '{print $1 "\t" $3 - $2}' | sort -k1,1 | join -t$'\t' - <(for i in $(seq 0 100); do cat score_to_count.txt | awk '$1 >= '$i | sort -k1,1g | head -1 | cut -f2 | awk '{print "'$i'\t" $1}'; done | sort -k1,1) | awk '{print $1 "\t" $2 / $3}' | sort -k2,2gr | head -1 | cut -f1)
n1=$(cat score_to_count.txt | awk '$1 >= '$bestthreshold | sort -k1,1g | head -1 | cut -f2)
c1=$(cat 2012_scoretable.txt | cut -f-2 | sort -k1,1 | join -t$'\t' - <(cat 2022_scoretable.txt | cut -f-2 | sort -k1,1) | awk '{print $1 "\t" $3 - $2}' | sort -k1,1 | awk '$1 == '$bestthreshold | cut -f2)
for i in $(seq 0 100); do
n2=$(cat score_to_count.txt | awk '$1 >= '$i | sort -k1,1g | head -1 | cut -f2)
c2=$(cat 2012_scoretable.txt | cut -f-2 | sort -k1,1 | join -t$'\t' - <(cat 2022_scoretable.txt | cut -f-2 | sort -k1,1) | awk '{print $1 "\t" $3 - $2}' | sort -k1,1 | awk '$1 == '$i | cut -f2)
python3 ../../../../src/2p_binomial.py <(echo $n1$'\t'$c1; echo $n2$'\t'$c2) | grep pvalue | awk '{print "'$i'\t" $3}'
done > interval_pvalues_versus_bestthreshold.txt


cat pergene/6622 | cut -f1,3 | sort -k1,1 | join -t$'\t' <(cat ../../../../mappings/entrez/entrez_to_primary_name.txt | sort -k1,1) - > snca_modifier_predictions.txt


