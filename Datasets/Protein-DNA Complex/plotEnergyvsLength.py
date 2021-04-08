import csv
import numpy as np
import math
from matplotlib import pyplot as plt
dnaSequences = []
proteinSequences = []
energies = []
with open('pronit.csv', newline='') as csvfile:
    pronit = csv.DictReader(csvfile)
    for row in pronit:
        if(row['d_g_wild']!='' and ('>' not in row['d_g_wild']) and ('<' not in row['d_g_wild'])):
            proteinSequences.append(len(row['sequence']))
            dnaSequences.append(len(row['sequence_wild1']))
            e = row['d_g_wild'].split(' ')[0].split('e')
            d = float(e[0])*math.pow(10, int(e[1]))
            energies.append(d)


plt.title("Binding Affinity Versus Protein Length")
plt.xlabel("Protein Length (# of Amino Acids)")
plt.ylabel("Binding Affinity (kcal/mol)")
plt.plot(proteinSequences, energies, "ob")
plt.show()

