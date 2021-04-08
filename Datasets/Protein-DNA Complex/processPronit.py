import csv

dnaSequences = []
proteinSequences = []
with open('pronit.csv', newline='') as csvfile:
    pronit = csv.DictReader(csvfile)
    for row in pronit:
        proteinSequences.append(row['sequence'])
        dnaSequences.append(row['sequence_wild1'])
dnaSequences = dnaSequences[::-1]
with open('DNADataset.csv', 'w', newline='') as csvfile:
    fieldnames = ['sequence']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for dna in dnaSequences:
        if(dna!=""):
            writer.writerow({'sequence':dna})

with open('ProteinDataset.csv', 'w', newline='') as csvfile:
    fieldnames = ['sequence']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for protein in proteinSequences:
        if(protein!=""):
            writer.writerow({'sequence':protein})
