#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
#AAorTT,ATorTA,TAorAT,CAorGT,GTorCA,CTorGA,
def encode_AA_by_fasta(fasta,outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fr_fasta = open(fasta,'r')
    for eachline in fr_fasta:
        if '>' in eachline:
            onechain = eachline.strip()
            for i in range(len(onechain)):
                if onechain[i]== ':' or '/' or " \ "or '?' or '"' or '<' or '>' or '|':
                    outname = onechain[1:i-1]+onechain[i:len(onechain)] + '.data'

            fw_feat = open(outdir + '/' + outname, 'w')
            continue
        seq = eachline.strip()
        number = 0
        for i in range(len(seq)-1):

            if (seq[i] == 'A' and seq[i+1]=='A') or (seq[i] == 'T' and seq[i+1]=='T'):
                number=number+1
        #print(number)

        fw_feat.write(str(number)+ '\n')
        fw_feat.close()
    fr_fasta.close()
def encode_AT_by_fasta(fasta,outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fr_fasta = open(fasta,'r')
    for eachline in fr_fasta:
        if '>' in eachline:
            onechain = eachline.strip()
            for i in range(len(onechain)):
                if onechain[i]== ':' or '/' or " \ "or '?' or '"' or '<' or '>' or '|':
                    outname = onechain[1:i-1]+onechain[i:len(onechain)] + '.data'

            fw_feat = open(outdir + '/' + outname, 'w')
            continue

        seq = eachline.strip()
        number = 0
        for i in range(len(seq)-1):
            if (seq[i] == 'A' and seq[i+1]=='T'):
                number=number+1
        #print(number)
        fw_feat.write(str(number)+ '\n')
        fw_feat.close()
    fr_fasta.close()
def encode_TA_by_fasta(fasta,outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fr_fasta = open(fasta,'r')
    for eachline in fr_fasta:
        if '>' in eachline:
            onechain = eachline.strip()
            for i in range(len(onechain)):
                if onechain[i]== ':' or '/' or " \ "or '?' or '"' or '<' or '>' or '|':
                    outname = onechain[1:i-1]+onechain[i:len(onechain)] + '.data'

            fw_feat = open(outdir + '/' + outname, 'w')
            continue
        seq = eachline.strip()
        number = 0
        for i in range(len(seq)-1):
            if (seq[i] == 'T' and seq[i+1]=='A'):
                number=number+1
        #print(number)
        fw_feat.write(str(number)+ '\n')
        fw_feat.close()
    fr_fasta.close()
def encode_CA_by_fasta(fasta,outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fr_fasta = open(fasta,'r')
    for eachline in fr_fasta:
        if '>' in eachline:
            onechain = eachline.strip()
            for i in range(len(onechain)):
                if onechain[i]== ':' or '/' or " \ "or '?' or '"' or '<' or '>' or '|':
                    outname = onechain[1:i-1]+onechain[i:len(onechain)] + '.data'

            fw_feat = open(outdir + '/' + outname, 'w')
            continue
        seq = eachline.strip()
        number = 0
        for i in range(len(seq)-1):
            if (seq[i] == 'C' and seq[i+1]=='A'):
                number=number+1
        #print(number)

        fw_feat.write(str(number)+ '\n')
        fw_feat.close()
    fr_fasta.close()
def encode_GT_by_fasta(fasta,outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fr_fasta = open(fasta,'r')
    for eachline in fr_fasta:
        if '>' in eachline:
            onechain = eachline.strip()
            for i in range(len(onechain)):
                if onechain[i]== ':' or '/' or " \ "or '?' or '"' or '<' or '>' or '|':
                    outname = onechain[1:i-1]+onechain[i:len(onechain)] + '.data'

            fw_feat = open(outdir + '/' + outname, 'w')
            continue
        seq = eachline.strip()
        number = 0
        for i in range(len(seq)-1):
            if (seq[i] == 'G' and seq[i+1]=='T'):
                number=number+1
        #print(number)
        fw_feat.write(str(number)+ '\n')
        fw_feat.close()
    fr_fasta.close()

def encode_CT_by_fasta(fasta,outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fr_fasta = open(fasta,'r')
    for eachline in fr_fasta:
        if '>' in eachline:
            onechain = eachline.strip()
            for i in range(len(onechain)):
                if onechain[i]== ':' or '/' or " \ "or '?' or '"' or '<' or '>' or '|':
                    outname = onechain[1:i-1]+onechain[i:len(onechain)] + '.data'

            fw_feat = open(outdir + '/' + outname, 'w')
            continue
        seq = eachline.strip()
        number = 0
        for i in range(len(seq)-1):
            if (seq[i] == 'C' and seq[i+1]=='T'):
                number=number+1
        #print(number)
        fw_feat.write(str(number)+ '\n')
        fw_feat.close()
    fr_fasta.close()
def encode_GA_by_fasta(fasta,outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fr_fasta = open(fasta,'r')
    for eachline in fr_fasta:
        if '>' in eachline:
            onechain = eachline.strip()
            for i in range(len(onechain)):
                if onechain[i]== ':' or '/' or " \ "or '?' or '"' or '<' or '>' or '|':
                    outname = onechain[1:i-1]+onechain[i:len(onechain)] + '.data'

            fw_feat = open(outdir + '/' + outname, 'w')
            continue
        seq = eachline.strip()
        number = 0
        for i in range(len(seq)-1):
            if (seq[i] == 'G' and seq[i+1]=='A'):
                number=number+1
        #print(number)
        fw_feat.write(str(number)+ '\n')
        fw_feat.close()
    fr_fasta.close()
def encode_CG_by_fasta(fasta,outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fr_fasta = open(fasta,'r')
    for eachline in fr_fasta:
        if '>' in eachline:
            onechain = eachline.strip()
            for i in range(len(onechain)):
                if onechain[i]== ':' or '/' or " \ "or '?' or '"' or '<' or '>' or '|':
                    outname = onechain[1:i-1]+onechain[i:len(onechain)] + '.data'

            fw_feat = open(outdir + '/' + outname, 'w')
            continue
        seq = eachline.strip()
        number = 0
        for i in range(len(seq)-1):
            if (seq[i] == 'C' and seq[i+1]=='G'):
                number=number+1
        #print(number)
        fw_feat.write(str(number)+ '\n')
        fw_feat.close()
    fr_fasta.close()
def encode_GC_by_fasta(fasta,outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fr_fasta = open(fasta,'r')
    for eachline in fr_fasta:
        if '>' in eachline:
            onechain = eachline.strip()
            for i in range(len(onechain)):
                if onechain[i]== ':' or '/' or " \ "or '?' or '"' or '<' or '>' or '|':
                    outname = onechain[1:i-1]+onechain[i:len(onechain)] + '.data'

            fw_feat = open(outdir + '/' + outname, 'w')
            continue
        seq = eachline.strip()
        number = 0
        for i in range(len(seq)-1):
            if (seq[i] == 'G' and seq[i+1]=='C'):
                number=number+1
        #print(number)
        fw_feat.write(str(number)+ '\n')
        fw_feat.close()
    fr_fasta.close()
def encode_GG_by_fasta(fasta,outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fr_fasta = open(fasta,'r')
    for eachline in fr_fasta:
        if '>' in eachline:
            onechain = eachline.strip()
            for i in range(len(onechain)):
                if onechain[i]== ':' or '/' or " \ "or '?' or '"' or '<' or '>' or '|':
                    outname = onechain[1:i-1]+onechain[i:len(onechain)] + '.data'

            fw_feat = open(outdir + '/' + outname, 'w')
            continue
        seq = eachline.strip()
        number = 0
        for i in range(len(seq)-1):
            if (seq[i] == 'G' and seq[i+1]=='G') or (seq[i] == 'C' and seq[i+1]=='C'):
                number=number+1
        #print(number)
        fw_feat.write(str(number)+ '\n')
        fw_feat.close()
    fr_fasta.close()

'''
if __name__=="__main__":
    params1 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/test_dna_seq_new.fasta'
    #params2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_AA'
    #params2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_AT'
    #params2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_TA'
    #params2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_CA'
    #params2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_GT'
    #params2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_CT'
    #params2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_GA'
    #params2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_CG'
    #params2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_GC'
    params2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_GG'


    encode_AA_by_fasta(params1, params2)
    #encode_AA_by_fasta(params1, params3)
    #encode_AA_by_fasta(params1, params4)
    #encode_AA_by_fasta(params1, params5)
    #encode_AA_by_fasta(params1, params6)
    #encode_AA_by_fasta(params1, params7)
    #encode_AA_by_fasta(params1, params8)
    #encode_AA_by_fasta(params1, params9)
    #encode_AA_by_fasta(params1, params10)
    #encode_AA_by_fasta(params1, params11)
'''


