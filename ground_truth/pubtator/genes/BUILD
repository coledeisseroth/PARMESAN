wget https://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/gene2pubtatorcentral.gz
zcat gene2pubtatorcentral.gz | cut -f1,4 | awk '$2 != ""' | sort -u > pubtator_genes.txt
python3 ../../../src/pubtator_gene_map.py pubtator_genes.txt | sort -u > pmid_to_genes.txt
python3 ../../../src/pubtator_gene_map.py pubtator_genes.txt -l > pubtator_genes_oneperline.txt
touch PUBTATOR_GENES_COMPLETE

