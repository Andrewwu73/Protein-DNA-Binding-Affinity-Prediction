#/usr/bin/python
#_*_ coding: utf-8 _*_
# desc: format protein chain file to get protein name file
import os                         
def getProteinfromChain(chainfile, outname):
    with open(outname,'w') as fo:
        ow = []
        with open(chainfile,'r') as fr:
            for eachline in fr:
                pdb_name = eachline.upper().strip()[0:4]
                if(ow.count(pdb_name+'\n') == 0):
                    ow.append(pdb_name+'\n')
        fo.write(''.join(sorted(ow))) 
