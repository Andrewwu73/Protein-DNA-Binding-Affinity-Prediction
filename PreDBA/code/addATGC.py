#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import numpy as np

def addATGC(featdir, chainfile, outdir,outfile):
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
                size = len(fr_feat)
                # print size
                sum = 0
                for i in range(size):
                    if fr_feat[i].strip():
                        sum += int(fr_feat[i])
                # print sum
                fw_out.write(str((sum)) + '\n')
        fw_out.close()
