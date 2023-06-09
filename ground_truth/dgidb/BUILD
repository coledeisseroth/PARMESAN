cd raw
bash BUILD
cd ..
while [ $(ls ../../mappings/pubchem/ | grep PUBCHEM_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
cat raw/interactions.tsv | cut -f3,5,7 | awk 'BEGIN {FS = "\t"} $1 != "" && $2 != "" && $3 != "" && NR > 1 {$3 = tolower($3); gsub(" ", "", $3); gsub("-", "", $3); gsub(";", "", $3); gsub(",", "", $3); print $1 "\t" $2 "\t" $3}' | sort -k2,2 | join -t$'\t' -1 2 -2 1 - <(cat raw/label_directionality.txt | sort -k1,1) | cut -f2- | awk 'BEGIN {FS = "\t"} $3 != 0' | sort -t$'\t' -k2,2 | join -t$'\t' -1 2 -2 1 - <(cat ../../mappings/pubchem/filtered_id_maps.txt | sort -k1,1) | awk 'BEGIN {FS = "\t"} {print $4 "\t" $2 "\t" $3}' | sort -u > mod_to_entrez.txt
cat raw/interactions.tsv | cut -f11 | awk 'NR > 1 && $1 != ""' |  sort -u > dgidb_pmids.txt

touch DGIDB_COMPLETE

#cat mod_to_entrez.txt | sort -u | cut -f3 | awk 'BEGIN {FS = "\t"; p = 0; n = 0} {if($1 > 0){p += 1} else if($1 < 0){n += 1}} END {print 1 - (p / (p + n))}'

