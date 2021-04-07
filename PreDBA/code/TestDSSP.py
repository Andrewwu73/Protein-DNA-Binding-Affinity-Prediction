#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
pdbתdssp    ҪDSSP
'''
import os

def formatdsspline(dsspline):
    eachline = dsspline
    col = '\t' + eachline[0:5]
    col += '\t' + eachline[5:10]
    col += '\t' + eachline[10:12]
    col += '\t' + eachline[12:15]
    col += '\t' + eachline[15:25]
    col += '\t' + eachline[25:29]
    col += '\t' + eachline[29:34]
    col += '\t' + eachline[34:38]
    col += '\t' + eachline[38:50]
    col += '\t' + eachline[50:61]
    col += '\t' + eachline[61:72]
    col += '\t' + eachline[72:83]
    col += '\t' + eachline[83:92]
    col += '\t' + eachline[92:97]
    col += '\t' + eachline[97:103]
    col += '\t' + eachline[103:109]
    col += '\t' + eachline[109:115]
    col += '\t' + eachline[115:122]
    col += '\t' + eachline[122:129]
    col += '\t' + eachline[129:136]
    return col


def pdbToDSSP(pdbnamefile, pdbdir, dsspdir, formatdir):
    if not os.path.exists(dsspdir):
        os.mkdir(dsspdir)
    pdbfiles = os.listdir(pdbdir)
    for filename in pdbfiles:
        name = filename.split('.')[0]
        pdbfile = pdbdir + '/' + filename
        dssp_file = dsspdir + '/' + name + ".dssp"
        command = "../code/dssp2 -i %s -o %s" % (pdbfile, dssp_file)
        os.system(command)

    dsspfiles = os.listdir(dsspdir)

    if os.path.exists(dsspdir + '/DSSP'):
        dsspfiles.remove('DSSP')

    with open(pdbnamefile, 'r') as namefile:

        for eachline in namefile:
            pdb_name = eachline.strip()
            dssp_file = pdb_name + '.dssp'
            output = open(dsspdir + '/DSSP', 'w')
            for dssp_file in dsspfiles:
                pdb_name = dssp_file.split('.')[0]
                with open(dsspdir + '/' + dssp_file, "r") as fr:
                    if not os.path.isdir(formatdir):
                        os.mkdir(formatdir)

                    with open(formatdir + '/' + pdb_name + '.dssp.format', 'w') as singleOut:

                        count = 0
                        for eachline in fr.readlines():
                            list1 = []
                            count += 1
                            list1.append(pdb_name)
                            if count >= 29:
                                eachline = formatdsspline(eachline)
                                list1.append(eachline)
                                content = ''.join(list1) + '\n'
                                output.write(content)
                                singleOut.write(content)


'''

if __name__ == "__main__":
    pdbnamefile = "/ifs/gdata1/yangwenyi/TestAll1/Test1/name1.data"
    pdbdir = "/ifs/gdata1/yangwenyi/TestAll1/Test1/PDB0"
    dsspdir = "/ifs/gdata1/yangwenyi/TestAll1/DSSP1/dssp"
    formatdir = '/ifs/gdata1/yangwenyi/TestAll1/DSSP1/format'
    pdbToDSSP(pdbnamefile, pdbdir, dsspdir, formatdir)
'''