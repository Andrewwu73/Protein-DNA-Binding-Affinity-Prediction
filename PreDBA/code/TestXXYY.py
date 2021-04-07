#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def extraXXYYfea(featdir,chainfile,Xoutfile,Youtfile,perX,perY):

    fw_out1 = open(Xoutfile, 'w')
    fw_out2 = open(Youtfile,'w')
    fw_out3 = open(perX,'w')
    fw_out4 = open(perY,'w')

    with open(chainfile, 'r') as fr_chain:


        for eachchain in fr_chain:
            y = []
            chainname = eachchain.strip()
            if not chainname:
                continue
            xyname=eachchain.strip()[0:-1].upper()
            path_feat = featdir + '/' + xyname + '.data'
            with open(path_feat, 'r') as fr:
                for eachline in fr:
                    eachline = eachline.replace(',', '\t')
                    # print(eachline)
                    # print(eachline.split('\t')[-1])
                    y.append(''.join([eachline.split('\t')[-1]]))
            #print(y)
            num = len(y) - 1
            #print(num)
            num2 = 0
            num1=0
            num3=0;num4=0
            for i in range(1, len(y)):

                if y[i] == '19\n' or y[i] == '19':
                    #print(1)

                    num1 = num1 + 1
                if y[i] == '20\n' or y[i] == '20':
                    #print(2)

                    num2 = num2 + 1
            #print(num1)
            if num !=0:
                num3=(num1/num)*100
                num4=(num2/num)*100
            #print(num3)
            #print(num4)
            fw_out1.write(str(num1) + '\n')
            fw_out2.write(str(num2) + '\n')
            fw_out3.write(str('%.2f' % num3) + '\n')
            fw_out4.write(str('%.2f' % num4) + '\n')

    fw_out1.close()
    fw_out2.close()
    fw_out3.close()
    fw_out4.close()




'''

if __name__ == "__main__":
    featdir = 'E:\Protein_DNATESTPredict/123/'
    chainfile = 'E:/Protein_DNATESTPredict/chainDouble1.txt'
    Xoutfile = 'E:/Protein_DNATESTPredict/added_encode_X.data'
    Youtfile='E:/Protein_DNATESTPredict/added_encode_Y.data'
    perX='E:/Protein_DNATESTPredict/added_encode_perX.data'
    perY='E:/Protein_DNATESTPredict/added_encode_perY.data'

    extraXXYYfea(featdir, chainfile, Xoutfile,Youtfile,perX,perY)
'''