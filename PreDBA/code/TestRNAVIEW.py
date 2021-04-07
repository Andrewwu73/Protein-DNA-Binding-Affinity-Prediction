#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
def RNAVIEW(namefile,pdbdir):
    #if not os.path.exists(rnaviewdir):
        #os.mkdir(rnaviewdir)
    #rnaview_file = rnaviewdir + '/' + "rnaview.out"
    #os.chdir(rnaviewdir)
    filename=open(namefile, 'r')
    for eachline in filename:
        pdb_name = eachline.strip()
    print(pdb_name)
    pdbfile = pdbdir+'/'+pdb_name+'.pdb'
    command = "../bin/RNAVIEW/bin/rnaview "+ pdbfile
    print(command)
    os.system(command)
