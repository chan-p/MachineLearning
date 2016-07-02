import random
import numpy as np

class multi_class:

    def __generate_X(self,item):
        return np.identity(item)

    def __generate_T(self,item,dim):
        t = np.zeros((item,dim))
        for i in range(item):
            k = random.randint(0,4)
            t[i][k] = 1.0
        return t

    def __generate_AE(self,item,dim):
        t = np.zeros((item,dim))
        for i in range(item):
            for k in range(dim):
                t[i][k] = float(random.randint(0,1))
        return t

    def run_rate(self,item,dim):
        return (self.__generate_X(item),self.__generate_T(item,dim))

    def run_ae(self,item,dim):
        return self.__generate_AE(item,dim)
