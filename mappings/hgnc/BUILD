cd raw
bash BUILD
cd ..

cat raw/hgnc_genes.txt | grep Approved | grep -vi withdrawn | sed 's/ /-/g' | cut -f2,3,5,8,9 | awk 'BEGIN {FS = "\t"} $5 != "" && NR > 1' | awk 'BEGIN {FS = "\t"} {print $5 "###" $0}' | cut -f-5 | sed 's/###/\t/g' | sed 's/",."/\t/g' | sed 's/"//g' | sed 's/  */ /g' | sort -u | rev | cut -f2- | rev | awk 'BEGIN {FS = "\t"} {for(i = 2; i <= NF; i += 1) {print $1 "\t" $i}}' | awk 'NF > 1' | sort -u > entrez_to_gene_symbols.txt
cat raw/hgnc_genes.txt | cut -f1,9 | awk 'BEGIN {FS = "\t"} NR > 1 && $1 != "" && $2 != ""' | sort -u > hgnc_to_entrez.txt

touch HGNC_COMPLETE

