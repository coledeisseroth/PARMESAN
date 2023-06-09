for file in $(ls ../baseline/*); do   zcat $file | paste -sd' ' | sed 's/<PubmedArticle>/\n/g' | awk 'NR > 1' | sed 's/<PMID Version="1">/\t/g' | sed 's/<\/PMID>/\t/g' | sed 's/<PubDate>/\t/g' | cut -f2,4- | sed 's/<Year>\|<\/Year>\|<Month>\|<\/Month>\|<Day>\|<\/Day>/\t/g' | cut -f1,3,5,7 | sort -u; done > pmid_to_date.txt


