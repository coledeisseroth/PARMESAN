curl ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline/ | rev | cut -d' ' -f1 | rev | grep -v md5 | grep gz > baseline.txt
curl ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/ | rev | cut -d' ' -f1 | rev | grep -v md5 | grep gz > update.txt

mkdir baseline
for file in $(cat baseline.txt); do  curl ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline/$file > baseline/$file; sleep 1; done
for file in $(cat update.txt); do  curl ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/$file > baseline/$file; sleep 1; done

cd dates
bash BUILD
cd ..

touch PUBMED_COMPLETE

