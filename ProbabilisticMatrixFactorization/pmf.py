import numpy as np
import math

from numpy.random import normal


class PMF:
    def __init__(self, k, alpha, learn_rate, iteration, lambda_u, lambda_i, R):
        self.dimension_k = k
        self.alpha = alpha
        self.learn_rate = learn_rate
        self.iteration = iteration
        self.l_u = lambda_u
        self.l_i = lambda_i
        self.R = R

    def _loss(self, U, V):
        total_loss = 0.
        count = 0.
        for index_tuple, value in np.ndenumerate(self.R):
            if value == 0:
                continue
            count += 1.
            total_loss += pow(value - np.dot(U[index_tuple[0]],
                                             V[index_tuple[1]]), 2)
        return math.sqrt(total_loss/count)

    def _get_init_matrix(self, num_user, num_item):
        # normal(ave=0,dispersion=1,size(line,row))
        return (np.array(normal(0, 1/self.l_u,
                                size=(num_user, self.dimension_k))),
                np.array(normal(0, 1/self.l_i,
                                size=(num_item, self.dimension_k))))

    def _sgd(self, u, v, ite):
        U = u
        V = v
        alpha = self.alpha
        for index_tuple, value in np.ndenumerate(self.R):
            if value == 0:
                continue
            i = index_tuple[0]
            j = index_tuple[1]
            error = -(value - np.dot(U[i], V[j]))

            Uold = U[i]
            U[i] = U[i] - self.learn_rate * (error * V[j] + alpha * U[i])
            V[j] = V[j] - self.learn_rate * (error * Uold + alpha * V[j])

        return U, V

    def fit(self, user_matrix, item_matrix):
        U = user_matrix
        V = item_matrix
        for ite in xrange(self.iteration):
            U, V = self._sgd(U, V, ite)
            if ite % 10 == 0:
                print self._loss(U, V)

    def run(self):
        num_user = len(self.R)
        num_item = len(self.R)
        U, V = self._get_init_matrix(num_user, num_item)

        self.fit(U, V)

