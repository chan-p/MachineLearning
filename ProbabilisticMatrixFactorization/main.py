import pmf
import numpy as np

if __name__ == '__main__':

    dimension_k = 7
    alpha = 0.0001
    learn_rate = 0.05
    iteration = 100
    lambda_u = 1
    lambda_i = 1

    # test data
    test = [[0, 5, 3, 0, 1, 0, 0, 2, 2],
            [4, 1, 2, 1, 0, 2, 5, 4, 4],
            [2, 3, 2, 1, 1, 4, 0, 1, 2],
            [0, 1, 5, 5, 5, 0, 0, 4, 1],
            [5, 5, 1, 4, 3, 0, 0, 1, 2],
            [0, 5, 3, 0, 1, 0, 0, 2, 2],
            [4, 1, 2, 1, 0, 2, 5, 4, 4],
            [2, 3, 2, 1, 1, 4, 0, 1, 2],
            [0, 1, 5, 5, 5, 0, 0, 4, 1],
            [5, 5, 1, 4, 3, 0, 0, 1, 2]]

    test = np.array(test)

    mf = pmf.PMF(dimension_k, alpha, learn_rate,
                 iteration, lambda_u, lambda_i, test)
    mf.run()
