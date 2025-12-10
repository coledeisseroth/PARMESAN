mkdir articles
cd articles
for url in $(curl https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_noncomm/txt/| grep tar.gz | cut -d'"' -f2 | awk '{print "https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_noncomm/txt/" $0}'); do  wget $url; sleep 1; done
for url in $(curl https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/txt/| grep tar.gz | cut -d'"' -f2 | awk '{print "https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/txt/" $0}'); do  wget $url; sleep 1; done
for url in $(curl https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_other/txt/| grep tar.gz | cut -d'"' -f2 | awk '{print "https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_other/txt/" $0}'); do  wget $url; sleep 1; done
cd ..

mkdir unzipped
cd unzipped
for prefix in $(ls ../articles/ | cut -d_ -f1-2 | sort -u); do
mkdir $prefix
cd $prefix
for zipfile in $(ls ../../articles/${prefix}*.tar.gz); do
tar -xvzf $zipfile
done
cd ..
done
cd ..

mkdir id_map
cd id_map
for url in $(curl https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_noncomm/txt/| grep filelist.txt | cut -d'"' -f2 | awk '{print "https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_noncomm/txt/" $0}'); do  wget $url; sleep 1; done
for url in $(curl https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/txt/| grep filelist.txt | cut -d'"' -f2 | awk '{print "https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/txt/" $0}'); do  wget $url; sleep 1; done
for url in $(curl https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_other/txt/| grep filelist.txt | cut -d'"' -f2 | awk '{print "https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_other/txt/" $0}'); do  wget $url; sleep 1; done
cd ..

cat id_map/* | cut -f3,5 | awk 'NR > 1' | sort -u > pmc_to_pmid.txt

while [ $(screen -ls | grep 'PMC_UNZIP' | wc -l) -gt 0 ]; do   sleep 1; done

touch PMC_COMPLETE
