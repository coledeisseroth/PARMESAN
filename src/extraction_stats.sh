echo -n 'Positive modifiers: '; cat consensus_directionality.txt | awk 'BEGIN {FS = "\t"} $3 > 0' | cut -f1 | sort -u | wc -l
echo -n 'Positive targets: '; cat consensus_directionality.txt | awk 'BEGIN {FS = "\t"} $3 > 0' | cut -f2 | sort -u | wc -l
echo -n 'Positive relationships: '; cat consensus_directionality.txt | awk 'BEGIN {FS = "\t"} $3 > 0' | cut -f1,2 | sort -u | wc -l
echo -n 'Positive articles: '; cat consensus_directionality.txt | awk 'BEGIN {FS = "\t"} $3 > 0' | cut -f1,2 | sed 's/\t/_/g' | sort -u | join -t$'\t' - <(cat directionality.txt | awk 'BEGIN {FS = "\t"} {print $2 "_" $3 "\t" $1}' | sort -k1,1) | cut -f2 | sort -u | wc -l
echo -n 'Negative modifiers: '; cat consensus_directionality.txt | awk 'BEGIN {FS = "\t"} $3 < 0' | cut -f1 | sort -u | wc -l
echo -n 'Negative targets: '; cat consensus_directionality.txt | awk 'BEGIN {FS = "\t"} $3 < 0' | cut -f2 | sort -u | wc -l
echo -n 'Negative relationships: '; cat consensus_directionality.txt | awk 'BEGIN {FS = "\t"} $3 < 0' | cut -f1,2 | sort -u | wc -l
echo -n 'Negative articles: '; cat consensus_directionality.txt | awk 'BEGIN {FS = "\t"} $3 < 0' | cut -f1,2 | sed 's/\t/_/g' | sort -u | join -t$'\t' - <(cat directionality.txt | awk 'BEGIN {FS = "\t"} {print $2 "_" $3 "\t" $1}' | sort -k1,1) | cut -f2 | sort -u | wc -l

