# -*- coding: utf-8 -*-
import numpy as np
from numpy.matrixlib.defmatrix import matrix
import random
import parameter

#caluculate total error of (RateMatrix - ReMatrix)
def difcost(a, b):
    dif = 0.0
    for i in range(np.matrix(a).shape[0]):
        for j in range(np.matrix(a).shape[1]):
            dif += pow(a[i][j] - b[i,j],2)
    print "TotalError" + str(dif)

#factorizing RateMatrix to UserMatrix and ItemMatrix
def factorize(data,iter):
    ic = np.matrix(data.RateMatrix).shape[0]
    fc = np.matrix(data.RateMatrix).shape[1]
    for i in range(iter):
        wh = data.UserMatrix * data.ItemMatrix
        if (i % 100) == 0:
            print "Iteration:" + str(i  Test.py                      |  9     dif = 0.0
                    )
            difcost(data.RateMatrix,wh)
        v = np.matrix(data.RateMatrix)
        hn = (data.UserMatrix.transpose() * v)
        hd = (data.UserMatrix.transpose() * data.UserMatrix * data.ItemMatrix)
        data.ItemMatrix = np.matrix(np.array(data.ItemMatrix)*np.array(hn)/np.array(hd))
        wn = (v * data.ItemMatrix.transpose())
        wd = data.UserMatrix * data.ItemMatrix * data.ItemMatrix.transpose()
        data.UserMatrix = np.matrix(np.array(data.UserMatrix)*np.array(wn)/np.array(wd))
    return data.UserMatrix,data.ItemMatrix

