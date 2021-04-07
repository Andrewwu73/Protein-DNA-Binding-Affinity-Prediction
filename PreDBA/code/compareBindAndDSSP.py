#!/usr/bin/python
#-*-coding:utf-8-*-
import os

'''
需要的文件：
    - 根据getNewDSSP.py生成的DSSP文件
    - 根据pdb计算出来的label文件
此文件主要是为了获取一个标准的DSSP文件和一个与DSSP文件对应的类别标签文件
具体流程如下：首先updateDSSP方法是根据类别标签文件来获取DSSP文件，同时更新里面的不
标准的残基（dssp中残基为小写字母的，统一改为C；残基为X的，改为label中对应的残基）。
但经过这个文件处理之后，得到的新DSSP文件的残基个数要少于类别标签文件的残基个数，所
以，需要compareAndOutLabel这个方法将类别标签与DSSP进行对比，然后将不存dssp值的残基
去掉即可。
'''


def updateOneLineDSSP(dsspline, val):
    oneline = dsspline.split('\t')
    if oneline[4].strip() == 'X':
        oneline[4] = val
    else:
        oneline[4] = ' C'
    return '\t'.join(oneline)

'''
根据类别标签获取并更新DSSP文件
    - 遇到小写字母的残基，统一改为C，
    - 遇到X残基，改为label中对应的残基
'''
def updateDSSP(DSSP, labelfile, outdssp):
    fw_dssp = open(outdssp, 'w')
    fo_dssp = open(DSSP, 'r')
    fo_label = open(labelfile, 'r')
    fr_dssp = fo_dssp.readlines() 
    fr_label = fo_label.readlines()
    content1 = ''; content2 = ''
    for eachline in fr_dssp:
        oneline = eachline.split('\t')
        content1 = oneline[0].strip() + oneline[3].strip() + oneline[2].strip()
        flag = False; AA = '' 
        for eachlabel in fr_label:
            if not len(eachlabel.strip()):
                continue
            onelabel = eachlabel.strip().split('\t')
            content2 = onelabel[0] + onelabel[1] + onelabel[3]
            AA = onelabel[2]
            if content1 == content2:
                flag = True
                break
        updateline = eachline
        if flag == True:
            if oneline[4].strip() != AA:
                val = ' ' + onelabel[2]
                updateline = updateOneLineDSSP(eachline, val)
            fw_dssp.write(updateline)
    fw_dssp.close()
    return True

'''
将类别标签与DSSP进行对比，然后将不存dssp值的残基去掉
'''
def compareAndOutLabel(DSSP, labelfile, outfile):
    fw_label = open(outfile, 'w')
    fo_dssp = open(DSSP, 'r')
    fo_label = open(labelfile, 'r')
    fr_dssp = fo_dssp.readlines() 
    fr_label = fo_label.readlines()
    content1 = ''; content2 = ''
    step = 0; COUNT = 0
    for dsspline in fr_dssp:
        oneline = dsspline.split('\t')
        content1 = oneline[0].strip() + oneline[3].strip() + \
                    oneline[4].strip() + oneline[2].strip()
        while step < len(fr_label):
            this_label = fr_label[step]
            onelabel = this_label.split('\t')
            content2 = onelabel[0] + onelabel[1] + onelabel[2] + onelabel[3]   
            if content1 == content2:
                fw_label.write(fr_label[step])
                step +=1
                break
            else:
                COUNT += 1 
                #print (content1, '-', content2)
                step +=1
    fw_label.close()
    return True
'''
if __name__=="__main__":
    DSSP = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/DSSP/DSSP2'
    labelfile ='/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/test_label_Double_5.0.data'
    outdssp = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/DSSP/DSSP3'
    outlabel = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/Actual.binding.site_new_5.0.data'
    updateDSSP(DSSP, labelfile, outdssp)
    compareAndOutLabel(outdssp, labelfile, outlabel)
'''