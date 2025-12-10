python3 ../../../src/summarize.py ../3_subject_object_split.txt | sort -u > summaries.txt

cat summaries.txt | sed 's/-//g' | sed 's/\t\t/\t.\t/g' | sed 's/\t\t/\t.\t/g' | awk 'BEGIN {FS = "\t"} {print toupper($2) "\t" toupper($5) "\t" $0}' | cut -f-9 | sort -t$'\t' -k1,1 | join -t$'\t' -1 1 -2 2 - <(cat ../../../abstracts/genes/4_parmesan/symbol_mapping/entrez_to_symbol_nodashes.txt | sort -t$'\t' -k2,2) | sort -t$'\t' -k2,2 | join -t$'\t' -1 2 -2 2 - <(cat ../../../abstracts/genes/4_parmesan/symbol_mapping/entrez_to_symbol_nodashes.txt | sort -t$'\t' -k2,2) | cut -f3- | awk '$NF != $(NF-1)' > summaries_mapped_entrez.txt

#Run the pubtator scripts
cd pubtator
bash BUILD
cd ..

cat summaries_mapped_entrez.txt pubtator/summaries_pubtator_entrez.txt | grep -v $'\t\t' | awk '$(NF-1) != $NF' | sort -u > summaries_with_entrez.txt

python3 ../../../src/find_substring_genes.py summaries_with_entrez.txt | sort -u > substring_gene_summaries.txt

cat summaries_with_entrez.txt | sort -u | comm -23 - substring_gene_summaries.txt | awk 'BEGIN {FS = "\t"} $8 != "" && $9 != ""' > tmp; mv tmp summaries_with_entrez.txt

cat summaries_with_entrez.txt | cut -f1 | sort -u | comm -23 - <(cat ../../../ground_truth/pubmed/retracted_pmids.txt | sort -u) | sort -u | join -t$'\t' - <(cat summaries_with_entrez.txt | sort -k1,1) > tmp; mv tmp summaries_with_entrez.txt

cd directionality
bash BUILD
cd ..
cd directionality_abstracts
bash BUILD
cd ..
cd timecapsule
bash BUILD
cd ..


