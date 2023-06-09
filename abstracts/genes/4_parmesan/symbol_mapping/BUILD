cd 1_hgnc
bash BUILD
cd ../2_entrez
bash BUILD
cd ..

cat 1_hgnc/level1.txt 2_entrez/level2.txt | sed 's/-//g' | sort -u > entrez_to_symbol_nodashes.txt

