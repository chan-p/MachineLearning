# -*- coding: utf-8 -*-
import random

class MULTI_CLASS:

    def __generate_X(self,item):
        x = {}
        for i in range(item):
            x[i] = []
            for j in range(item):
                if i == j:
                    x[i].append(1)
                else:
                    x[i].append(0)
        return x

    def __generate_T(self,item):
        t = {}
        for i in range(item):
            t[i] = random.randint(0,4)
        return t

    def run_onehot(self,item):
        return (self.__generate_X(item),self.__generate_T(item))
