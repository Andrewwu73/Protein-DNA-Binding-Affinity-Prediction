#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def extraRNAfea(rnafoldfile,MFEfile,EDfile):
    with open(MFEfile,'w') as fw:
        with open(rnafoldfile,'r') as fr:
            for eachline in fr:
                if ' frequency of mfe structure in ensemble' in eachline:
                    #print(eachline)
                    files=eachline.split(';')
                    files1=files[0].split(' ')
                    #print(files1[7])
                    MFE=float(files1[7])*100
                    fw.write(str(MFE)+'\n')

    with open(EDfile,'w') as f1w:
        with open(rnafoldfile,'r') as fr:
            for eachline in fr:
                if ' frequency of mfe structure in ensemble' in eachline:
                    #print(eachline)
                    files=eachline.split(';')
                    files1=files[1].split(' ')
                    #print(files1[3])
                    ED=float(files1[3])
                    f1w.write(str(ED)+'\n')

'''
if __name__ == "__main__":
    rnafoldfile = "/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/rnaout"
    MFEfile = "/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/mergedfea/added_encode_MFE.data"
    EDfile = "/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/mergedfea/added_encode_ED.data"
    extraRNAfea(rnafoldfile, MFEfile, EDfile)
'''