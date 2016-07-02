from feed_forword import *
from test import *
import random

if __name__ == '__main__':

    item_num = 10
    class_num = 5
    dim = 20
    data = multi_class()
    X,T = data.run_rate(item_num,class_num)
    # X = data.run_ae(item_num,dim)
    T = X

    N = X.shape[0]
    input_size = X.shape[1]
    hidden_size = 5
    output_size = class_num
    # output_size = dim
    epsilon = 0.01
    mu = 0.5
    epoch = 10000

    nn = Neural(input_size, hidden_size, output_size)
    nn.train(X, T, epsilon, mu, epoch)
    # nn.error_graph()

    C, Y = nn.predict(X)

    for i in range(N):
        x = X[i, :]
        y = Y[i, :]
        t = T[i, :]
        c = C[i]

        print "item:",
        print i
        print "x:"
        print x
        print "y:"
        print y
        print "t:"
        print t
        print "c:",
        print c
        print ","
