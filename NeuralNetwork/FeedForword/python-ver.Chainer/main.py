# -*- coding: utf-8 -*-
import numpy as np
import chainer
from chainer import Function, Variable, optimizers
from chainer import Link, Chain
import chainer.functions as F
import chainer.links as L
import random

# model = Chain(layer1=L.Linear(20, 100),layer2=L.Linear(100,70),layer3=L.Linear(70, 30),layer4=L.Linear(30, 5))
model = Chain(layer1=L.Linear(50,30),layer2=L.Linear(30,5))

optimizer = optimizers.Adam()
optimizer.setup(model)

x_list = []
t_list = []

# 入力値と教師データ
a = np.identity(50)
for i in range(len(a)):
    x_data = np.array([a[i]], dtype=np.float32)
    x_list.append(x_data)
    t_data = np.array([random.randint(0,4)],dtype=np.int32) # 教師データ(クラス)
    t_list.append(t_data)

print x_list
print t_list


for i in range(1000):
    total = 0.0
    for j in range(len(x_list)):
        # print "j:" + str(j)
        x = Variable(x_list[j])
        t = Variable(t_list[j])

        optimizer.zero_grads()
        # 順伝播
        z1 = F.dropout(F.relu(model.layer1(x)))
        u2 = model.layer2(z1)
        y = F.softmax(u2)
        # z1 = F.dropout(F.relu(model.layer1(x)))
        # z2 = F.dropout(F.relu(model.layer2(z1)))
        # z3 = F.dropout(F.relu(model.layer3(z2)))
        # u4 = model.layer4(z3)
        # y = F.softmax(u4)
        # y = F.sigmoid(u4)
        if i % 100 == 0:
            print j
            print "正解："+str(t.data)
            print "出力："+str(y.data)
            print "写像："+str(u2.data)
        # 損失関数
        loss = F.softmax_cross_entropy(u2, t)
        total = loss.data
        # 誤差逆伝播
        loss.backward()
        optimizer.weight_decay(0.0005)
        optimizer.update()
    if i % 100 == 0:
        print "loss:"+str(total)
