#!/usr/bin/python
# -*- coding: utf-8 -*-
# 计算残基的各个原子和残基重心的距离
# 替换氨基酸名称   over
import os
import math
import shutil

def raplaceAA(strline):
    strline = strline.replace('ALA', '  A').replace('ARG', '  R'). \
        replace('ASN', '  N').replace('ASP', '  D').replace('CYS', '  C'). \
        replace('GLU', '  E').replace('GLN', '  Q').replace('GLY', '  G'). \
        replace('HIS', '  H').replace('ILE', '  I').replace('LEU', '  L'). \
        replace('LYS', '  K').replace('MET', '  M').replace('PHE', '  F'). \
        replace('PRO', '  P').replace('SER', '  S').replace('THR', '  T'). \
        replace('TRP', '  W').replace('TYR', '  Y').replace('VAL', '  V')
    return strline
def raplaceDA(strline):
    strline = strline.replace(' DT', '  T').replace(' DA', '  A'). \
        replace(' DG', '  G').replace(' DC', '  C')
    return strline

# 处理PDB文件,每列用‘\t’隔开，得到的是.format.pdb文件  over
def pdbformat(eachline):
    col = eachline[0:4]
    col += '\t' + eachline[4:11]
    col += '\t' + eachline[11:17]
    col += '\t' + eachline[17:20]
    col += '\t' + eachline[20:22]
    col += '\t' + eachline[22:27]
    col += '\t' + eachline[27:38]
    col += '\t' + eachline[38:46]
    col += '\t' + eachline[46:54]
    col += '\t' + eachline[54:60]
    col += '\t' + eachline[60:66]
    col += '\t' + eachline[66:78] + '\n'
    return col


# inputfile: pdb name list file,pdbdir
# return AA_chain pdbfile,dna.info
def removeATGC(pdbnamefile, pdbdir):
    name_list = open(pdbnamefile, 'r')
    name_term = []
    if len(pdbdir):
        pdbdir = pdbdir + '/'
    for name in name_list:
        name_term = name.split()
        protein_name = pdbdir + name_term[0] + '.pdb'
        file_out = name_term[0] + '.rm.pdb'
        file_dna = name_term[0] + '.dna.pdb'

        AAdir = pdbdir + '/AAdir'
        DNAdir = pdbdir + '/DNAdir'
        if not os.path.isdir(AAdir):
            os.mkdir(AAdir)
        if not os.path.isdir(DNAdir):
            os.mkdir(DNAdir)

        output = open(AAdir + '/' + file_out, 'w')
        outAUGC = open(DNAdir + '/' + file_dna, 'w')

        protein_list = open(protein_name, 'r')
        protein_term = []
        for protein in protein_list:
            protein_term = protein.split()
            if protein_term[0] == 'ATOM':
                temp = 0
                if protein[17:20]==' DA' or protein[17:20]==' DT' \
                    or protein[17:20]==' DG' or protein[17:20]==' DC':
                    temp = temp + 1
                if temp == 0:
                    eachline = raplaceAA(protein)
                    eachline = pdbformat(eachline)
                    output.write(eachline)
                else:
                    eachline = raplaceDA(protein)
                    #print(eachline)
                    eachline = pdbformat(eachline)
                    outAUGC.write(eachline)
                    #print(eachline)

        protein_list.close()
        output.close()
        outAUGC.close()
    name_list.close()

# 求出原子的最小距离，放到outseq中
def caldnaDistance(mypdb, chainID, mydna, cutoff):
    fo_pdb = open(mypdb, 'r')
    pdbinput = fo_pdb.readlines()
    content1 = '';
    content2 = ''
    with open(mydna, 'r') as dnainput:
        dnaname = mydna.split('/')[-1].split('.')[0]
        firstline = [];
        secondline = [];
        thirdline = []
        preDName = [];
        prePos = [];
        isbsite = "-"
        for eachline1 in dnainput:
            onednaline = eachline1.split('\t')
            if str(chainID) != onednaline[4].strip():
                continue
            firstline = []
            firstline.append('>' + ''.join(dnaname) + ':' + \
                             ''.join(onednaline[4].strip()))
            resName = onednaline[3].strip()
            resPos = onednaline[5].strip()
            if isbsite == '+' and resName == preDName and resPos == prePos:
                continue
            if (resName != preDName or resPos != prePos) and len(preDName):
                secondline.append(preDName)
                thirdline.append(isbsite)
                val_class = '-1'
                if isbsite == '+':
                    val_class = '+1'
                col = dnaname + '\t' + chainID + '\t' + preDName + '\t' + prePos + '\t' + val_class + '\n'
                content2 += col
                isbsite = '-'
            preDName = resName
            prePos = resPos
            for eachline2 in pdbinput:
                onepdbline = eachline2.split('\t')
                distx = float(onepdbline[6].strip()) - float(onednaline[6].strip())
                disty = float(onepdbline[7].strip()) - float(onednaline[7].strip())
                distz = float(onepdbline[8].strip()) - float(onednaline[8].strip())
                dist = math.sqrt(distx * distx + disty * disty + distz * distz)
                if dist - cutoff <= 0.0:
                    isbsite = "+"
                    break
        secondline.append(preDName)
        thirdline.append(isbsite)
        val_class = '-1'
        if isbsite == '+':
            val_class = '+1'
        col = dnaname + '\t' + chainID + '\t' + preDName + '\t' + prePos + '\t' + val_class + '\n'
        content2 += col
    content1 = ''.join(map(str, firstline)) + '\n' + ''.join(map(str, secondline)) \
               + '\n' + ''.join(map(str, thirdline))
    fo_pdb.close()
    return content1, content2


# 计算结合位点
def caldnaSites(AAdir, DNAdir, chainfile, cutoff, outfile1, outfile2, ):
    with open(chainfile, 'r') as inputfile:
        with open(outfile1, 'w') as outputfile1:
            with open(outfile2, 'w') as outputfile2:
                for eachname in inputfile:
                    onechain = []
                    onechain.append(eachname.strip()[0:-1])
                    onechain.append(eachname.strip()[-1])
                    #print ("calculate binding sites:", eachname)
                    proname = onechain[0] + '.rm.pdb'
                    dnaname = onechain[0] + '.dna.pdb'
                    chainID = onechain[1].strip()  # A china or B chain
                    mypdb = AAdir + '/' + proname
                    mydna = DNAdir + '/' + dnaname
                    content, content2 = caldnaDistance(mypdb, chainID, mydna, cutoff)
                    outputfile1.write(content + '\n')
                    outputfile2.write(content2)

    if os.path.exists(AAdir):
        shutil.rmtree(AAdir)
    if os.path.exists(DNAdir):
        shutil.rmtree(DNAdir)



'''
if __name__ == "__main__":
    
    pdbnamefile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/nameDouble1.txt'
    pdbdir = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/PDB/'
    removeATGC(pdbnamefile, pdbdir)
    cutoff = 5.0
    AAdir = pdbdir + "/AAdir"
    DNAdir = pdbdir + "/DNAdir"
    chainname = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/chainDouble_D1.txt'
    outfile1 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/cal_dnadouble_binding_sites_5.0.data'
    outfile2 = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/test_dnadouble_label_5.0.data'
    caldnaSites(AAdir, DNAdir, chainname, cutoff, outfile1, outfile2)

    pdbnamefile = '/ifs/gdata1/yangwenyi/PROTEIN_DNA/nameSingle.txt'
    pdbdir = '/ifs/gdata1/yangwenyi/PROTEIN_DNA/PDB100/'
    removeAUGC(pdbnamefile, pdbdir)
    cutoff = 5.0
    AAdir = pdbdir + "/AAdir"
    DNAdir = pdbdir + "/DNAdir"
    chainname = '/ifs/gdata1/yangwenyi/PROTEIN_DNA/chainSingle_D.txt'
    outfile1 = '/ifs/gdata1/yangwenyi/PROTEIN_DNA/cal_dnasingle_binding_sites_5.0.data'
    outfile2 = '/ifs/gdata1/yangwenyi/PROTEIN_DNA/test_dnasingle_label_5.0.data'
    caldnaSites(AAdir, DNAdir, chainname, cutoff, outfile1, outfile2)
'''
