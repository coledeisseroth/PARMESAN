mkdir id_maps
for file in $(curl https://ftp.ncbi.nlm.nih.gov/pubchem/Substance/CURRENT-Full/XML/ | grep '\.xml\.gz' | grep -v '\.md5' | cut -d'"' -f2 | sort -u); do
curl https://ftp.ncbi.nlm.nih.gov/pubchem/Substance/CURRENT-Full/XML/$file | zcat | grep '</PC-ID_id>\|<PC-Substance_synonyms_E>' | cut -d'<' -f-2 | paste -s | sed 's/<PC-ID_id>/\n/g' | awk 'NR > 1' | sed 's/\t//g' | sed 's/ *<PC-Substance_synonyms_E>/|/g' | awk 'BEGIN {FS = "|"} {for(i = 2; i <= NF; i += 1){print $1 "\t" $i}}' | tr '[:upper:]' '[:lower:]' | sort -u > id_maps/${file%.xml.gz}.txt
sleep 1
done

while [ $(ls ../../ground_truth/pubtator/chemicals/ | grep PUBTATOR_CHEMICALS_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done

zcat ../../ground_truth/pubtator/chemicals/chemical2pubtator3.gz | cut -f4 | sed 's/|/\n/g' | tr '[:upper:]' '[:lower:]' | awk 'BEGIN {FS = "\t"} $1 != "" {key = $1; gsub(" ", "", key); gsub("-", "", key); gsub(";", "", key); gsub(",", "", key); print key}' | awk '$1 != ""' | sort -u > pubtator_names.txt

for file in $(ls id_maps); do
cat id_maps/$file | awk 'BEGIN {FS = "\t"} {key = $2; gsub(" ", "", key); gsub("-", "", key); gsub(";", "", key); gsub(",", "", key); print key "\t" $0}' | sort -t$'\t' -k1,1 | join -t$'\t' - pubtator_names.txt | cut -f-2 | sort -u
done | sort -t$'\t' -k1,1 -k2,2 -u | sort -t$'\t' -k1,1 -u > filtered_id_maps.txt

zcat raw/SID-Synonym.gz | awk 'BEGIN {FS = "\t"; cur = ""; firstname = ""} {if(cur != $1){print} cur = $1}' > substance_id_to_primary_name.txt

mkdir split
cd split
split -l $(cat ../substance_id_to_primary_name.txt | wc -l | awk '{print int($1 / 1000)}') ../substance_id_to_primary_name.txt
cd ..
mkdir split_output
cd split_output
for file in $(ls ../split); do
cat ../filtered_id_maps.txt | cut -f2 | sort -u | join -t$'\t' - <(cat ../split/$file | sort -t$'\t' -k1,1) > $file
done
cd ..
cat split_output/* > used_substance_primary_names.txt
rm -r split split_output/


touch PUBCHEM_COMPLETE

