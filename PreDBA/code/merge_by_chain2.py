#!/usr/bin/python
#-*- coding: utf-8 -*-

import os

def merge_ab_by_chain(featdir, chainfile, outfile, window_size = 1):
    rsize = int(window_size/2)
    fw_out = open(outfile, 'w')
    content = ''
    #print (featdir)
    with open(chainfile, 'r') as fr_chain:
        for eachchain in fr_chain:
            chainname = eachchain.strip()
            if not chainname:
                continue
            path_feat = featdir + '/' + chainname + '.data'            
            with open(path_feat, 'r') as fo_feat:
                fr_feat = fo_feat.readlines()
                size = len(fr_feat) - rsize
                if not fr_feat[-1].strip():
                    size = rsize + 1
                for i in range(rsize, size):
                    if fr_feat[i].strip():
                        content += fr_feat[i]
        fw_out.write(content)
    fw_out.close()


'''
if __name__=="__main__":
    featdir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_ab'
    chainfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/chainDouble1.txt'
    outfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/merged_encode_ab.data'
    merge_ab_by_chain(featdir, chainfile, outfile)

'''
