roc=$1

cat $roc | sort -k1,1g | awk 'BEGIN {FS = "\t"; fpr = ""; tpr = ""; auc = 0} {if(fpr != ""){dfpr = $1 - fpr; dtpr = $2 - tpr; rectangle = tpr * dfpr; triangle = dfpr * dtpr * 0.5; auc += rectangle + triangle} fpr = $1; tpr = $2} END {print auc}'

