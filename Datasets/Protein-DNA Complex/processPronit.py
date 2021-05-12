import csv

dnaSequences = []
proteinSequences = []
foundPairs =set()
with open('pronit.csv', newline='') as csvfile:
    pronit = csv.DictReader(csvfile)
    processed = open("ProNIT_Final.csv", 'w', newline='')
    writer = csv.DictWriter(processed, fieldnames=['protein_sequence', 'dna_sequence', 'd_g_wild', 'entry'])
    writer.writeheader()
    for row in pronit:
        if(row['sequence']!='' and (row['sequence_mutant1']!='' or row['sequence_wild1']!='') and (row['d_g_wild']!='')):
            if(row['mutation_nucleic_acid']!='wild'):
                if((row['sequence']+row['sequence_mutant1']) not in foundPairs):
                    writer.writerow({'protein_sequence':row['sequence'],
                                        'dna_sequence':row['sequence_mutant1'],
                                         'd_g_wild':row['d_g_wild'],
                                         'entry':row['entry']})
                    foundPairs.add(row['sequence']+row['sequence_mutant1'])
                    
            else:
                if((row['sequence']+row['sequence_wild1']) not in foundPairs):
                    writer.writerow({'protein_sequence':row['sequence'],
                                     'dna_sequence':row['sequence_wild1'],
                                     'd_g_wild':row['d_g_wild'],
                                     'entry':row['entry']})
                    foundPairs.add(row['sequence']+row['sequence_wild1'])

#dnaSequences = dnaSequences[::-1]
#with open('DNADataset.csv', 'w', newline='') as csvfile:
#    fieldnames = ['sequence']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#    writer.writeheader()
#    for dna in dnaSequences:
#        if(dna!=""):
#            writer.writerow({'sequence':dna})

#with open('ProteinDataset.csv', 'w', newline='') as csvfile:
#    fieldnames = ['sequence']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#    writer.writeheader()
#    for protein in proteinSequences:
#        if(protein!=""):
#            writer.writerow({'sequence':protein})
