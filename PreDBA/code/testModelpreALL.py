# -*- coding: utf-8 -*-
from mlxtend.regressor import StackingRegressor
#from sklearn.linear_model import LinearRegression,Ridge,SGDRegressor
from sklearn.svm import SVR
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.model_selection import KFold
from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score,mean_absolute_error,explained_variance_score,mean_squared_error,median_absolute_error
from sklearn.model_selection import LeaveOneOut,LeavePOut
from sklearn.model_selection import ShuffleSplit,StratifiedKFold
from sklearn import preprocessing
import time
import xgboost as xgb
from sklearn.linear_model import Lasso
#single DNA
def predictModelSS(combineinfile,comparefile,outvalue):
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
        X_input=[list(map(eval, X_in))]
        #print(X_input)
        for train, test in loo.split(X):
            X_train, X_test, y_train, y_test = \
                np.array(X)[train], np.array(X)[test], np.array(y)[train], np.array(y)[test]
            #GBRT
            params = {'n_estimators': 627, 'max_depth': 2, 'min_samples_split': 6,
                      'learning_rate': 0.66, 'loss': 'ls', 'random_state': 61}
            GBRT = GradientBoostingRegressor(**params)
            # GBRT.fit(X_train, y_train)
            # y_pred = GBRT.predict(X_test)

            params2 = {'n_estimators': 905, 'booster': 'gbtree', 'objective': 'reg:gamma', 'max_depth': 10,
                       'subsample': 0.71, 'colsample_bytree': 0.67, 'min_child_weight': 1,
                       'eta': 0.01, 'seed': 500}
            # XGBmodel = xgb.XGBRegressor(**params2)
            XGBmodel = xgb.XGBRegressor(**params2)
            RF = RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=10,
                                       n_estimators=3,
                                       oob_score=False, random_state=590)
            svr_rbf = SVR(kernel='rbf', gamma=0.23, C=0.74)
            stregr = StackingRegressor(regressors=[GBRT, RF, svr_rbf], meta_regressor=XGBmodel)
            stregr.fit(X_train, y_train)
            #print(X_train)
            #print(X_input)

            y_pred = stregr.predict(X_input)
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

        outvalue=float("%.2f" %(outvalue1))*(-1)
        #print(outvalue)


        y2.append(outvalue)
        fw.write(str(outvalue) + '\n')

        print('The forecast is completed and the predicted value is' + str(outvalue))

#double I
def predictModelDI(combineinfile,comparefile,outvalue):
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
        X_input=[list(map(eval, X_in))]
        #print(X_input)
        for train, test in loo.split(X):
            X_train, X_test, y_train, y_test = \
                np.array(X)[train], np.array(X)[test], np.array(y)[train], np.array(y)[test]
            #GBRT
            params = {'n_estimators': 790, 'max_depth': 2, 'min_samples_split': 5,
                      'learning_rate': 0.46, 'loss': 'ls', 'random_state': 1}
            clf = GradientBoostingRegressor(**params)
            # clf.fit(X_train, y_train)
            # y_pred1 = clf.predict(X_test)

            params2 = {
                'n_estimators': 200, 'booster': 'gbtree', 'objective': 'reg:gamma', 'max_depth': 2,
                'subsample': 0.94, 'colsample_bytree': 0.67, 'min_child_weight': 0.94,
                'eta': 0.1, 'seed': 186, }
            model1 = xgb.XGBRegressor(**params2)
            # model1.fit(X_train, y_train)
            # y_pred=model1.predict(X_test)

            RF = RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=1,
                                       n_estimators=10,
                                       random_state=90)
            svr_rbf = SVR(kernel='rbf', gamma=1.47, C=2.62)

            stregr = StackingRegressor(regressors=[clf, RF, svr_rbf], meta_regressor=model1)
            stregr.fit(X_train, y_train)
            #print(X_train)
            #print(X_input)
            y_pred = stregr.predict(X_input)
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

        outvalue=float("%.2f" %(outvalue1))*(-1)
        #print(outvalue)


        y2.append(outvalue)
        fw.write(str(outvalue) + '\n')

        print('The forecast is completed and the predicted value is' + str(outvalue))


#double II
def predictModelDII(combineinfile,comparefile,outvalue):
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
        #print(X_in)
        #X_input = [(X_in)]
        #print(X_input)
        #X_inp=map(eval, X_in)
        #print(list(X_inp))
        X_input=[list(map(eval, X_in))]
        #print(X_input)
        for train, test in loo.split(X):
            X_train, X_test, y_train, y_test = \
                np.array(X)[train], np.array(X)[test], np.array(y)[train], np.array(y)[test]
            #GBRT
            params = {'n_estimators': 910, 'max_depth': 2, 'min_samples_split': 27,
                      'learning_rate': 0.32, 'loss': 'ls', 'random_state': 74}
            clf = GradientBoostingRegressor(**params)
            params2 = {
                'n_estimators': 201, 'booster': 'gbtree', 'objective': 'reg:gamma', 'max_depth': 4,
                'subsample': 0.62, 'colsample_bytree': 0.67, 'min_child_weight': 2.16,
                'eta': 0.01, 'seed': 543}
            model1 = xgb.XGBRegressor(**params2)

            RF = RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=6,
                                       n_estimators=6,
                                       oob_score=False, random_state=433)

            svr_rbf = SVR(kernel='rbf', gamma=0.03, C=4.72)

            stregr = StackingRegressor(regressors=[clf, RF, svr_rbf], meta_regressor=model1)
            stregr.fit(X_train, y_train)
            #print(X_train)


            y_pred = stregr.predict(X_input)
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

        outvalue=float("%.2f" %(outvalue1))*(-1)
        #print(outvalue)


        y2.append(outvalue)
        fw.write(str(outvalue) + '\n')

        print('The forecast is completed and the predicted value is' + str(outvalue))


def predictModelDIII(combineinfile,comparefile,outvalue):
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
        X_input=[list(map(eval, X_in))]
        #print(X_input)
        for train, test in loo.split(X):
            X_train, X_test, y_train, y_test = \
                np.array(X)[train], np.array(X)[test], np.array(y)[train], np.array(y)[test]
            #GBRT
            params = {'n_estimators': 300, 'max_depth': 2, 'min_samples_split': 7,
                      'learning_rate': 0.45, 'loss': 'ls', 'random_state': 1}
            clf = GradientBoostingRegressor(**params)
            # clf.fit(X_train, y_train)

            params2 = {
                'n_estimators': 992, 'booster': 'gbtree', 'objective': 'reg:gamma', 'max_depth': 3,
                'subsample': 0.88, 'colsample_bytree': 1, 'min_child_weight': 4,
                'eta': 0.1, 'seed': 652,
            }
            model1 = xgb.XGBRegressor(**params2)
            # model1.fit(X_train, y_train)
            # y_pred=model1.predict(X_test)

            RF = RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=1,
                                       n_estimators=14,
                                       random_state=335)

            svr_rbf = SVR(kernel='rbf', gamma=0.41, C=0.43)

            stregr = StackingRegressor(regressors=[clf, RF, svr_rbf], meta_regressor=model1)
            stregr.fit(X_train, y_train)
            y_pred = stregr.predict(X_input)
            #print(X_input)
            #print(y_pred)
            y1.append(y_pred)
            size=len(y1)
            #print(size)
            num = 0.0
        for i in range(size):
            num=num+float(y1[i])
        #print(num)
        outvalue1 = float(num) / float(size)*(-1)

        outvalue=float("%.2f" %(outvalue1))
        #print(outvalue)


        y2.append(outvalue)
        fw.write(str(outvalue) + '\n')

        print('The forecast is completed and the predicted value is' + str(outvalue))
def predictModelMISC(combineinfile,comparefile,outvalue):
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
        X_input=[list(map(eval, X_in))]
        #print(X_input)
        for train, test in loo.split(X):
            X_train, X_test, y_train, y_test = \
                np.array(X)[train], np.array(X)[test], np.array(y)[train], np.array(y)[test]
            #GBRT
            params = {'n_estimators': 33, 'max_depth': 2, 'min_samples_split': 9,
                      'learning_rate': 0.78, 'loss': 'ls', 'random_state': 15}
            clf = GradientBoostingRegressor(**params)

            params2 = {
                'n_estimators': 491, 'booster': 'gbtree', 'objective': 'reg:gamma', 'max_depth': 4,
                'subsample': 0.93, 'colsample_bytree': 0.01, 'min_child_weight': 0.99
                , 'eta': 0.01, 'seed': 362, }
            model1 = xgb.XGBRegressor(**params2)

            RF = RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=3,
                                       n_estimators=18, random_state=560, )

            svr_rbf = SVR(kernel='rbf', gamma=0.23, C=24)
            stregr = StackingRegressor(regressors=[clf, svr_rbf, RF], meta_regressor=model1)
            stregr.fit(X_train, y_train)


            y_pred = stregr.predict(X_input)
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

        outvalue=float("%.2f" %(outvalue1))*(-1)
        #print(outvalue)


        y2.append(outvalue)
        fw.write(str(outvalue) + '\n')

        print('The forecast is completed and the predicted value is ' + str(outvalue))
'''
if __name__ == '__main__':
    combineinfile  = 'E:/test1/combinefile.txt'
    comparefile='E:/test1/combine_RNAweight_perpbind_MFE.data'
    outvalue='E:/test1/outvalue.txt'
    params = {'n_estimators': 500, 'max_depth': 2, 'min_samples_split': 11,
              'learning_rate': 0.6, 'loss': 'ls', 'random_state': 5}
    predictModel(combineinfile, comparefile, outvalue, params)
'''