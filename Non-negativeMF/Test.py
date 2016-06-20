import parameter
import NMF
import time
import numpy as np

def result(data,w,h):
    print "UserMatrix="
    print w
    print "ItemMatrixm="
    print h
    print "RateMatrix="
    print np.matrix(data.RateMatrix)
    print "ReMatrix="
    print np.matrix(w*h)

def run(data):
    data = parameter.Parameter()
    data.get_sample()
    w,h = NMF.factorize(data,1000)
    result(data,w,h)

if __name__=='__main__':
    start = time.time()
    data = parameter.Parameter()
    run(data)
    elaspe_time = time.time() - start
    print "RunningTime:" + str(elaspe_time)
