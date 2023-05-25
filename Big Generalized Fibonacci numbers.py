"""https://www.codewars.com/kata/5d7bb3eda58b36000fcc0bbb/python"""

import numpy as np


def generalized_fibonacchi(a, b, n):
    x = len(a)
    if n < x:
        return a[n]
    else:
        Z = np.diag(np.ones(x - 1, dtype=object), k=1)
        Z[-1, :] = np.array(list(reversed(b)), dtype=object)
        return np.linalg.matrix_power(Z, n).dot(np.array(a))[0]


assert generalized_fibonacchi([-1, 3, -2], [2, 2, -2], 17) == 195328
