while [ $(ls ../../../../../mappings/hgnc/ | grep HGNC_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
for line in $(cat ../../../../../mappings/hgnc/entrez_to_gene_symbols.txt | tr '[:lower:]' '[:upper:]' | sed 's/\t/#/g' | sed 's/ /_/g'); do  entrez=$(echo $line | cut -d'#' -f1); echo $line | cut -d'#' -f2 | sed 's/_/\n/g' | awk '{print "'$entrez'\t" $1 "\t" NR}'; done | sort -k2,2 -k3,3g -k1,1g | sort -k2,2 -u | cut -f1,2 > best_entrez_to_symbol.txt
cat best_entrez_to_symbol.txt | awk '{print toupper($0)}' > level1.txt

