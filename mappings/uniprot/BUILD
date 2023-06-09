cd raw
bash BUILD
cd ..

zcat raw/HUMAN_9606_idmapping_selected.tab.gz | cut -f1,3 | awk 'NF > 1' | sort -u > uniprot_to_entrez.txt

touch UNIPROT_COMPLETE

