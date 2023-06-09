cd raw
bash BUILD
cd ..

cat raw/FIsInGene_122921_with_annotations.txt | cut -f1,2,4 | awk 'NR > 1' | awk 'BEGIN {FS = "\t"} {back=substr($3, 0, 1); forward=substr($3, length($3)); if(back == "<"){print $2 "\t" $1 "\t1"} if(back == "|") {print $2 "\t" $1 "\t-1"} if(forward == ">"){print $1 "\t" $2 "\t1"} if(forward == "|"){print $1 "\t" $2 "\t-1"}}' > reactome_annotations.txt

touch REACTOME_COMPLETE

