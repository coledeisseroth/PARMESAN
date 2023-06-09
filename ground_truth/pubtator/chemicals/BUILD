wget https://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/chemical2pubtatorcentral.gz
zcat chemical2pubtatorcentral.gz | cut -f1,4 | awk '$2 != ""' | sort -u | sort -k1,1 > pubtator_chemicals.txt
python3 ../../../src/pubtator_gene_map.py pubtator_chemicals.txt | sort -u > pmid_to_chemicals.txt
python3 ../../../src/pubtator_gene_map.py pubtator_chemicals.txt -l > pubtator_chemicals_oneperline.txt

touch PUBTATOR_CHEMICALS_COMPLETE
