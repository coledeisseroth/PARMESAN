experiment=$1
truth=$2

cat $experiment | awk '{print $1 "_" $2 "\t" $3}' | awk '$2 != 0' | sort -k1,1 | join -t$'\t' - <(cat $truth | awk '{print $1 "_" $2 "\t" $3}' | awk '$2 != 0' | sort -k1,1) | awk 'BEGIN {FS = "\t"; t=0; f=0; ep=0; en=0; tp=0; tn=0} {if($2 > 0){ep += 1} else{en += 1} if($3 > 0) {tp += 1} else{tn += 1} if($2 * $3 > 0){t += 1} else{f += 1}} END {p = ep / (ep + en); q = tp / (tp + tn); pcorr = t / (t + f); print 1 + ((pcorr - 1) / (p + q - (2 * p * q)))}'

