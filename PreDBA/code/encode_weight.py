#!/usr/bin/python
# -*- coding: utf-8 -*-


import os

def encode_phy(dssp, AAfea_phy, outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    dsspfile = open(dssp, 'r')
    fo_fea = open(AAfea_phy, 'r')   
    fr_fea = fo_fea.readlines()
    content = []; 
    pre_chain = [];AA_pos = 0
    for eachline in dsspfile:
        oneline = eachline.split('\t')
        AA_code = oneline[4].strip()
        print(AA_code)
        chainname = oneline[0].strip() + oneline[3].strip()
        if chainname != pre_chain:
            outname = chainname + '.data'
            fw_feat = open(outdir + '/' + outname, 'w')
            AA_pos  = 0
        AA_pos +=1
        content = []
        for onelinefea in fr_fea:
            linefea = onelinefea.split('\t')
            if AA_code == linefea[1].strip():
                #content.append(linefea[2].strip() + '\t') #1.ԭ�Ӹ���-
                #content.append(linefea[3].strip() + '\t') #2.������-
                #content.append(linefea[4].strip() + '\t') #3.�������-
                content.append(linefea[5].strip() + '\t') #4.Mmass
                #content.append(linefea[6].strip() + '\t') #5.hydro1��ˮ��-
                #content.append(linefea[7].strip() + '\t') #6.��ˮ��ָ�� 
                #content.append(linefea[8].strip() + '\t') #7.����
                #content.append(linefea[9].strip() + '\t') #8.������
                #content.append(linefea[10].strip() + '\t')#9.����
                #content.append(linefea[11].strip())       #10.ƽ���ɼ������
                break
        fw_feat.write(''.join(content)+ '\n')
        pre_chain = chainname
    fw_feat.close() 
    fo_fea.close()
    dsspfile.close()

def encode_weight_by_fasta(fasta, AAfea_phy, outdir):
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
            AA_code = seq[i]
            for onelinefea in fr_fea:
                linefea = onelinefea.split('\t')
                if AA_code == linefea[1].strip():
                    #content.append(linefea[2].strip() + '\t') #1.ԭ�Ӹ���
                    #content.append(linefea[3].strip() + '\t') #2.������
                    #content.append(linefea[4].strip() + '\t') #3.�������
                    content.append(linefea[5].strip() + '\t') #4.Mmass
                    #content.append(linefea[6].strip() + '\t') #5.hydro1��ˮ��
                    #content.append(linefea[7].strip() + '\t') #6.��ˮ��ָ��
                    #content.append(linefea[8].strip() + '\t') #7.����
                    #content.append(linefea[9].strip() + '\t') #8.������
                    #content.append(linefea[10].strip() + '\t')#9.����
                    #content.append(linefea[11].strip())      #10.ƽ���ɼ������
                    break
            fw_feat.write(''.join(content)+ '\n')
        fw_feat.close()
    fr_fasta.close()
'''
if __name__=="__main__":
    params1 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/ProDoubleDNA.fasta'
    params2 = '/ifs/gdata1/yangwenyi/DATA/_Global_data/AAfea_phy.txt'
    params3 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_weight'
    #encode_phy(params1, params2, params3)
    encode_weight_by_fasta(params1, params2, params3)
'''