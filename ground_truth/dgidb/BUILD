cd raw
bash BUILD
cd ..
while [ $(ls ../../mappings/pubchem/ | grep PUBCHEM_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
cat raw/interactions.tsv | cut -f2,6,8 | grep "hgnc:" | sed 's/hgnc:/HGNC:/g' | awk '$2 != "NULL" && $3 != "NULL"' | sort -k1,1 | join -t$'\t' <(cat ../../mappings/hgnc/hgnc_to_entrez.txt | sort -k1,1) - | cut -f2- | sort -u | awk 'BEGIN {FS = "\t"} $1 != "" && $2 != "" && $3 != "" && NR > 1 {$3 = tolower($3); gsub(" ", "", $3); gsub("-", "", $3); gsub(";", "", $3); gsub(",", "", $3); print $1 "\t" $2 "\t" $3}' | sort -k2,2 | join -t$'\t' -1 2 -2 1 - <(cat raw/label_directionality.txt | sort -k1,1) | cut -f2- | awk 'BEGIN {FS = "\t"} $3 != 0' | sort -t$'\t' -k2,2 | join -t$'\t' -1 2 -2 1 - <(cat ../../mappings/pubchem/filtered_id_maps.txt | sort -k1,1) | awk 'BEGIN {FS = "\t"} {print $4 "\t" $2 "\t" $3}' | sort -u > mod_to_entrez.txt
cat raw/interactions2022.tsv | cut -f11 | sed 's/,/\n/g' | awk 'NR > 1 && $1 != ""' |  sort -u > dgidb_pmids.txt

touch DGIDB_COMPLETE

