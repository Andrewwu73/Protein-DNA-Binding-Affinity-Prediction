#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def spiltrnaBind(bindfile, chainfile, outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    with open(chainfile, 'r') as fr_chain:
        for eachline in fr_chain:
            onechain = eachline.strip()
            #print(onechain[1])
            onechain1='>'+onechain[0:4]+':'+onechain[4]
            #print(onechain1)
            outname = onechain + '.data'
            fw_sp = open(outdir + '/' + outname, 'w')
            #print (onechain)
            with open(bindfile, 'r') as fr_bind:
                files = fr_bind.readlines()
                size = len(files)
                #print (size)
                for i in range(size):
                    if onechain1 == files[i].strip():
                        value = str(files[i]) + str(files[i+1])
                        fw_sp.write(str(value))
                        i = i + 2
        fw_sp.close()


if __name__ == "__main__":
    bindfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/ProDoubleDNA.fasta'
    chainfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/chainDouble1.txt'
    outdir = '//ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/fasta_86'
    spiltrnaBind(bindfile, chainfile, outdir)
