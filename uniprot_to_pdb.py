import csv

# read from file
Infile = open('clusteredGeneIDToPDBMapping.txt', 'r')
reader = Infile.readlines()
uniprot_dict = {}
# converts uniprot csv file into dictionary
for row in reader:
        if row[9] == "	":
            rowSplit = row[10:].split(",")
        else:
            rowSplit = row[9:].split(",")
        for pdb in rowSplit:
            # if the uniprot id is not in the dict
            if row[:6] not in uniprot_dict:
                # uniprot id as key and pdb id + chain as value
                uniprot_dict[row[:6]] = [pdb[:4] + pdb[5]]
            else:
                # if the uniprot id is already present in the dict but pdb id is not
                if not any(pdb[:4] in entry for entry in uniprot_dict[row[:6]]):
                    # uniprot id as key and pdb id + chain as value
                    # appends the value list with pdb id + chain
                    uniprot_dict[row[:6]].append(pdb[:4] + pdb[5])


# function for getting PDB IDs + chain
def getPDB(uniprot_id):
    # defines an empty list for result
    PDBs = []
    if uniprot_id == "?":
        return "The UniProt entry was not found"
    else:
        PDBs = uniprot_dict[uniprot_id]
        return PDBs


# uniprots without pdb id
notfound = []
uniprot_pdb_dict = {}

with open('interactions_pdb.txt', 'wt', newline='') as out_file:
    tsv_writer = csv.writer(out_file, delimiter=' ')
    file = open('interactions_uniprot.txt', 'r')
    next(file)
    for line in file:
        # stores uniprot ids in a row
        uniprots = line.rstrip('\n').split(' ')
        # get pdbs for the first uniprot id
        try:
            pdbList1 = getPDB(uniprots[0])
            uniprot_pdb_dict[uniprots[0]] = getPDB(uniprots[0])
        except KeyError:
            if not notfound.__contains__(uniprots[0]):
                notfound.append(uniprots[0])
        # get pdbs for the second uniprot id
        try:
            pdbList2 = getPDB(uniprots[1])
            uniprot_pdb_dict[uniprots[1]] = getPDB(uniprots[1])
            # writes the pdb pairs to pdb_list.txt
            for pdb1 in pdbList1:
                for pdb2 in pdbList2:
                    tsv_writer.writerow([pdb1,
                                         pdb2])
        except KeyError:
            if not notfound.__contains__(uniprots[1]):
                notfound.append(uniprots[1])



