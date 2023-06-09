for year in 2012 2022; do
cat ../${year}_consensus_directionality.txt | awk '$2 == 6622' | cut -f1,2 | sed 's/\t/_/g' | sort -u > ${year}_relationships.txt
cat ../${year}_directionality.txt | awk '$3 == 6622' | cut -f1 | sort -u | join -t$'\t' -1 1 -2 3 - <(cat ../../directionality_abstracts/ortholog_mapping.txt | sort -k3,3) | awk 'BEGIN {FS = "\t"} {print $2 "\t" $3 "\t" $0}' | cut -f-3,6- > ${year}_ortholog_mapping.txt
cat ${year}_ortholog_mapping.txt | awk 'BEGIN {FS = "\t"} $3 != 0 {if($5 == ".") {cmod = $1} else {cmod = $5} if($8 == "."){ctarg = $2} else{ctarg = $8} print cmod "_" ctarg "\t" $3 "_" $1 "_" $2 "\t" $0}' | grep -wf ${year}_relationships.txt | sort -k1,1 | join -t$'\t' - <(cat ${year}_relationships.txt | sort -u) | sort -t$'\t' -k2,2 | join -t$'\t' -1 2 -2 1 - <(cat ../../summaries_with_entrez.txt ../../../../../abstracts/genes/4_parmesan/summaries_with_entrez.txt | awk 'BEGIN {FS = "\t"} {print $1 "_" $8 "_" $9 "\t" $0}' | sort -t$'\t' -k1,1) | cut -f2,6,8,9,11-15,17-18,20- | sed 's/_/\t/g' | sort -u > ${year}_relation_justification.txt
cat ${year}_relation_justification.txt | awk '{print $1 "_" $2 "\t" $0}' | sort -k1,1 | join -t$'\t' <(cat ../${year}_consensus_directionality.txt | awk '{print $1 "_" $2 "\t" $3}' | sort -k1,1) - | awk 'BEGIN {FS = "\t"} {print $3 "\t" $4 "\t" $2 "\t" $10 "\t" $15 "\t" $6 "\t" $7 "\t" $16 "\t" $8 "\t" $9 "\t" $14 " " $11 " " $12 " " $13}' | sed 's/\t\. /\t/g' | sort -u > ${year}_output_table.txt
done


