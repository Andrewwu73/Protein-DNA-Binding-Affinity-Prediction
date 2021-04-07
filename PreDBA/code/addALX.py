#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import numpy as np

'''
计算a螺旋和bzhedie

'''

# import pandas as pd
def addnumalx(featdir, chainfile, outfile):
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
                    if fr_feat[i].strip()=='1':
                        sum += 1
                #print (sum)
                if size:
                    per = float(sum) / float(size)*100
                else:per = 0
                #print (sum)
                #print (per)
                fw_out.write(str(sum) + '\n')
        fw_out.close()



