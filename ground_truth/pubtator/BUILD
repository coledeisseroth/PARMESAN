cd genes
screen -m -d -S "PUBTATOR_GENES" bash -c "bash BUILD"
cd ../chemicals
screen -m -d -S "PUBTATOR_CHEMICALS" bash -c "bash BUILD"
cd ..

while [ $(screen -ls | grep 'PUBTATOR_GENES' | wc -l) -gt 0 ]; do   sleep 10; done
while [ $(screen -ls | grep 'PUBTATOR_CHEMICALS' | wc -l) -gt 0 ]; do   sleep 10; done

join -a 1 -a 2 -o auto -t$'\t' <(sort -k1,1 genes/pubtator_genes_oneperline.txt) <(sort -k1,1 chemicals/pubtator_chemicals_oneperline.txt) | sort -k1,1 > genes_and_chemicals.txt

touch PUBTATOR_COMPLETE

