#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
#������λ��ٷֱ�
def perOfDNAbind(binddir, chainfile, outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    with open(chainfile, 'r') as fr_chain:
        for eachline in fr_chain:
            onechain = eachline.strip()
            outname = onechain + '.data'
            fw_np = open(outdir + '/' + outname, 'w')
            #print (onechain)
            if onechain:
                path_bind = binddir + '/' + onechain + '.data'
                with open(path_bind, 'r') as fr_bind:
                    files = fr_bind.readlines()
                    seq = files[2].strip()
                    num = 0
                    for i in range(len(seq)):
                        if seq[i] == '+':
                            num +=1
                    value = float(num)/float(len(seq))*100
                    #print (value)
		          
                    fw_np.write(str(value) + '\n')
            fw_np.close()


'''
if __name__ == "__main__":

    binddir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_dnaspbind'
    chainfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/chainDouble_D1.txt'
    outdir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/encode/encode_perdnabind'
    perOfRNAbind(binddir, chainfile, outdir)
'''