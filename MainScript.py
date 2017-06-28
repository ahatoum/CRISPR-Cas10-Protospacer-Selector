
import GNfunctions

tag = ['A', 'C', 'G', 'A', 'G', 'A', 'A', 'C'] # Corresponding (Reverse Complemented) Mask = ['G', 'T', 'T', 'C', 'T', 'C', 'G', 'T']
mask = [gene for gene in reversed(GNfunctions.comp(tag))]
print mask

gene = "ATGGCAGAAGAAGAAAAAATTATTAAAGAAGAACCAACGAATGAAGAAACAGAACAACCAGAAAAAATTGAAAGTGCAGAAGATGTTGTAACTGAACCTGAAAAAGAAGTTACAGAAGAAAAATCAGAAGCTTTTGTACAATTAGAACAACGTATATCTTCTTTAGAACAAAGATTAAATAACTTAGAATCACAACCACAACCAACGCAAGAATCAAGCGACCCAAATTTTGAAGATAAAACAGTACCAACTGAAGTTGATGACAATCAAGAAACAGACGGTATTGAATCAAGTGAAGAAATTAAACAAATGTTAAATTTATAA"
poscount, Data = GNfunctions.AnalyzeSpacer(mask, gene)

#poscount above is a number that represents the number of possible targets in the gene

# WRITE FILE

file = open("Results.txt", "w")
file.write('Length of Sequence: ' + str(len(gene))+'\n\n')
file.write('Possible Protospacers: ' + str(poscount)+'\n\n')
file.write('Tag Input: ' + ''.join(tag) + '\n\n')
file.write('Sequence Input: ' + ''.join(gene) + '\n\n\n')

for d in Data:

    stLocation = str(d[0])
    stProtoSpacer = ''.join(d[1])
    stAntitag = ''.join(d[2])
    stSpacer = ''.join(d[3])
    mystring = stLocation + '\t ' + stProtoSpacer + ' ' + stAntitag + ' ' + stSpacer + '\n'
    file.write(mystring)

file.close()
