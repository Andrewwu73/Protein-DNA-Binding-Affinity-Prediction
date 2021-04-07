#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


def encode_walx(dssp,AAfea_phy,outdir):
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
        if 'H' in oneline[5]:
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


def encode_walx_by_label(labelfile, dsspdir, outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fo_label = open(labelfile, 'r')
    fr_label = fo_label.readlines()
    content1 = '';
    content2 = ''
    pre_chain = []
    for eachlabel in fr_label:
        if not len(eachlabel.strip()):
            continue
        onelabel = eachlabel.strip().split('\t')
        chainname = onelabel[0] + onelabel[1]
        if chainname != pre_chain:
            outname = chainname + '.data'
            fw_feat = open(outdir + '/' + outname, 'wa')
        content1 = chainname + onelabel[3]
        flag = False
        content = []
        dsspfile = dsspdir + "/" + chainname[0:4] + ".dssp.format"
        fo_dssp = open(dsspfile + "", 'r')
        fr_dssp = fo_dssp.readlines()
        for eachline in fr_dssp:
            oneline = eachline.split('\t')
            content2 = oneline[0].strip() + oneline[3].strip() + oneline[2].strip()
            if content2 == content1:
                if 'H' in oneline[5]:
                    content.append('1\t0')
                elif 'E' in oneline[5]:
                    content.append('0\t1')
                else:
                    content.append('0\t0')
                flag = True
                break
        if flag == False:
            content.append('0\t0')
        fw_feat.write(''.join(content) + '\n')
        pre_chain = chainname
    fo_label.close()
    fo_dssp.close()
    fw_feat.close()
    return True

'''
if __name__ == "__main__":
    dssp = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/DSSP/DSSP3'
    AAfea_phy= '/ifs/gdata1/yangwenyi/DATA/_Global_data/AAfea_phy.txt'
    outdir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_walx'
    encode_walx(dssp,AAfea_phy,outdir)
    #params1 = '/ifs/gdata1/yangwenyi/TESTALL/TEST_5/test5_label_6.0.data'
    #params2 = '/ifs/gdata1/yangwenyi/TESTALL/PDB/DSSP_OUT5/format'
    #params3 = '/ifs/gdata1/yangwenyi/TESTALL/TEST_5/test6.0/encode/encode_ab'
    #encode_ss_by_label(params1, params2, params3)

'''