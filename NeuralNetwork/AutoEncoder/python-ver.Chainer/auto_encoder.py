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
    #主要コンストラクタ
    def __init__(self,num_input,num_hidden,Vec_input,ite,task = "None"):
        if len(Vec_input) > 0:
            self.Vec_input = Vec_input
            self.Vec_correct = Vec_input
            self.num_input = num_input
            self.num_output = num_input
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

        if ite > 0:
            self.iteration = ite
        else:
            print "-----------------------------------"
            sys.stderr.write("Number of Iteration is Error!")
            print
            print "-----------------------------------"
            return

        if task == "None":
            self.task = "None"
            print "---Auto Encoder Start---"
        elif task == "Denoise":
            self.task = "Denoise"
            print "---Denoising Auto Encoder Start---"
        else:
            print "-----------------------------------"
            sys.stderr.write("Type of Auto Encoder is Error!")
            print
            print "-----------------------------------"
            return

    # privateメソッド
     # モデル構築：三層パーセプトロン
    def __get_model(self):
        self.model =  Chain(Hidden_Layer=L.Linear(self.num_input,self.num_hidden),Output_Layer=L.Linear(self.num_hidden,self.num_output))

     # 最適化アルゴリズム：Adam
    def __get_optimizer(self):
        self.optimizer = optimizers.Adam()
        self.optimizer.setup(self.model)

     # データ変換：辞書{アイテムint,ベクトルリスト[]}→辞書{アイテムint,ベクトルnumpy配列array[]}
    def __get_data(self):
        self.x_dic = {}
        for key,value in self.Vec_input.items():
            self.x_dic[key] = np.array([np.array(value,dtype=np.float32)],dtype=np.float32)

     # データ変換：Variable型
    def __change_data(self,key):
        return Variable(self.x_dic[key])

    # Decodeメソッド
     # 活性化鑵子：シグモイド
    def __Decode(self,u1):
        h = F.dropout(F.relu(u1))
        u2 = self.model.Output_Layer(h)
        return F.sigmoid(u2)

     # 損失メソッド
     # 損失関数：二乗誤差
    def __LossFunction(self,t,y):
        return F.mean_squared_error(y,t)

     # 誤差逆伝播メソッド
    def __BackPropagation(self):
         # 勾配計算
        self.loss.backward()
         # 学習率設定
        self.optimizer.weight_decay(0.0001)
         # パラメーター更新
        self.optimizer.update()

     # 平均二乗誤差メソッド
    def __RMSE(self,roop,total):
        print "Roop:" + str(roop)
        print "RMSE:" + str(math.sqrt(total/len(self.Vec_input)))

    # publicメソッド
     # Encodeメソッド
      # 活性化関数：relu
    def Encode(self,x):
        if self.task == "None":
            return self.model.Hidden_Layer(x)
        elif self.task == "Denoise":
            return self.model.Hidden_Layer(F.dropout(x))

     # 出力結果確認メソッド
    def Answer_check(self):
        for key,value in self.x_dic.items():
            print "Item Number:" + str(key)
            x = self.__change_data(key)
            print "Output:" + str(self.__Decode(self.Encode(x)).data)
            print "Correct:" + str(self.x_dic[key])
            print "Encode:" + str(self.Encode(x).data)

    def check_state(self):
        if self.task == "None":
            print "Auto Encoder"
        elif self.task == "Denoise":
            print "Denoising Auto Encoder"
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
            for key,value in self.x_dic.items():
                x = self.__change_data(key)
                # 勾配初期化
                self.optimizer.zero_grads()
                # Encode
                u1 = self.Encode(x)
                # Decode
                y =self.__Decode(u1)
                # 損失関数
                self.loss = self.__LossFunction(x,y)
                total += pow(self.loss.data,2)
                # 誤差逆伝搬
                self.__BackPropagation()
            if roop % 100 == 0:
                self.__RMSE(roop,total)
