import numpy as np
import random
from sklearn.datasets.mldata import fetch_mldata
from sklearn.externals import joblib
import os
from sklearn.metrics import roc_auc_score
from itertools import product

# load data
def loadDataSet(fileName):
    fr = open(fileName, 'r')
    dataMat = []; labelMat = []
    for eachline in fr:
        lineArr = []
        curLine = eachline.strip().split(' ')  
        for i in range(len(curLine)-1):         
            lineArr.append(float(curLine[i]))   
        dataMat.append(lineArr)
        labelMat.append(int(curLine[-1]))      
    fr.close()
    labelMat = np.array(labelMat)
    dataMat = np.array(dataMat)
    return dataMat, labelMat

def testClf(modeldir, test_X, test_y, Name, resultdir = "PredictResults"):
    if not os.path.exists(resultdir):
        os.mkdir(resultdir)
    # test classifier with testsets 
    predict_y = []
    Probas = np.mat(np.zeros((len(test_y),1)))
    i =1
    clf = joblib.load(modeldir + '/clf_' + str(i) + '.model')
    predict_ = clf.predict(test_X) #return type is float64
    proba = clf.predict_proba(test_X) #return type is float64
    #print proba
    np.savetxt(resultdir + "/"+ Name + "_proba.data",\
	proba,fmt="%f", delimiter="\t")
    proba_each = []
    for i in range(len(Probas)):
        Probas[i] += proba[i][1]
        proba_each.append(proba[i][1])

if __name__ == '__main__':
    model = os.sys.argv[1]
    IndepTest = os.sys.argv[2]
    File = os.sys.argv[3]
    Name = os.sys.argv[4]
    os.chdir(File)
    indeptest_x, indeptest_y = loadDataSet(IndepTest)
    testClf(model, indeptest_x, indeptest_y, Name)