while [ $(ls ../../../../../mappings/entrez/ | grep ENTREZ_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done

#cp ../../../../mappings/entrez/best_entrez_to_symbol.txt entrez_best_symbols.txt
#cat entrez_best_symbols.txt | awk '{print toupper($0)}' | cut -f2 | sort -u | comm -23 - <(cat ../1_hgnc/level1.txt | cut -f2 | sort -u)
cat ../../../../../mappings/entrez/best_entrez_to_symbol.txt | awk '{print toupper($0)}' | cut -f2 | sort -u | comm -23 - <(cat ../1_hgnc/level1.txt | cut -f2 | sort -u) | join -t$'\t' -1 1 -2 2 - <(cat ../../../../../mappings/entrez/best_entrez_to_symbol.txt | sort -k2,2) | awk '{print $2 "\t" $1}' > entrez_only.txt
cat entrez_only.txt ../1_hgnc/level1.txt | sort -u > level2.txt


