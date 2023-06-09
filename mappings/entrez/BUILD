cd raw
bash BUILD
cd ..

zcat raw/gene_info.gz | cut -f2,3,5,11 | sed 's/ \|\t/|/g' | sed 's/|-//g' | tr '[:lower:]' '[:upper:]' | awk '{print $0 "|"}' > gene_to_alias_expanded.txt
#zcat raw/gene2ensembl.gz | grep ENSG0 | cut -f2 | sort -u > human_genes.txt
zcat raw/gene_info.gz | awk '$1 == 9606' | cut -f2 | sort -u > human_genes.txt

cat gene_to_alias_expanded.txt | sed 's/|/\t/g' | sort -k1,1 | join -t$'\t' - human_genes.txt | sed 's/\t/|/g' > human_gene_to_alias.txt
for line in $(cat human_gene_to_alias.txt); do  entrez=$(echo $line | cut -d'|' -f1); for alias in $(echo $line | cut -d'|' -f2- | sed 's/|/\n/g' | awk '$1 != ""' | awk '{print $0 "|" NR}'); do  echo $entrez$'\t'$alias; done; done | sed 's/|/\t/g' | sort -k2,2 -k3,3g -k1,1g | sort -k2,2 -u | cut -f1,2 > best_entrez_to_symbol.txt

cat gene_to_alias_expanded.txt | cut -d'|' -f2- | rev | cut -d'|' -f2- | rev | grep "|" > tmp
cat tmp | sed 's/|/\t/g' | sort -k1,1 | join -t$'\t' - <(cat human_gene_to_alias.txt | cut -d'|' -f2- | sed 's/|/\n/g' | sort -u) | sed 's/\t/|/g' > tmp2
cat tmp2 | sort -u > tmp3
cat tmp3 | grep -v "_" > tmp4

for line in $(cat tmp4); do  symbol=$(echo $line | cut -d'|' -f1); for alias in $(echo $line | cut -d'|' -f2- | sed 's/|/\n/g' | awk '$1 != ""' | awk '{print $0 "|" NR}'); do  echo $symbol$'\t'$alias; done; done | sed 's/|/\t/g' | sort -k2,2 -k3,3g -k1,1g | sort -k2,2 -u | cut -f1,2 > best_alias_to_symbol.txt

cat human_gene_to_alias.txt | tr '[:upper:]' '[:lower:]' | awk 'BEGIN {FS = "|"} {for(i = 2; i <= NF; i += 1) {print $1 "\t" $i}}' | awk 'NF > 1' | sort -u > human_gene_clinphen_map.txt

zcat raw/gene_info.gz | awk '$1 == 9606' | cut -f2,3 | sort -u > entrez_to_primary_name.txt

touch ENTREZ_COMPLETE

