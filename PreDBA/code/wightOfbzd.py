#!/usr/bin/python
# -*- coding: utf-8 -*-


import os


def encode_wbzd(dssp,AAfea_phy,outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    dsspfile = open(dssp, 'r')
    fo_fea = open(AAfea_phy, 'r')
    fr_fea = fo_fea.readlines()
    content = []
    pre_chain = []
    AA_pos = 0
    for eachline in dsspfile:
        oneline = eachline.split('\t')
        AA_code = oneline[4].strip()
        #print(AA_code)
        chainname = oneline[0].strip() + oneline[3].strip()
        if chainname != pre_chain:
            outname = chainname + '.data'
            fw_feat = open(outdir + '/' + outname, 'w')
            AA_pos = 0
        AA_pos += 1
        content = []
        if 'E' in oneline[5]:
            for onelinefea in fr_fea:
                linefea = onelinefea.split('\t')

                if AA_code == linefea[1].strip():
                    content.append(linefea[5].strip() + '\t') #4.Mmass
                    break
        else:
            content.append('0')
        fw_feat.write(''.join(content) + '\n')
        pre_chain = chainname
    dsspfile.close()
    fw_feat.close()

'''

if __name__ == "__main__":
    dssp = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/DSSP/DSSP3'
    AAfea_phy= '/ifs/gdata1/yangwenyi/DATA/_Global_data/AAfea_phy.txt'
    outdir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_wbzd'
    encode_wbzd(dssp,AAfea_phy,outdir)
'''

