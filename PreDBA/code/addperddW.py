#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import numpy as np
'''
        簱    ͷ    就     ڽ  λ    ռ İٷֱ 
'''

# import pandas as pd
def addperddW(featdir, chainfile, outfile):
    fw_out = open(outfile, 'w')
    #print featdir
    with open(chainfile, 'r') as fr_chain:
        for eachchain in fr_chain:
            chainname = eachchain.strip()
            if not chainname:
                continue
            path_feat = featdir + '/' + chainname + '.data'
            with open(path_feat, 'r') as fo_feat:
                fr_feat = fo_feat.readlines()
                size = len(fr_feat)
                #print (size)
                per = 0
                sum = 0
                for i in range(size):
                    if fr_feat[i].strip()=='1.0':
                        sum += 1
                #print (sum)
                if size != 0:
                    per = float(sum) / float(size)*100
                else:per = 0
                #print (sum)
                #print (per)
                fw_out.write(str(per) + '\n')
        fw_out.close()

'''
if __name__ == "__main__":
    featdir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/numhddW'
    chainfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/chainDouble1.txt'
    outfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/mergedfea/added_encode_per_ddW.data'
    addperxxc(featdir, chainfile, outfile)
'''
