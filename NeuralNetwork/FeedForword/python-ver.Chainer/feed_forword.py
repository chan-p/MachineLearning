# -*- coding: utf-8 -*-
import numpy as np
import chainer
from chainer import Function, Variable, optimizers
from chainer import Link, Chain
import chainer.functions as F
import chainer.links as L
import random
import traceback
import sys
import math


class NeuralNet:
    # 主要コンストラクタ

    def __init__(self, num_hidden, num_out, Vec_input, Vec_Correct, ite, task):
        if len(Vec_input) > 0:
            self.Vec_input = Vec_input
            self.num_input = len(Vec_input[0])
        else:
            print "-----------------------------------"
            sys.stderr.write("Input Vectol is Empty!")
            print
            print "-----------------------------------"
            return

        if num_hidden > 0:
            self.num_hidden = num_hidden
        else:
            print "-----------------------------------"
            sys.stderr.write("Number of Hidden unit is Error!")
            print
            print "-----------------------------------"
            return

        if num_out > 0:
            self.num_out = num_out
        else:
            print "-----------------------------------"
            sys.stderr.write("Number of Output unit is Error!")
            print
            print "-----------------------------------"
            return

        if task == "MULTI_CLASS":
            self.task = "MULTI_CLASS"
        elif task == "MULTI_LABEL":
            self.task = "MULTI_LABEL"
        else:
            print "-----------------------------------"
            sys.stderr.write("A Name of Task is Error!")
            print
            print "-----------------------------------"
            return

        if len(Vec_input) == len(Vec_Correct):
            for key, value in Vec_Correct.items():
                if key not in Vec_input:
                    print "-----------------------------------"
                    sys.stderr.write(
                        "Correct Vectol contains different Item Number!")
                    print
                    print "-----------------------------------"
                    return
                if 0 >= value and value > self.num_out:
                    print "-----------------------------------"
                    sys.stderr.write("Correct Value Value is not correct!")
                    print
                    print "-----------------------------------"
                    return
            self.Vec_correct = Vec_Correct
        else:
            print "-----------------------------------"
            sys.stderr.write("Input Vectol is Empty!")
            print
            print "-----------------------------------"
            return

        if ite > 0:
            self.iteration = ite
        else:
            print "-----------------------------------"
            sys.stderr.write("Number of Iteration is Error!")
            print
            print "-----------------------------------"
            return

    # privateメソッド
     # モデル構築：三層パーセプトロン
    def __get_model(self):
        self.model = Chain(Hidden_Layer=L.Linear(
            self.num_input, self.num_hidden), Output_Layer=L.Linear(self.num_hidden, self.num_out))

     # 最適化アルゴリズム：Adam
    def __get_optimizer(self):
        self.optimizer = optimizers.Adam()
        self.optimizer.setup(self.model)

     # データ変換：辞書{アイテムint,ベクトルリスト[]}→辞書{アイテムint,ベクトルnumpy配列array[]}
    def __get_data(self):
        self.x_dic = {}
        self.t_dic = {}
        for key, value in self.Vec_input.items():
            self.x_dic[key] = np.array(
                [np.array(value, dtype=np.float32)], dtype=np.float32)
            self.t_dic[key] = np.array([self.Vec_correct[key]], dtype=np.int32)

     # データ変換：Variable型
    def __change_data(self, key):
        return (Variable(self.x_dic[key]), Variable(self.t_dic[key]))

     # 順伝播メソッド
     # 活性化関数：relu
    def __FeedForword(self, x):
        u1 = self.model.Hidden_Layer(x)
        h = F.dropout(F.relu(u1))
        return self.model.Output_Layer(h)

     # 活性化メソッド
     # 活性化関数：
      # 多クラス分類：ソフトマックス関数
      # 多値ラベル：シグモイド関数
    def __Activate(self, u2):
        if self.task == "MULTI_CLASS":
            return F.softmax(u2)
        elif self.task == "MULTI_LABEL":
            return F.sigmoid(u2)

     # 損失メソッド
     # 損失関数
      # 多クラス分類：交差エントロピー
      # 多値ラベル：二乗誤差
    def __LossFunction(self, u2, t, y):
        if self.task == "MULTI_CLASS":
            return F.softmax_cross_entropy(u2, t)
        elif self.task == "MULTI_LABEL":
            return F.mean_squared_error(y, t)

     # 誤差逆伝播メソッド
    def __BackPropagation(self):
         # 勾配計算
        self.loss.backward()
        # 学習率設定
        self.optimizer.weight_decay(0.0005)
        # パラメーター更新
        self.optimizer.update()

     # 平均二乗誤差メソッド
    def __RMSE(self, roop, total):
        print "Roop:" + str(roop)
        print "RMSE:" + str(math.sqrt(total / len(self.Vec_input)))

    # publicメソッド
     # 出力結果確認メソッド
    def Answer_check(self):
        for key, value in self.x_dic.items():
            print "Item Number:" + str(key)
            x, t = self.__change_data(key)
            print "Output:" + str(self.__Activate(u2=self.__FeedForword(x)).data)
            print "Class:" + str(np.argmax(self.__Activate(u2=self.__FeedForword(x)).data[0]))
            print "Correct:" + str(self.t_dic[key])

    def check_state(self):
        print "Feed Forword Neural Network"
        if self.task == "MULTI_CLASS":
            print "Type of Task:MULTI_CLASS"
        elif self.task == "MULTI_LABEL":
            print "Type of Task:MULTI_LABEL"
        print "Number of Item:" + str(self.num_input)
        print "Number of Input Units:" + str(self.num_input)
        print "Number of Hidden Units:" + str(self.num_hidden)
        print "Number of Output Units:" + str(self.num_output)

     # 実行メソッド
    def run(self):
        self.__get_model()
        self.__get_optimizer()
        self.__get_data()

        for roop in range(self.iteration):
            total = 0.0
            for key, value in self.x_dic.items():
                x, t = self.__change_data(key)
                # 勾配初期化
                self.optimizer.zero_grads()
                # 順伝播
                u2 = self.__FeedForword(x)
                # 活性化
                y = self.__Activate(u2)
                # 損失関数
                self.loss = self.__LossFunction(u2, t, y)
                total += pow(self.loss.data, 2)
                # 誤差逆殿番
                self.__BackPropagation()
            if roop % 100 == 0:
                self.__RMSE(roop, total)
