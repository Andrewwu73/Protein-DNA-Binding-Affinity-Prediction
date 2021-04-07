#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def spiltBind(bindfile, chainfile, outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    with open(chainfile, 'r') as fr_chain:
        for eachline in fr_chain:
            onechain = eachline.strip()
            #print(onechain[1])
            onechain1='>'+onechain[0:-1]+':'+onechain[-1]
            print(onechain1)
            outname = onechain + '.data'
            fw_sp = open(outdir + '/' + outname, 'w')
            #print (onechain)
            with open(bindfile, 'r') as fr_bind:
                files = fr_bind.readlines()
                size = len(files)
                #print (size)
                for i in range(size):
                    if onechain1 == files[i].strip():
                        value = str(files[i]) + str(files[i+1]) +str(files[i+2])
                        fw_sp.write(str(value))
                        i = i + 3
        fw_sp.close()

'''
if __name__ == "__main__":
    bindfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/binding_sites_Double_5.0.data'
    outchain = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/chainDouble1.txt'
    outdir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_spbind'
    spiltBind(bindfile, outchain, outdir)
'''