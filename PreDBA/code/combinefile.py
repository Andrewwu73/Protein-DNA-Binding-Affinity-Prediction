#!/usr/bin/python
#-*- coding: utf-8 -*-

import os

def combine_feature(filelist, outfile):
    content = []
    with open(outfile, 'w') as fw_out:
        fr_file1 = open(filelist[0], 'r')
        content = fr_file1.readlines()
        for i in range(1, len(filelist)):
            if not os.path.exists(filelist[i]):
                continue
            with open(filelist[i], 'r') as fo_file:
                temp_file = fo_file.readlines()
                #print (i, '=', len(temp_file[0].split('\t')))
                for j in range(len(temp_file)):
                    content[j] = content[j].strip() + '\t' + temp_file[j]
        fw_out.write(''.join(content))
        fr_file1.close()
    return content

def combinefile1(featdir, outfile, felem):
    filelist = []
    #filelist.append(label)
    for i in range(len(felem)):
        featfile = featdir + '/added_encode_' + felem[i] + '.data'
        filelist.append(featfile)
    #print (filelist)
    import combine_feature as cmbfeat
    cmbfeat.combine_feature(filelist, outfile)       
    



'''
if __name__=="__main__":
    feat_elem = ['RNAweight','weight','perpbind','rasa','percWW']
    featdir = 'E:/test combine code/meagerdfea'
    label = 'E:/test combine code/test_label_5.0.data'
    outfile = 'E:/test combine code/combine_ab_label.data'
    felem = feat_elem
    combinefile(featdir, outfile, felem)
'''







