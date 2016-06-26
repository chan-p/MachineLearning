from ff import *
from test import *
import random

if __name__ == '__main__':

    item_num = 5
    class_num = 5
    data = multi_class()
    X,T = data.run(item_num,class_num)

    N = X.shape[0]
    input_size = X.shape[1]
    hidden_size = 10
    output_size = class_num
    epsilon = 0.1
    mu = 0.5
    epoch = 1000

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
