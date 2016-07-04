# -*- coding: utf-8 -*-
import test
import auto_encoder

if __name__=="__main__":

    item = 50
    num_input = 200
    testcase = test.MULTI_CLASS()
    x = testcase.run_onehot(item,num_input)

    num_hidden = 100
    iteration = 5000
    neural = auto_encoder.NeuralNet(num_input,num_hidden,x,iteration)
    neural.run()
    neural.Answer_check()
