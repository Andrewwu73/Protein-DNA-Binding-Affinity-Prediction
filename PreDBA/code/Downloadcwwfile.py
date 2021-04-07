#/usr/bin/python
# -*- coding: utf-8 -*-
import os
def downloadPDB(namefile,PDBdir):
    if not os.path.exists(PDBdir):
        os.mkdir(PDBdir)
    inputfile = open(namefile,'r')
    #outdir='/PDB'
    for eachline in inputfile:
        print (eachline)
        pdbname = eachline.lower().strip()[0:4]
        os.system("wget http://ndbserver.rutgers.edu/service/ndb/atlas/stfeatures?searchTarget=" + pdbname + "&ftrType=bphbc&type=csv")

        os.system("gzip -d pdb" + pdbname + '.ent.gz')
        os.system("mv pdb" + pdbname + ".ent " + pdbname.upper() + '.pdb')
        os.system("mv "+pdbname.upper()+'.pdb '+PDBdir)
    inputfile.close()
