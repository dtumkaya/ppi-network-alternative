# ppi-network-alternative
Embedding Alternative Conformations of Proteins in Protein-protein interaction networks.

IdMapping.py & geneIDToPDBExtractor.py are not used since we have a mapping txt.

Follow steps: 
1. Run PdbDownloader.py with "geneIDToPDBMapping.txt" file. This will downloard the PDB data to the local.
2. Install TMAlign with commands given in Halakou's Alternative Conformations Chapter 9.
3. Run mainProgram.py to cluster the IDs and find number of alternative conformations.
4. Run PpiNetworkToPDBNetwork.py to get all pairs interacting with each other. This will give all interactions that should be submitted to Prism.
5. After submmission and getting results for every pair, run PpiNetworkPrismPredictions.py and get all the results of interaction results present in Prism for the pairs we have in our list.

