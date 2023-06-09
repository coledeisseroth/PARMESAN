mkdir raw

while [ $(ls ../entrez/ | grep ENTREZ_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done

mkdir split
cd split
split -l $(cat ../../entrez/human_genes.txt | sort -u | wc -l | awk '{print int($1 / 19)}') ../../entrez/human_genes.txt
cd ..
mkdir split/output
for file in $(ls split); do
for gene in $(cat split/$file); do curl https://www.flyrnai.org/tools/diopt/web/diopt_api/v9/get_orthologs_from_entrez/9606/$gene/all/none | awk '{print "'$gene'\t" $0}'; done > split/output/$file &
done

cat split/output/* > raw/orthologs.txt
rm -r split


(echo $'#Human_gene_entrez\tdiopt_score\tmax_diopt_score\tortholog_entrez\tspecies_id'; cat raw/orthologs.txt | awk 'BEGIN {FS = "\t"} {gsub("{\"methods\":", "\n" $1 "\t", $2); print}' | sed 's/\t.*"score":/\t/g' | sed 's/,.*"max_score":/\t/g' | sed 's/,.*"geneid":/\t/g' | sed 's/,.*"species_id":/\t/g' | cut -d, -f1 | grep -v '{') > diopt_orthologs.txt

touch DIOPT_COMPLETE

