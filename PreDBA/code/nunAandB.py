#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import numpy as np

def addAandB(featdir, chainfile, outdir,outfile):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fw_out = open(outdir+'/'+outfile, 'w')
    #print featdir
    with open(chainfile, 'r') as fr_chain:
        for eachchain in fr_chain:
            chainname = eachchain.strip()
            if not chainname:
                continue
            path_feat = featdir + '/' + chainname + '.data'
            with open(path_feat, 'r') as fo_feat:
                fr_feat = fo_feat.readlines()
                size = len(fr_feat)-1
                #print(size)
                number = 0
                for i in range(size):

                    #print(fr_feat[i])
                    if str(fr_feat[i].strip())!='0' and str(fr_feat[i+1].strip())=='0':
                        number=number+1
                        #print(1)
                #print(number)
                fw_out.write(str((number)) + '\n')
        fw_out.close()

'''
if __name__ == "__main__":
    featdir1 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_walx'
    featdir2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_wbzd'
    chainfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/chainDouble1.txt'
    outdir='/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/mergedfea'
    outfile1 = 'added_encode_numA.data'
    outfile2 = 'added_encode_numB.data'


    addAandB(featdir1, chainfile, outdir, outfile1)
    addAandB(featdir2, chainfile, outdir, outfile2)
'''
