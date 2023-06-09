for datadir in dgidb pmc pubmed pubtator reactome; do
cd $datadir
bash BUILD &
cd ..
done

while [ $(ls dgidb/ | grep DGIDB_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
while [ $(ls pmc/ | grep PMC_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
while [ $(ls pubmed/ | grep PUBMED_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
while [ $(ls pubtator/ | grep PUBTATOR_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
while [ $(ls reactome/ | grep REACTOME_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done


