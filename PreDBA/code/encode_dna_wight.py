#!/usr/bin/python
# -*- coding: utf-8 -*-


import os

def encode_dnaweight_by_fasta(fasta, AAfea_phy, outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fr_fasta = open(fasta,'r')
    fo_fea = open(AAfea_phy, 'r')
    fr_fea = fo_fea.readlines()
    chainname = []
    for eachline in fr_fasta:
        if '>' in eachline:
            onechain = eachline.strip()
            for i in range(len(onechain)):
                if onechain[i]== ':' or '/' or " \ "or '?' or '"' or '<' or '>' or '|':
                    outname = onechain[1:i-1]+onechain[i:len(onechain)] + '.data'

            fw_feat = open(outdir + '/' + outname, 'w')
            continue
        seq = eachline.strip()
        for i in range(len(seq)):
            content = []
            RNA_code = seq[i]
            for onelinefea in fr_fea:
                linefea = onelinefea.split('\t')
                if RNA_code == linefea[1].strip():
                    content.append(linefea[2].strip() + '\t') #4.Mmass

                    break
            fw_feat.write(''.join(content)+ '\n')
        fw_feat.close()
    fr_fasta.close()
'''
if __name__=="__main__":
    params1 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/test_dna_seq_new.fasta'
    params2 = '/ifs/gdata1/yangwenyi/DATA/_Global_data/DNAfeaDouble_phy.txt'
    params3 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_DNA_weight'
    #encode_phy(params1, params2, params3)
    encode_phy_by_fasta(params1, params2, params3)
'''