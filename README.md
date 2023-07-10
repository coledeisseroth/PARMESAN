To generate all of the data, cd into PARMESAN and run:
bash setup.sh

All genes are indexed by Entrez ID, and all drugs are indexed by PubChem ID.

Upon completion, gene modifier extractions will be here:
pmc/gene/4_parmesan/directionality_abstracts/consensus_directionality.txt
The format is:
Modifier	Target	Directionality score

The accuracy values for extractions at each directionality score threshold will be here:
pmc/gene/4_parmesan/directionality_abstracts/accuracy_test/reactome_scoretable.txt
The format is:
Score threshold	Accuracy	No. correct extractions in the ground-truth comparison	No. incorrect extractions in the ground-truth comparison

Gene modifier predictions will be here:
pmc/gene/6_hypotheses_with_pubmed/hypotheses/pergene/
For each target gene, there will be a file whose name is the entrez ID of that gene. For example, the predicted modifiers of MeCP2 will be in the file titled "4204".
The format for each table is:
Modifier        Target  Directionality score

The accuracy values for predictions at each directionality score threshold will be here:
pmc/gene/6_hypotheses_with_pubmed/hypotheses/reactome_scoretable.txt
The format is:
Score threshold Accuracy        No. correct predictions in the ground-truth comparison  No. incorrect predictions in the ground-truth comparison


Drug modifier extractions will be here:
pmc/gene/4_parmesan/directionality_abstracts/consensus_directionality.txt
The format is:
Modifier        Target  Directionality score

The accuracy values for extractions at each directionality score threshold will be here:
pmc/drug/4_parmesan/directionality_abstracts/accuracy_test/dgidb_scoretable.txt
The format is:
Score threshold Accuracy        No. correct extractions in the ground-truth comparison  No. incorrect extractions in the ground-truth comparison


Drug modifier predictions will be here:
pmc/drug/6_hypotheses_with_pubmed/no_dgidb/pergene/
For each target gene, there will be a file whose name is the entrez ID of that gene. For example, the predicted modifiers of MeCP2 will be in the file titled "4204".
The format for each table is:
Modifier        Target  Directionality score

The accuracy values for predictions at each directionality score threshold will be here:
pmc/gene/6_hypotheses_with_pubmed/no_dgidb/dgidb_scoretable.txt
The format is:
Score threshold Accuracy        No. correct predictions in the ground-truth comparison  No. incorrect predictions in the ground-truth comparison


Copyright 2023, Baylor College of Medicine. All rights reserved.
