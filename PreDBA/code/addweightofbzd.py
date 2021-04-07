#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import numpy as np
#b折叠
def addbzdWeight(featdir, chainfile, outfile):
    fw_out = open(outfile, 'w')
    #print (featdir)
    with open(chainfile, 'r') as fr_chain:
        for eachchain in fr_chain:
            chainname = eachchain.strip()
            if not chainname:
                continue
            path_feat = featdir + '/' + chainname + '.data'
            with open(path_feat, 'r') as fo_feat:
                fr_feat = fo_feat.readlines()
                size = len(fr_feat)
                # print size
                sum = 0
                for i in range(size):
                    if fr_feat[i].strip():
                        sum += float(fr_feat[i])
                # print sum
                fw_out.write(str(float(sum)) + '\n')
        fw_out.close()

'''
if __name__ == "__main__":
    featdir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_wbzd'
    chainfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/chainDouble1.txt'
    outfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/mergedfea/added_encode_wbzd.data'
    addbzdWeight(featdir, chainfile, outfile)
'''