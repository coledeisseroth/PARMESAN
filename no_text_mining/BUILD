while [ $(ls ../ground_truth/reactome/ | grep REACTOME_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
while [ $(ls ../ground_truth/dgidb/ | grep DGIDB_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
while [ $(ls ../mappings/entrez/ | grep ENTREZ_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done



cat ../ground_truth/reactome/reactome_annotations.txt | sort -t$'\t' -k1,1 | join -t$'\t' -1 1 -2 2 - <(cat ../mappings/entrez/best_entrez_to_symbol.txt | sort -t$'\t' -k2,2) | sort -t$'\t' -k2,2 | join -t$'\t' -1 2 -2 2 - <(cat ../mappings/entrez/best_entrez_to_symbol.txt | sort -t$'\t' -k2,2) | sort -u | awk '{print $4 "\t" $5 "\t" $3}' | awk '$1 != $2' | sort -u > reactome_entrez.txt

cat reactome_entrez.txt | sort -k2,2 | join -t$'\t' -1 2 -2 1 - <(cat reactome_entrez.txt | sort -k1,1) | cut -f2- | awk '$1 != $3 {print $1 "_" $3 "\t" $2 * $4 / (sqrt($2 ^ 2) + sqrt($4 ^ 2))}' | sort -k1,1 | awk 'BEGIN {FS = "\t"; cur = ""; p = 0; n = 0} {if(cur != "" && cur != $1){print cur "\t" (p - n) * sqrt((p - n) ^ 2) / (p + n); p = 0; n = 0} cur = $1; if($2 > 0){p += $2} else if($2 < 0){n -= $2}} END {print cur "\t" (p - n) * sqrt((p - n) ^ 2) / (p + n)}' | sed 's/_/\t/g' | sort -u > reactome_gene_gene_predictions.txt
cat reactome_gene_gene_predictions.txt | cut -f3 | awk '{print int(sqrt($1 ^ 2))}' | sort | uniq -c | awk '{print $2 "\t" $1}' | sort -k1,1gr | awk 'BEGIN {n = ""; t = 0} {if(n != "" && n != $1) {print n "\t" t} n = $1; t += $2} END {print n "\t" t}' > gene_score_to_count.txt


#Evaluate the performance of gene-gene predictions using reactome alone
for i in 0 $(seq 100); do cat reactome_gene_gene_predictions.txt | awk '{print $1 "_" $2 "\t" $3}' | awk 'sqrt($2 * $2) > '$i | sort -k1,1 | join -t$'\t' - <(cat reactome_entrez.txt | awk '{print $1 "_" $2 "\t" $3}' | sort -u | sort -k1,1) | awk 'BEGIN {t=0; f=0} {if($2 * $3 > 0){t = t + 1} else{f = f + 1}} END {print "'$i'\t" t "\t" f "\t" t/(t+f)}'; done > gene_reactome_comparison.txt

cat ../ground_truth/dgidb/mod_to_entrez.txt | sort -k2,2 | join -t$'\t' -1 2 -2 1 - <(cat reactome_entrez.txt | sort -k1,1) | cut -f2- | awk '$1 != $3 {print $1 "_" $3 "\t" $2 * $4 / (sqrt($2 ^ 2) + sqrt($4 ^ 2))}' | sort -k1,1 | awk 'BEGIN {FS = "\t"; cur = ""; p = 0; n = 0} {if(cur != "" && cur != $1){print cur "\t" (p - n) * sqrt((p - n) ^ 2) / (p + n); p = 0; n = 0} cur = $1; if($2 > 0){p += $2} else if($2 < 0){n -= $2}} END {print cur "\t" (p - n) * sqrt((p - n) ^ 2) / (p + n)}' | sed 's/_/\t/g' | sort -u > dgidb_reactome_drug_gene_predictions.txt
cat dgidb_reactome_drug_gene_predictions.txt | cut -f3 | awk '{print int(sqrt($1 ^ 2))}' | sort | uniq -c | awk '{print $2 "\t" $1}' | sort -k1,1gr | awk 'BEGIN {n = ""; t = 0} {if(n != "" && n != $1) {print n "\t" t} n = $1; t += $2} END {print n "\t" t}' > drug_score_to_count.txt


#Evaluate the performance of drug-gene predictions using dgidb and reactome alone
for i in 0 $(seq 100); do cat dgidb_reactome_drug_gene_predictions.txt | awk '{print $1 "_" $2 "\t" $3}' | awk 'sqrt($2 * $2) > '$i | sort -k1,1 | join -t$'\t' - <(cat ../ground_truth/dgidb/mod_to_entrez.txt | awk '{print $1 "_" $2 "\t" $3}' | sort -u | sort -k1,1) | awk 'BEGIN {t=0; f=0} {if($2 * $3 > 0){t = t + 1} else{f = f + 1}} END {print "'$i'\t" t "\t" f "\t" t/(t+f)}'; done > drug_dgidb_comparison.txt



for i in $(cat gene_reactome_comparison.txt | cut -f1); do cat gene_reactome_comparison.txt | awk '$1 <= '$i | cut -f4 | sort -gr | head -1 | awk '{print "'$i'\t" $0}'; done | sort -k1,1 | join -t$'\t' - <(cat gene_score_to_count.txt | sort -k1,1) | cut -f2- | sort -k2,2gr | sort -k1,1gr -u > gene_accuracy_distribution.txt

for i in $(cat drug_dgidb_comparison.txt | cut -f1); do cat drug_dgidb_comparison.txt | awk '$1 <= '$i | cut -f4 | sort -gr | head -1 | awk '{print "'$i'\t" $0}'; done | sort -k1,1 | join -t$'\t' - <(cat drug_score_to_count.txt | sort -k1,1) | cut -f2- | sort -k2,2gr | sort -k1,1gr -u > drug_accuracy_distribution.txt

cat reactome_gene_gene_predictions.txt | cut -f2- | awk 'BEGIN {FS = "\t"} {print $1 "\t" sqrt($2 ^ 2)}' | sort -u | sort -k2,2gr | awk 'BEGIN {cur = ""; t = 0} {if($2 != cur && cur != ""){print cur "\t" t} cur = $2; t += 1} END {print cur "\t" t}' > gene_minscore_no_genes.txt
cat dgidb_reactome_drug_gene_predictions.txt | cut -f2- | awk 'BEGIN {FS = "\t"} {print $1 "\t" sqrt($2 ^ 2)}' | sort -u | sort -k2,2gr | awk 'BEGIN {cur = ""; t = 0} {if($2 != cur && cur != ""){print cur "\t" t} cur = $2; t += 1} END {print cur "\t" t}' > drug_minscore_no_genes.txt

reactome_size=$(cat reactome_entrez.txt | wc -l); cat reactome_gene_gene_predictions.txt | awk '{print $1 "_" $2 "\t" $3}' | sort -k1,1 | join -t$'\t' - <(cat reactome_entrez.txt | awk '{print $1 "_" $2 "\t" $3}' | sort -u | sort -k1,1) | awk 'BEGIN {FS = "\t"} $2 * $3 != 0 {prod = $2 * $3; print sqrt($2 ^ 2) "\t" prod / sqrt(prod ^ 2)}' | sort -k1,1g | awk 'BEGIN {FS = "\t"; tp = 0; tn = '$reactome_size'; fp = 0; fn = '$reactome_size'; cur = ""; print "0\t0"} {if(cur != "" && cur != $1){tpr = tp / (tp + fn); fpr = fp / (fp + tn); print fpr "\t" tpr} cur = $1; if($2 > 0){tp += 1; fn -= 1} else if($2 < 0){fp += 1; tn -= 1}} END {tpr = tp / (tp + fn); fpr = fp / (fp + tn); print fpr "\t" tpr; print "1\t1"}' | sort -k2,2gr | sort -k1,1g -u | sort -k2,2 -u | sort -k1,1g > reactome_roc.txt

dgidb_size=$(cat ../ground_truth/dgidb/mod_to_entrez.txt | wc -l); cat dgidb_reactome_drug_gene_predictions.txt | awk '{print $1 "_" $2 "\t" $3}' | sort -k1,1 | join -t$'\t' - <(cat ../ground_truth/dgidb/mod_to_entrez.txt | awk '{print $1 "_" $2 "\t" $3}' | sort -u | sort -k1,1) | awk 'BEGIN {FS = "\t"} $2 * $3 != 0 {prod = $2 * $3; print sqrt($2 ^ 2) "\t" prod / sqrt(prod ^ 2)}' | sort -k1,1g | awk 'BEGIN {FS = "\t"; tp = 0; tn = '$dgidb_size'; fp = 0; fn = '$dgidb_size'; cur = ""; print "0\t0"} {if(cur != "" && cur != $1){tpr = tp / (tp + fn); fpr = fp / (fp + tn); print fpr "\t" tpr} cur = $1; if($2 > 0){tp += 1; fn -= 1} else if($2 < 0){fp += 1; tn -= 1}} END {tpr = tp / (tp + fn); fpr = fp / (fp + tn); print fpr "\t" tpr; print "1\t1"}' | sort -k2,2gr | sort -k1,1g -u | sort -k2,2 -u | sort -k1,1g > dgidb_roc.txt

bash ../src/auroc.sh reactome_roc.txt
bash ../src/auroc.sh dgidb_roc.txt

cat ../ground_truth/dgidb/mod_to_entrez.txt | sort -k2,2 | join -t$'\t' -1 2 -2 1 - <(cat ../abstracts/genes/udn/udn_entrez_mentioned.txt | cut -f2 | sort -u) | awk 'BEGIN {FS = "\t"} {print $2 "\t" $1 "\t" $3}' | sort -u | sort -k2,2 | join -t$'\t' -1 2 -2 1 - <(cat ../mappings/entrez/entrez_to_primary_name.txt | sort -k1,1) | sort -k2,2 | join -t$'\t' -1 2 -2 2 - <(cat ../mappings/pubchem/filtered_id_maps.txt | sort -t$'\t' -k2,2) | sort -k1,1 > udn_gene_drugs_registered.txt

touch NO_TEXT_MINING_COMPLETE

