cat ../consensus_directionality.txt | awk 'BEGIN {FS = "\t"} {print $1 "_" $2 "\t" $3}' | sort -k1,1 | join -t$'\t' - <(cat ../../../../../no_text_mining/reactome_entrez.txt | awk 'BEGIN {FS = "\t"} {print $1 "_" $2 "\t" $3}' | sort -k1,1) | sed 's/_/\t/g' > reactome_comparison.txt

for i in 0 $(seq 100); do cat reactome_comparison.txt | awk 'BEGIN {FS = "\t"; p = 0; n = 0} sqrt($3 ^ 2) > '$i' {if($3 * $4 > 0) {p += 1} else if($3 * $4 < 0) {n += 1}} END {print '$i' "\t" p / (p + n) "\t" p "\t" n}'; done > reactome_scoretable.txt

for i in 0 $(seq 100); do cat ../consensus_directionality.txt | awk 'BEGIN {FS = "\t"} sqrt($3 ^ 2) > '$i | wc -l | awk '{print "'$i'\t" $1}'; done > score_to_count.txt

#cat ../ortholog_mapping.txt | awk 'BEGIN {FS = "\t"} {if($5 == ".") {cmod = $1} else {cmod = $5} if($8 == "."){ctart = $2} else{ctarg = $8} print cmod "_" ctarg "\t" $1 "_" $2 "\t" $0}' | sort -k2,2 | join -t$'\t' -1 2 -2 1 - <()

get_seeded_random()
{
  seed="$1"
  openssl enc -aes-256-ctr -pass pass:"$seed" -nosalt \
    </dev/zero 2>/dev/null
}


shuf --random-source=<(get_seeded_random 2023) <(cat ../consensus_directionality.txt | awk '{print $1 "_" $2}' | sort -u) | head -100 | sort -u > random_relationships.txt
python3 ../../../../../src/powered_threshold.py reactome_scoretable.txt > power_samplesize.txt
minscore=$(cat power_samplesize.txt | awk '$2 < 100' | cut -f1 | head -1); shuf --random-source=<(get_seeded_random 2023) <(cat ../consensus_directionality.txt | awk 'sqrt($3 ^ 2) > '$minscore | awk '{print $1 "_" $2}' | sort -u) | head -100 | sort -u > highscoring_relationships.txt

for prefix in random highscoring; do
cat ../ortholog_mapping.txt | awk 'BEGIN {FS = "\t"} $3 != 0 {if($5 == ".") {cmod = $1} else {cmod = $5} if($8 == "."){ctarg = $2} else{ctarg = $8} print cmod "_" ctarg "\t" $3 "_" $1 "_" $2 "\t" $0}' | grep -wf ${prefix}_relationships.txt | sort -k1,1 | join -t$'\t' - <(cat ${prefix}_relationships.txt | sort -u) | sort -t$'\t' -k2,2 | join -t$'\t' -1 2 -2 1 - <(cat ../../summaries_with_entrez.txt ../../../../../abstracts/genes/4_parmesan/summaries_with_entrez.txt | awk 'BEGIN {FS = "\t"} {print $1 "_" $8 "_" $9 "\t" $0}' | sort -t$'\t' -k1,1) | cut -f2,6,8,9,11-15,17-18,20- | sed 's/_/\t/g' | sort -u > ${prefix}_relation_justification.txt
for file in $(ls ../../../../../abstracts/genes/1_annotated_articles/); do cat ../../../../../abstracts/genes/1_annotated_articles/$file | cut -f-3 | grep -wf <(cat ${prefix}_relation_justification.txt | cut -f8 | sort -u) | sort -k1,1 | join -t$'\t' - <(cat ${prefix}_relation_justification.txt | cut -f8 | sort -u); done > ${prefix}_source_abstracts.txt
for pmcid in $(cat ${prefix}_relation_justification.txt | cut -f8 | sort -u | join -t$'\t' -1 1 -2 2 - <(cat ../../../../../ground_truth/pmc/pmc_to_pmid.txt | sort -k2,2) | cut -f2 | sort -u); do for dir in $(ls ../../../0_pmc/); do cat ../../../0_pmc/$dir/$pmcid.txt 2> /dev/null; done; done > ${prefix}_source_fulltexts.txt
for item in $(cat ${prefix}_relation_justification.txt | cut -f1,2,8-12 | sed 's/ /_/g' | sed 's/\t/|/g' | sort -u); do modentrez=$(echo $item | cut -d'|' -f1); targentrez=$(echo $item | cut -d'|' -f2); pmid=$(echo $item | cut -d'|' -f3); mod=$(echo $item | cut -d'|' -f4 | sed 's/_/ /g' | sed 's/-//g'); targ=$(echo $item | cut -d'|' -f6 | sed 's/_/ /g' | sed 's/-//g'); pred=$(echo $item | cut -d'|' -f5); action=$(echo $item | cut -d'|' -f7); cat ${prefix}_source_abstracts.txt ${prefix}_source_fulltexts.txt | awk '$1 == '$pmid | cut -f2- | sed 's/\t/\n/g' | sed 's/\. /.\n/g' | sed 's/-//g' | grep -f <(echo $mod) | grep -f <(echo $targ) | grep -if <(echo $pred) | grep -if <(echo $action) | paste -sd' ' | awk '{print "'$modentrez'\t'$targentrez'\t'$pmid'\t" $0}'; done | sort -k1,1 -k2,2 -k3,3 | awk 'BEGIN {FS = "\t"; cur = ""; text = ""} {if(cur != "" && cur != $1 "\t" $2 "\t" $3){print cur "\t" text; text=""} cur = $1 "\t" $2 "\t" $3; text = text " " $4} END {print cur "\t" text}' > ${prefix}_source_sentences.txt
cat ${prefix}_relation_justification.txt | awk '{print $1 "_" $2 "\t" $0}' | sort -k1,1 | join -t$'\t' <(cat ../consensus_directionality.txt | awk '{print $1 "_" $2 "\t" $3}' | sort -k1,1) - | awk 'BEGIN {FS = "\t"} {print $3 "\t" $4 "\t" $2 "\t" $10 "\t" $15 "\t" $6 "\t" $7 "\t" $16 "\t" $8 "\t" $9 "\t" $14 " " $11 " " $12 " " $13}' | sed 's/\t\. /\t/g' | awk 'BEGIN {FS = "\t"} {print $4 "_" $1 "_" $2 "\t" $0}' | sort -k1,1 | join -t$'\t' - <(cat ${prefix}_source_sentences.txt | awk 'BEGIN {FS = "\t"} {print $3 "_" $1 "_" $2 "\t" $4}' | sort -k1,1) | cut -f2- | sort -u | sort -t$'\t' -k1,1 -k2,2 -k4,4 > ${prefix}_accuracy_evaluation_table.txt
done

#cat ../ortholog_mapping.txt | awk 'BEGIN {FS = "\t"} $3 != 0 {if($5 == ".") {cmod = $1} else {cmod = $5} if($8 == "."){ctarg = $2} else{ctarg = $8} print cmod "_" ctarg "\t" $3 "_" $1 "_" $2 "\t" $0}' | grep -wf highscoring_relationships.txt | sort -k1,1 | join -t$'\t' - <(cat highscoring_relationships.txt | sort -u) | sort -t$'\t' -k2,2 | join -t$'\t' -1 2 -2 1 - <(cat ../../summaries_with_entrez.txt ../../../../../abstracts/genes/4_parmesan/summaries_with_entrez.txt | awk 'BEGIN {FS = "\t"} {print $1 "_" $8 "_" $9 "\t" $0}' | sort -t$'\t' -k1,1) | cut -f2,6,8,9,11-15,17-18,20- | sed 's/_/\t/g' | sort -u > highscoring_relation_justification.txt
#for file in $(ls ../../../../../abstracts/genes/1_annotated_articles/); do cat ../../../../../abstracts/genes/1_annotated_articles/$file | cut -f-3 | grep -wf <(cat highscoring_relation_justification.txt | cut -f8 | sort -u) | sort -k1,1 | join -t$'\t' - <(cat highscoring_relation_justification.txt | cut -f8 | sort -u); done > highscoring_source_abstracts.txt
#cat highscoring_relation_justification.txt | awk '{print $1 "_" $2 "\t" $0}' | sort -k1,1 | join -t$'\t' <(cat ../consensus_directionality.txt | awk '{print $1 "_" $2 "\t" $3}' | sort -k1,1) - | awk 'BEGIN {FS = "\t"} {print $3 "\t" $4 "\t" $2 "\t" $10 "\t" $15 "\t" $6 "\t" $7 "\t" $16 "\t" $8 "\t" $9 "\t" $14 " " $11 " " $12 " " $13}' | sed 's/\t. /\t/g' > highscoring_accuracy_evaluation_table.txt


