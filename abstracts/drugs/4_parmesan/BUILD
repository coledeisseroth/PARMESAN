
python3 ../../../src/summarize.py ../3_subject_object_split.txt | sort -u > summaries.txt

#Run the pubtator scripts
cd pubtator
bash BUILD
cd ..

cat pubtator/summaries_pubtator_entrez.txt | awk '$(NF-1) != $NF' | sort -u > summaries_with_entrez.txt

python3 ../../../src/find_substring_genes.py summaries_with_entrez.txt | sort -u > substring_gene_summaries.txt

cat summaries_with_entrez.txt | sort -u | comm -23 - substring_gene_summaries.txt | awk 'BEGIN {FS = "\t"} $8 != "" && $9 != ""' > tmp; mv tmp summaries_with_entrez.txt

cd directionality
bash BUILD
cd ../no_dgidb
bash BUILD
cd ../timecapsule
bash BUILD
cd ..


