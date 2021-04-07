#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def numHyd(labelfile, hyddir, outdir):
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

                if oneline[4] =='+1':
                    number=number + 1

                    if oneline[2] =="S" or oneline[2] == "T" or oneline[2] == "Y" or oneline[2] == "N" \
                            or oneline[2] =="Q" or oneline[2] =="C" or oneline[2] =="G" :
                        content.append(str(1) + '\n')

                    elif oneline[2] =="A" or oneline[2] == "F" or oneline[2] == "I" or oneline[2] == "L" \
                            or oneline[2] =="V" or oneline[2] =="P" or oneline[2] =="M" or oneline[2] == "W":
                        content.append(str(-1) + '\n')

                    else:content.append(str(0) +'\n')
        fw_feat.write(''.join(content))
        pre_chain = chainname
    fo_label.close()
    fo_hyd.close()
    fw_feat.close()
'''
if __name__ == "__main__":
    labelfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/Actual.binding.site_new_5.0.data'
    hyddir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_abhhh/'
    outdir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/numhyd'
    numHyd(labelfile, hyddir, outdir)
'''