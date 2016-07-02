import theano
import theano.tensor as T
import numpy as np
from sklearn.datasets import fetch_mldata
from sklearn import preprocessing
from random import *

mnist = fetch_mldata('MNIST original',data_home=".")
X_digits,_,_,t_digits = mnist.values()
data_size = 1000
index = np.arange(70000)
index = shuffle(index)[0:70000]
x_digits = X_digits[index[0:data_size]]
t_digits = t_digits[index[0:data_size]]

data_x = []

for A in x_digits:
    data_x.append(np.array([1 if x > 100 else 0 for x in A]))

lb = preprocessing.LabelBinarizer()
lb.fit([0,1,2,3,4,5,6,7,8,9])

b,c = T.dvectors("b","c")
wx,wh = T.dmatrices("wx","wh")
t,y,x,h = T.dvectors('t','y','x','h')

_wx = theano.shared(np.random.randn(196,784),name="_wx")
_wh = theano.shared(np.random.randn(10,196),name="_wh")
_b = theano.shared(np.random.randn(196),name="_b")
_c = theano.shared(np.random.randn(10),name="_c")

def sigmoid(x):
    return 1./(1+T.exp(-x))

h = sigmoid(T.dot(wx,x) + b)
y = sigmoid(T.dot(wh,h) + c)

eta = 0.01

cost_func = T.sum((t -y)**2)

grad_cost = T.grad(cost=cost_func,wrt=[wx,b,wh,c])

grad_cost_func = theano.function(inputs=[t,wh,bh,wx,bx,x],outputs=[],updates={_wx:_wx-eta*grad_cost[0],_b:_b-eta*grad_cost[1],_wh:_wh-eta*grad_cost[2],_c:_c-eta*grad_cost[3]})

train_count = 10000

for n in range(train_count):
    for x,t in zip(data_x,data_t):
        input = [t,_wh.get_value(),_bh.get_value(),_wx.get_value(),_bx.get_value(),x]
        grad_cost_func
