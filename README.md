<h1>PARsing ModifiErS via Article aNnotations (PARMESAN)</h1>

PARMESAN is an open-source computational tool that automatically extracts gene-gene and drug-gene relationships from PubMed and PubMed Central. Upon extracting these relationships, it predicts unknown regulatory relationships.

Each extracted and predicted relationship is given a numeric score based on the amount of supporting and opposing evidence. To assign meaning to these scores, we compare the relationships to manually curated relationships in the Drug-Gene Interaction Database (DGIdb) and Reactome's functional interaction list. This gives us a score table, telling us the accuracy of predictions scoring above a given threshold.

<h2>Disclaimer</h2>
PARMESAN is designed to help guide molecular experiments, but NOT medical deicision-making. PARMESAN, its extractions, and its predictions should never be used to make medical decisions.

<h1>Setup</h1>
To generate all of the relevant tables, cd into PARMESAN and run:

<code>bash setup.sh</code>

All genes are indexed by Entrez ID, and all drugs are indexed by PubChem ID. All tables listed below are tab-separated.

<h2>Gene modifiers</h2>
<h3>Extracted known relationships</h3>
Upon completion, gene modifier extractions will be here:

<code>pmc/gene/4_parmesan/directionality_abstracts/consensus_directionality.txt</code>

The format is:

Modifier[tab]Target[tab]Directionality_score

The accuracy values for extractions at each directionality score threshold will be here:

<code>pmc/gene/4_parmesan/directionality_abstracts/accuracy_test/reactome_scoretable.txt</code>

The format is:

Score threshold[tab]Accuracy[tab]No. relationships consistent with the manually curated database[tab]No. relationships contradicted by the manually curated database

<h3>Predicted relationships</h3>
Gene modifier predictions will be here:

<code>pmc/gene/6_hypotheses_with_pubmed/hypotheses/pergene/</code>

For each target gene, there will be a file whose name is the entrez ID of that gene. For example, the predicted modifiers of MeCP2 will be in the file titled "4204".
The format for each table is:

Modifier[tab]Target[tab]Directionality score

The accuracy values for predictions at each directionality score threshold will be here:

<code>pmc/gene/6_hypotheses_with_pubmed/hypotheses/reactome_scoretable.txt</code>

The format is:

Score threshold[tab]Accuracy[tab]No. relationships consistent with the manually curated database[tab]No. relationships contradicted by the manually curated database

<h2>Drug modifiers</h2>

<h3>Extracted known relationships</h3>
Drug modifier extractions will be here:

<code>pmc/gene/4_parmesan/directionality_abstracts/consensus_directionality.txt</code>

The format is:

Modifier[tab]Target[tab]Directionality score

The accuracy values for extractions at each directionality score threshold will be here:

<code>pmc/drug/4_parmesan/directionality_abstracts/accuracy_test/dgidb_scoretable.txt</code>
The format is:

Score threshold[tab]Accuracy[tab]No. relationships consistent with the manually curated database[tab]No. relationships contradicted by the manually curated database

<h3>Predicted relationships</h3>
Drug modifier predictions will be here:

<code>pmc/drug/6_hypotheses_with_pubmed/no_dgidb/pergene/</code>

For each target gene, there will be a file whose name is the entrez ID of that gene. For example, the predicted modifiers of MeCP2 will be in the file titled "4204".
The format for each table is:

Modifier[tab]Target[tab]Directionality score

The accuracy values for predictions at each directionality score threshold will be here:

<code>pmc/gene/6_hypotheses_with_pubmed/no_dgidb/dgidb_scoretable.txt</code>

The format is:

Score threshold[tab]Accuracy[tab]No. relationships consistent with the manually curated database[tab]No. relationships contradicted by the manually curated database


<h1>Citation</h1>
To cite PARMESAN, you can use the preprint below:

https://www.biorxiv.org/content/10.1101/2022.09.08.506253v1

Copyright 2023, Baylor College of Medicine. All rights reserved.
