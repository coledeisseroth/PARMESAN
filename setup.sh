###This is the master BUILD script that assembles everything

mydir=$(realpath $0 | rev | cut -d'/' -f2- | rev)
cd $mydir/

##Compile mapping data
cd mappings
screen -m -d -S "MAPPINGS" bash -c "bash BUILD"
cd ..

##Compile ground-truth data
cd ground_truth
screen -m -d -S "GROUND_TRUTH" bash -c "bash BUILD"
cd ..

#Compile the analysis of non-text-mining data
cd no_text_mining
screen -m -d -S "NO_TEXT_MINING" bash -c "bash BUILD"
cd ..

#Build the PARMESAN database
cd abstracts/
bash BUILD
cd ..

cd pmc
bash BUILD
cd ..

