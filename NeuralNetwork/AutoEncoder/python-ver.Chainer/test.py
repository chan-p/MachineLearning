# -*- coding: utf-8 -*-
import random

class MULTI_CLASS:

    def __generate_X(self,item,num_input):
        x = {}
        for i in range(item):
            x[i] = []
            for j in range(num_input):
                x[i].append(random.randint(0,1))
        return x

    def run_onehot(self,item,num_input):
        return self.__generate_X(item,num_input)
