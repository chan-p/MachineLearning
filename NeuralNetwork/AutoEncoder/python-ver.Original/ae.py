# coding: utf-8
import theano as t
import numpy as np
import math
import random
from test import *

class AutoEncoder:

    #主要コンストラクタ
    def __init__(self,num_input,num_hidden):
        self.weight1 = np.random.random_sample((num_hidden,num_input + 1))
        self.weight2 = np.random.random_sample((num_input,num_hidden + 1))

    #publicメソッド
    #学習メソッド
    def train(self,X,e,epoch):
        self.error = np.zeros(epoch)
        N = X.shape[0]
        for epo in range(epoch):
            if epo % 100 == 0:
                print "Roop:" + str(epo)
            for i in range(N):
                x = X[i, :]
                #更新メソッド
                self.__update_weight(x,e)
            #誤差算出メソッド
            self.error[epo] = self.__calcE(X)
            if epo % 100 == 0:
                print self.error[epo]

    def predict(self,X):
        N = X.shape[0]
        C = np.zeros(N).astype('int')
        Y = np.zeros((N,X.shape[1]))
        for i in range(N):
            x = X[i, :]
            z = self.encode(x)
            y = self.__decode(z)
            Y[i] = y
            C[i] = y.argmax()
        return (C,Y)

   #privateメソッド
    # シグモイドメソッド
    def __sigmoid(self,arr):
        return np.vectorize(lambda x: 1.0 / (1.0 + math.exp(-x)))(arr)

    # encodeメソッド
    def encode(self,x):
        return self.__sigmoid(self.weight1.dot(np.r_[np.array([1]), x]))

    # decodeメソッド
    def __decode(self,y):
        return self.__sigmoid(self.weight2.dot(np.r_[np.array([1]), y]))

    # 誤差逆伝播メソッド
    def __update_weight(self, x,epsilon):
        z = self.encode(x)
        y = self.__decode(z)

        #中間-出力の重みの更新
        output_delta = (y - x) * y * (1.0 - y)
        self.weight2 -= epsilon * output_delta.reshape((-1, 1)) * np.r_[np.array([1]), z]

        #入力-中間の重みの更新
        hidden_delta = (self.weight2[:, 1:].T.dot(output_delta)) * z * (1.0 - z)
        self.weight1 -= epsilon * hidden_delta.reshape((-1, 1)) * np.r_[np.array([1]), x]

    #誤差算出メソッド
    def __calcE(self, X):
        N = X.shape[0]
        err = 0.0
        for i in range(N):
            x = X[i, :]
            z = self.encode(x)
            y = self.__decode(z)
            err += (y - x).dot((y - x).reshape((-1, 1))) / x.shape
        return err



if __name__=="__main__":
    item_num = 20
    dim = 100
    data = test_case()
    X = data.run(item_num,dim)

    N = X.shape[0]
    input_size = X.shape[1]
    hidden_size = 50
    epsilon = 0.001
    epoch = 10000

    ae = AutoEncoder(dim, hidden_size)
    ae.train(X, epsilon, epoch)
    # nn.error_graph()

    C, Y = ae.predict(X)

    for i in range(N):
        x = X[i, :]
        y = Y[i, :]
        c = C[i]

        print "item:",
        print i
        print "x:"
        print x
        print "y:"
        print y
        print "encode"
        print ae.encode(x)
        print ","
