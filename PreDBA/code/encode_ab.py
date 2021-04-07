#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os

def encode_ab_by_label(labelfile, dsspdir, outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fo_label = open(labelfile, 'r')
    fr_label = fo_label.readlines()
    content1 = ''; content2 = ''
    pre_chain = []
    for eachlabel in fr_label:
        if not len(eachlabel.strip()):
            continue
        onelabel = eachlabel.strip().split('\t')
        chainname = onelabel[0] + onelabel[1]
        if chainname != pre_chain:
            outname = chainname + '.data'
            fw_feat = open(outdir + '/' + outname, 'w')
        content1 = chainname + onelabel[3]
        flag = False
        content = []
        dsspfile = dsspdir + "/" + chainname.strip()[0:-1] + ".dssp.format"
        #print(dsspfile)
        fo_dssp = open(dsspfile + "", 'r')
        fr_dssp = fo_dssp.readlines()
        for eachline in fr_dssp:
            oneline = eachline.split('\t')
            content2=oneline[0].strip()+oneline[3].strip()+oneline[2].strip()
            if content2 == content1:
                if 'H'in oneline[5]:
                    #print(1)
                    content.append('1\t0')
                elif 'E' in oneline[5]:
                    #print(2)
                    content.append('0\t1')
                else :content.append('0\t0')
                flag = True
                break
        if flag == False:
            content.append('0\t0')
        fw_feat.write(''.join(content) + '\n')

        #print(fw_feat)
        pre_chain = chainname
        #print(pre_chain)
    fo_label.close()
    fo_dssp.close()
    fw_feat.close()
'''

if __name__=="__main__":

    params1 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/Actual.binding.site_new_5.0.data'
    params2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/DSSP/format/'
    params3 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_ab'
    encode_ab_by_label(params1, params2, params3)
'''