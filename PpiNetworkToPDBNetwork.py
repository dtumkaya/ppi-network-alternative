import time


t1 = time.time()

#geneIdNetworkFile = open('PPI_Network.txt', 'r')
PdbNetworkFile = open('PDB_Network.txt', 'w')
alternativeConformationsFile = open('clusteredGeneIDToPDBMapping.txt', 'r')
alternativeConformations = alternativeConformationsFile.readlines()
alternativeConformationsFile.close()

alternativeConfs = []

for geneId in alternativeConformations:
        alternativeConf = []
        splittedGeneId = geneId.split('\t')
        if len(splittedGeneId) > 2:
                alternativeConfs = splittedGeneId[2].split(',')
                for i in range(0, int(splittedGeneId[1])):
                        alternativeConf.append(alternativeConfs[i][:4] + alternativeConfs[i][5:6])
                print(alternativeConf)

                for i in range(len(alternativeConf)):
                        for j in range(len(alternativeConf)):
                                if (alternativeConf[i] == alternativeConf[j]):
                                        break
                                else:
                                        print(alternativeConf[i] + ' ' + alternativeConf[j])
                                        PdbNetworkFile.write(alternativeConf[i] + ' ' + alternativeConf[j] + "\n")


PdbNetworkFile.close()
t2 = time.time()
print('Elapsed time = %f' %(t2-t1))
