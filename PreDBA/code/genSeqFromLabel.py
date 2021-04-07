#/usr/bin/python
#_*_ coding: utf-8 _*_
import os 
'''
从格式化后的dssp文件DSSP中输出序列信息，要求序列中不含有‘X’残基，序列最短长度可人为
指定
Parameters：
    - dsspfile:为格式过的DSSP文件
    - foseq: 为输出的序列文件
    - fochain: 输出的蛋白链文件
    - minLen:  最短的序列长度
'''
def getSeqFromLabel(labelfile, outfasta, outsites):
    fw_fasta = open(outfasta, 'w')
    fw_sites = open(outsites, 'w')
    with open(labelfile, 'r') as fr_label:
        thisChain = []; preChain = []
        firstline=[]; secondline=[];thirdline = []; content1=''; content2 = ''
        for eachline in fr_label:
            oneline = eachline.split('\t') 
            thisChain = '>' + oneline[0] + ':' + oneline[1] 
            thisRes = oneline[2]
            #print (thisRes)
            if thisChain != preChain and preChain:
                firstline.append(preChain)
                content1 = ''.join(firstline)+'\n'+''.join(secondline)+'\n'
                fw_fasta.write(content1)
                content2 = content1 + ''.join(thirdline) + '\n'
                fw_sites.write(content2)
                firstline = [];secondline=[]; thirdline = []
                secondline.append(thisRes)
                label = '-'
                if oneline[4].strip() == '+1' or oneline[4].strip() == '1':
                    label = '+'
                thirdline.append(label)
            else: 
                label = '-'
                if oneline[4].strip() == '+1' or oneline[4].strip() == '1':
                    label = '+'
                secondline.append(thisRes)
                thirdline.append(label)
            preChain = thisChain
        firstline.append(preChain)
        content1 = ''.join(firstline)+'\n'+''.join(secondline)+'\n'
        fw_fasta.write(content1)
        content2 = content1 + ''.join(thirdline) + '\n'
        fw_sites.write(content2)
    fw_fasta.close()
    fw_sites.close()
###############################################################################

'''
if __name__=="__main__":
    labelfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/test_label_Double_5.0.data'
    outfasta = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/ProDoubleDNA.fasta'
    outsites = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/ProDoubleDNAsites.data'
    getSeqFromLabel(labelfile, outfasta, outsites)
    

Test sample:
python genSeqFromLabel.py \
/ifs/gdata1/yangwenyi/DATA/test5_label_5.0.data\
/ifs/gdata1/yangwenyi/DATA/test5_pseq_new.fasta \
/ifs/gdata1/yangwenyi/DATA/test5_sites_5.0_new.data \
> getSeqFromLabel_203.out 2>&1 &
'''
    