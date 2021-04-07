#/usr/bin/python
#_*_ coding: utf-8 _*_
import os 

def getdnaSeqFromLabel(labelfile, outfasta, outsites):
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
    labelfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/test_dnadouble_label_5.0.data'
    outfasta = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/test_dna_seq_new.fasta'
    outsites = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/test_dna_sites_5.0_new.data'
    getrnaSeqFromLabel(labelfile, outfasta, outsites)

Test sample:
python genSeqFromLabel.py \
/ifs/gdata1/yangwenyi/DATA/test5_label_5.0.data\
/ifs/gdata1/yangwenyi/DATA/test5_pseq_new.fasta \
/ifs/gdata1/yangwenyi/DATA/test5_sites_5.0_new.data \
> getSeqFromLabel_203.out 2>&1 &
'''
    