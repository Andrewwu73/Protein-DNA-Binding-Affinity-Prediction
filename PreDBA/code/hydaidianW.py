#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def spiltHyddW(labelfile, hyddir, outdir):
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
        content = []
        hydfile = hyddir + "/" + chainname + ".data"
        fo_hyd = open(hydfile + "", 'r')
        fr_hyd = fo_hyd.readlines()
        number = 0
        temp = 0
        for eachline in fr_hyd:
            oneline = eachline.split('\t')
            content2=oneline[0].strip()+ oneline[1].strip() + oneline[3].strip()
            if content2 == content1:
                if oneline[2] == "H" or oneline[2] == "R" or oneline[2] == "K" or oneline[2] == "E" \
                        or oneline[2] == "D":
                    content.append(str(1.0) + '\n')
                else:content.append(str(0.0)+'\n')
        fw_feat.write(''.join(content))
        pre_chain = chainname
    fo_label.close()
    fo_hyd.close()
    fw_feat.close()
'''
if __name__ == "__main__":
    labelfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/Actual.binding.site_new_5.0.data'
    hyddir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_abhhh/'
    outdir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/numhddW'
    spiltHyxxc(labelfile, hyddir, outdir)

'''