#!/usr/bin/python
# -*- coding: utf-8 -*-

#二级结构 ---根据dssp的
import os

MaxAcc = {'A': 106, 'C': 135, 'D': 163, 'E': 194,
          'F': 197, 'G': 84, 'H': 184, 'I': 169,
          'K': 205, 'L': 164, 'M': 188, 'N': 157,
          'P': 136, 'Q': 198, 'R': 248, 'S': 130,
          'T': 142, 'V': 142, 'W': 227, 'Y': 222}
          
def encode_rasa(dssp, outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    dsspfile = open(dssp,'r')
    content = []
    pre_chain = [];AA_pos = 0
    for eachline in dsspfile:
        oneline = eachline.split('\t')
        AA_code = oneline[4].strip()
        #print (AA_code)
        chainname = oneline[0].strip() + oneline[3].strip()
        if chainname != pre_chain:
            outname = chainname + '.data'
            fw_feat = open(outdir + '/' + outname, 'wa')
            AA_pos  = 0
        AA_pos +=1
        content = []
        num1 = float(oneline[14].strip())
        num2 = float(MaxAcc[AA_code])
        content.append(str(float('%.3f' % (num1/num2))) + '\t') 
        fw_feat.write(''.join(content)+ '\n')
        pre_chain = chainname
    dsspfile.close()
    fw_feat.close() 


def encode_rasa_by_label(labelfile, dsspdir, outdir):
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
        AA_code = onelabel[2]
        if chainname != pre_chain:
            outname = chainname + '.data'
            fw_feat = open(outdir + '/' + outname, 'w')
        content1 = chainname + onelabel[3]
        content = []
        num1 = 0
        dsspfile = dsspdir + "/" + chainname.strip()[0:-1] + ".dssp.format"
        fo_dssp = open(dsspfile + "", 'r')
        fr_dssp = fo_dssp.readlines() 
        for eachline in fr_dssp:
            oneline = eachline.split('\t')
            content2=oneline[0].strip()+oneline[3].strip()+oneline[2].strip()
            if content2 == content1:
                num1 = float(oneline[8].strip())
                #print num1
                break
        num2 = float(MaxAcc[AA_code])
        content.append(str(float('%.3f' % (num1/num2)))) 
        fw_feat.write(''.join(content)+ '\n')
        pre_chain = chainname
    fo_label.close()
    fo_dssp.close()
    fw_feat.close()
    return True
'''
if __name__=="__main__":

    params1 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/Actual.binding.site_new_5.0.data'
    params2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/DSSP/format/'
    params3 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_rasa'
    encode_rasa_by_label(params1, params2, params3)
'''
