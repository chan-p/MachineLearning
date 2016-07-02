import random
import numpy as np

class test_case:

    def __generate_X(self,doc,dim):
        x = np.zeros((doc,dim))
        for i in range(doc):
            for j in range(dim):
                x[i][j] = float(random.randint(0,1))
        return x

    def run(self,item,dim):
        return self.__generate_X(item,dim)
