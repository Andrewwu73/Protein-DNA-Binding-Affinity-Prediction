# -*- coding: utf-8 -*-
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score,mean_absolute_error,explained_variance_score,mean_squared_error,median_absolute_error
from sklearn.model_selection import LeaveOneOut,LeavePOut
from sklearn.model_selection import ShuffleSplit,StratifiedKFold

from cacul_r import cacul_r
from sklearn import preprocessing


def predictModel(combineinfile,comparefile,outvalue,params):
    fw=open(outvalue,'w')
    fc=open(combineinfile,'r')
    ft=fc.readlines()
    size=len(ft)
    fr=open(comparefile,'r')
    fileList=fr.readlines()
    X=[];y=[]
    m = len(fileList)
    for i in range(m):
        strLine=fileList[i].split('\t')
        numFeat = len(strLine)-1
        lineList=[]
        for p in range(0,numFeat):
            lineList.append(float(strLine[p]))
        X.append(lineList)
        #print (X)
        y.append(float(strLine[-1]))

    y2=[]
    loo = LeaveOneOut()
    for eachline in ft:
        y1=[]
        X_in = eachline.split('\t')
        X_input = [(X_in)]
        #print(X_input)
        for train, test in loo.split(X):
            X_train, X_test, y_train, y_test = \
                np.array(X)[train], np.array(X)[test], np.array(y)[train], np.array(y)[test]

            clf = GradientBoostingRegressor(**params)
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_input)
            #print(X_input)
            #print(y_pred)
            y1.append(y_pred)
            size=len(y1)
            #print(size)
            num = 0.0
        for i in range(size):
            num=num+float(y1[i])
        #print(num)
        outvalue1 = float(num) / float(size)

        outvalue=float("%.2f" %(outvalue1))
        #print(outvalue)


        y2.append(outvalue)
        fw.write(str(outvalue) + '\n')

        print('The forecast is completed and the predicted value is' + str(outvalue))
'''
if __name__ == '__main__':
    combineinfile  = 'E:/test1/combinefile.txt'
    comparefile='E:/test1/combine_RNAweight_perpbind_MFE.data'
    outvalue='E:/test1/outvalue.txt'
    params = {'n_estimators': 500, 'max_depth': 2, 'min_samples_split': 11,
              'learning_rate': 0.6, 'loss': 'ls', 'random_state': 5}
    predictModel(combineinfile, comparefile, outvalue, params)
'''