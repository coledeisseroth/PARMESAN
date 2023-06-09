zcat ../../../entrez/raw/gene_info.gz | cut -f1,2,3,5,11 | grep -wf <(cat ../diopt_orthologs.txt | awk 'NR > 1' | cut -f5 | sort -u) > ortholog_gene_aliases.txt
cat ../diopt_orthologs.txt | cut -f4 | sort -u | join -t$'\t' - <(cat ortholog_gene_aliases.txt | cut -f2- | sort -t$'\t' -k1,1) > human_mapped_gene_aliases.txt

