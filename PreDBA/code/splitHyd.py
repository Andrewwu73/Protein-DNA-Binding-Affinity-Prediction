#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def spiltHyd(labelfile, hydfile, outdir):
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
        #hydfile = dsspdir + "/" + chainname[0:4] + ".dssp.format"
        fo_hyd = open(hydfile + "", 'r')
        fr_hyd = fo_hyd.readlines()
        for eachline in fr_hyd:
            oneline = eachline.split('\t')
            content2=oneline[0].strip()+ oneline[1].strip() + oneline[3].strip()
            if content2 == content1:
                    content.append(eachline)
        fw_feat.write(''.join(content))
        pre_chain = chainname
    fo_label.close()
    fo_hyd.close()
    fw_feat.close()
'''
if __name__ == "__main__":
    labelfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/Actual.binding.site_new_5.0.data'
    hydfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/combine_ab_label.data'
    outdir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_abhhh/'
    spiltHyd(labelfile, hydfile, outdir)
'''