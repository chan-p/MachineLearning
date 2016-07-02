# coding: utf-8
import numpy
import math
import random
# from matplotlib import pyplot

class Neural:

    # 主要コンストラクタ
    def __init__(self, n_input, n_hidden, n_output):
        self.hidden_weight = numpy.random.random_sample((n_hidden, n_input + 1))
        self.output_weight = numpy.random.random_sample((n_output, n_hidden + 1))
        self.hidden_momentum = numpy.zeros((n_hidden, n_input + 1))
        self.output_momentum = numpy.zeros((n_output, n_hidden + 1))


    # publicメソッド
    # 学習メソッド(入力ベクトル、正解ベクトル、学習率、正則係数、ループ数)
    def train(self, X, T, epsilon, mu, epoch):
        self.error = numpy.zeros(epoch)
        N = X.shape[0]
        for epo in range(epoch):
            if epo % 100 == 0:
                print "Roop:" + str(epo)
            for i in range(N):
                x = X[i, :]
                t = T[i, :]
                # 更新メソッド
                self.__update_weight(x, t, epsilon, mu)
            # 誤差算出メソッド
            self.error[epo] = self.__calc_error(X, T)
            if epo % 100 == 0:
                print self.error[epo]


    # 予測メソッド
    def predict(self, X):
        N = X.shape[0]
        C = numpy.zeros(N).astype('int')
        Y = numpy.zeros((N, X.shape[1]))
        for i in range(N):
            x = X[i, :]
            z, y = self.__forward(x)
            print y
            Y[i] = y
            C[i] = y.argmax()

        return (C, Y)

    # privateメソッド
    # シグモイドメソッド
    def __sigmoid(self, arr):
        return numpy.vectorize(lambda x: 1.0 / (1.0 + math.exp(-x)))(arr)

    # 順伝播メソッド
    def __forward(self, x):
        # z:中間層からの出力, y:出力層からの出力
        z = self.__sigmoid(self.hidden_weight.dot(numpy.r_[numpy.array([1]), x]))
        y = self.__sigmoid(self.output_weight.dot(numpy.r_[numpy.array([1]), z]))
        return (z, y)

    # 誤差逆伝播メソッド
    def __update_weight(self, x, t, epsilon, mu):
        z, y = self.__forward(x)

        # 中間-出力の重みの更新
        output_delta = (y - t) * y * (1.0 - y)
        _output_weight = self.output_weight
        self.output_weight -= epsilon * output_delta.reshape((-1, 1)) * numpy.r_[numpy.array([1]), z] - mu * self.output_momentum
        self.output_momentum = self.output_weight - _output_weight

        # 入力-中間の重みの更新
        hidden_delta = (self.output_weight[:, 1:].T.dot(output_delta)) * z * (1.0 - z)
        _hidden_weight = self.hidden_weight
        self.hidden_weight -= epsilon * hidden_delta.reshape((-1, 1)) * numpy.r_[numpy.array([1]), x]
        self.hidden_momentum = self.hidden_weight - _hidden_weight

    # 誤差算出メソッド
    def __calc_error(self, X, T):
        N = X.shape[0]
        err = 0.0
        for i in range(N):
            x = X[i, :]
            t = T[i, :]

            z, y = self.__forward(x)
            err += (y - t).dot((y - t).reshape((-1, 1))) / 5.0

        return err
