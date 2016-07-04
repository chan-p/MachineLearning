# -*- coding: utf-8 -*-
import test
import feed_forword

if __name__=="__main__":

    item = 50
    testcase = test.MULTI_CLASS()
    x,t = testcase.run_onehot(item)

    num_hidden = 100
    num_output = 5
    iteration = 1000
    neural = feed_forword.NeuralNet(num_hidden,num_output,x,t,iteration,"MULTI_CLASS")
    neural.run()
    neural.Answer_check()
    neural.check_state()
