#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
根据蛋白质链从DSSP文件中获取固定的DSSP文件
'''
import os    


#extract dssp from old dssp file 
def extractDSSP(dsspfile, chainfile, outfile):
    fw_dssp = open(outfile, 'w')
    fo_chain = open(chainfile,'r')
    fr_chain = fo_chain.readlines()
    with open(dsspfile, 'r') as  fo_dssp:  
        for eachline in fo_dssp:
            oneline = eachline.split('\t')
            for eachchain in fr_chain:
                pname = eachchain.strip()[0:-1]
                chain_id = eachchain.strip()[-1]
                if oneline[0].strip() == pname and oneline[3].strip() == chain_id:
                    fw_dssp.write(eachline)
                    break
    fo_chain.close()
    fw_dssp.close()
    
    
def extractDSSP2(dsspfile, chainfile, outfile):
    fw_dssp = open(outfile, 'w')
    fo_dssp = open(dsspfile,'r')
    fr_dssp = fo_dssp.readlines()
    with open(chainfile, 'r') as  fr_chain:  
        #print chainfile
        for eachchain in fr_chain:
            pname = eachchain.strip()[0:-1]
            chain_id = eachchain.strip()[-1]
            for eachline in fr_dssp:
                oneline = eachline.split('\t')
                if oneline[0].strip() == pname and oneline[3].strip() == chain_id:
                    fw_dssp.write(eachline)
    fo_dssp.close()
    fw_dssp.close()
'''
if __name__=="__main__":
    dsspfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/DSSP/dssp/DSSP'
    chainfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/chainDouble1.txt'
    outfile = '/ifs/gdata1/yangwenyi/Protein_DNANEW/Double/ClassI/DSSP/DSSP2'
    extractDSSP2(dsspfile, chainfile, outfile)
'''

