for file in $(ls ../../../ground_truth/pubmed/baseline); do zcat ../../../ground_truth/pubmed/baseline/$file | grep -i '<CollectiveName>Undiagnosed Diseases Network</CollectiveName>\|</PMID>\|<PubmedArticle>' | grep -v '          <PMID Version' | paste -s | sed 's/<PubmedArticle>/\n/g' | grep '<CollectiveName>Undiagnosed Diseases Network</CollectiveName>' | cut -d'>' -f2- | cut -d'<' -f1; done | sort -u > udn_pmids.txt

for file in $(ls ../1_annotated_articles/); do cat ../1_annotated_articles/$file | grep -wf udn_pmids.txt | sort -k1,1 | join -t$'\t' - <(cat udn_pmids.txt | sort -u); done | sort -u > udn_annotated_articles.txt

cat udn_annotated_articles.txt | cut -f1,2,4 | sed 's/|/\t/g' | awk 'BEGIN {FS = "\t"} {article = $2 ". " $3; for(i = 4; i <= NF; i += 1){if(index(article, $i) > 0){print $1 "\t" $i}}}' | awk '$2 != ""' > udn_genes_mentioned.txt

for pair in $(cat udn_genes_mentioned.txt | awk 'BEGIN {FS = "\t"} length($2) > 1' | sed 's/\t/|/g' | sed 's/ /_/g'); do pmid=$(echo $pair | cut -d'|' -f1); gene=$(echo $pair | cut -d'|' -f2 | sed 's/_/ /g'); superstrings=$(cat udn_genes_mentioned.txt | awk 'BEGIN {FS = "\t"} $1 == '$pmid | grep -f <(echo $gene) | wc -l); fullmention=$(cat udn_annotated_articles.txt | awk '$1 == '$pmid | cut -f2 | grep -wf <(echo $gene) | wc -l); echo $pmid$'\t'$gene$'\t'$superstrings$'\t'$fullmention; done | awk 'BEGIN {FS = "\t"} $3 == 1 && $4 > 0' > filtered_udn_gene_mentions.txt

cat filtered_udn_gene_mentions.txt | cut -f1,2 | tr '[:lower:]' '[:upper:]' | sed 's/ //g' | sed 's/-//g' | sort -u | sort -t$'\t' -k2,2 | join -t$'\t' -1 2 -2 2 - <(cat ../4_parmesan/symbol_mapping/entrez_to_symbol_nodashes.txt | sort -t$'\t' -k2,2) | awk 'BEGIN {FS = "\t"} {print $2 "\t" $3 "\t" $1}' > udn_entrez_mentioned.txt

#for pair in $(cat udn_genes_mentioned.txt | awk 'BEGIN {FS = "\t"} length($2) > 1' | sed 's/\t/|/g' | sed 's/ /_/g'); do pmid=$(echo $pair | cut -d'|' -f1); gene=$(echo $pair | cut -d'|' -f2 | sed 's/_/ /g'); superstrings=$(cat udn_genes_mentioned.txt | grep -f <(echo $gene) | wc -l); fullmention=$(cat udn_annotated_articles.txt | awk '$1 == '$pmid | cut -f2 | grep -f <(echo $gene) | wc -l); echo $pmid$'\t'$gene$'\t'$superstrings$'\t'$fullmention; done | sort -k1,1 -k2,2

