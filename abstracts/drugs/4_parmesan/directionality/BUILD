cat ../pubtator/summaries_pubtator_pubchem_entrez.txt | grep -v $'\t\t' | awk '$(NF-1) != $NF' | sort -u > summaries_with_entrez.txt
python3 ../../../../src/find_substring_genes.py summaries_with_entrez.txt | sort -u > substring_gene_summaries.txt
cat summaries_with_entrez.txt | sort -u | comm -23 - substring_gene_summaries.txt | awk 'BEGIN {FS = "\t"} $8 != "" && $9 != ""' > tmp; mv tmp summaries_with_entrez.txt


cat summaries_with_entrez.txt | cut -f1,3,6,8,9 | sort -t$'\t' -k2,2 | join -t$'\t' -1 2 -2 1 - <(cat ../../../../src/vocabulary.py | grep 'positive\|negative' | grep predicate | cut -d'"' -f2,6 | sed 's/"/\t/g' | sed 's/positive/1/g' | sed 's/negative/-1/g' | sort -k1,1) | cut -f2- | sort -k2,2 | join -t$'\t' -1 2 -2 1 - <(cat ../../../../src/vocabulary.py | grep '"action"' | grep 'negative' | cut -d'"' -f2 | sort -u | awk 'BEGIN{print ".\t1"} {print $1 "\t-1"}' | sort -k1,1) | cut -f2- | awk '{print $1 "\t" $2 "\t" $3 "\t" $4 * $5}' | sort -u > pmid_mod_targentrez_direction.txt


cat pmid_mod_targentrez_direction.txt | sort -k3,3 | join -t$'\t' -1 3 -2 4 -a 1 -o auto -e "." - <(cat ../../../../mappings/diopt/diopt_orthologs.txt | cut -f-4 | grep -v "#" | awk '$2 / $3 > 0.5' | sort -k4,4) | awk 'BEGIN {FS = "\t"} {print $2 "\t" $0}' | cut -f1,2,4- | sort -u > ortholog_mapping.txt

cat ortholog_mapping.txt | awk 'BEGIN {FS = "\t"} {mcoef = 1; mod = $3; if($5 == "."){tcoef = 1; targ = $2} else{tcoef = $6 / $7; targ = $5} score = mcoef * tcoef * $4; print score / sqrt(score ^ 2) "\t" sqrt(score ^ 2) "\t" $1 "\t" mod "\t" targ "\t" mcoef * tcoef * $4}' | sort -k2,2gr | sort -k1,1 -k3,3 -k4,4 -k5,5 -u | cut -f3- > directionality.txt

cat directionality.txt | sort -t$'\t' -k3,3 | join -t$'\t' -1 3 -2 1 - <(cat ../../../../mappings/entrez/human_genes.txt | sort -u) | awk 'BEGIN {FS = "\t"} {print $2 "\t" $3 "\t" $1 "\t" $4}' > tmp; mv tmp directionality.txt

cat directionality.txt | cut -f2- | awk '{print $1 "_" $2 "\t" $3}' | sort -k1,1 | awk 'BEGIN {rel = ""; pos = 0; neg = 0} {if($1 != rel && rel != ""){print rel "\t" pos "\t" neg; pos = 0; neg = 0} rel = $1; if($2 > 0){pos += $2} if($2 < 0){neg -= $2}} END {print rel "\t" pos "\t" neg}' | sed 's/_/\t/g' > consensus_sums.txt

cat consensus_sums.txt | awk '$3 + $4 > 0 {print $1 "\t" $2 "\t" ($3 - $4) * sqrt(($3 - $4) ** 2) / ($3 + $4)}' | awk '$3 != 0' | awk '$1 != $2' > consensus_directionality.txt


