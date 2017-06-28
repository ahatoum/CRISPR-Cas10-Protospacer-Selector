import re

def comp(seq):

    inv = list()

    for gene in seq:

        if gene == 'A':
            inv.append('T')
        if gene == 'T':
            inv.append('A')
        if gene == 'G':
            inv.append('C')
        if gene == 'C':
            inv.append('G')

    return inv

def AnalyzeSpacer(mask, genome):

    blocklen = 8
    ProtoSpacerLen = 35
    N = range(len(genome)-blocklen + 1)
    poscount = 0
    Data = list()


    for i in N:

        block  = genome[i:i+blocklen]
        filter = [block[0] != mask[0],
                  block[1] != mask[1],
                  block[2] != mask[2],
                  block[3] != mask[3],
                  block[4] != mask[4],
                  block[5] != mask[5],
                  block[6] != mask[6],
                  block[7] != mask[7]]

        if (all(filter) and i >= ProtoSpacerLen):

            ProtoSpacer = genome[i-ProtoSpacerLen:i]
            Spacer = list(reversed(comp(ProtoSpacer)))

            poscount += 1
            location = i+1-ProtoSpacerLen
            Data.append([location, ProtoSpacer, block, Spacer])

    return poscount, Data