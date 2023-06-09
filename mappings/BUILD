for datadir in diopt entrez hgnc mesh pubchem uniprot; do
cd $datadir
bash BUILD &
cd ..
done

while [ $(ls diopt/ | grep DIOPT_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
while [ $(ls entrez/ | grep ENTREZ_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
while [ $(ls hgnc/ | grep HGNC_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
while [ $(ls mesh/ | grep MESH_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
while [ $(ls pubchem/ | grep PUBCHEM_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done
while [ $(ls uniprot/ | grep UNIPROT_COMPLETE | wc -l) -lt 1 ]; do sleep 1; done


