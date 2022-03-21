import numpy as np  # blocked in some katas

"""Matrix Addition
https://www.codewars.com/kata/526233aefd4764272800036f/python"""


def matrix_addition(a, b):
    n, m = len(a), len(a[0])
    return [[a[i][j] + b[i][j] for i in range(n)] for j in range(m)]


"""Matrix Multiplier
https://www.codewars.com/kata/573248f48e531896770001f9/python"""


def matrix_product(a, b):
    n1, m1 = len(a), len(a[0])
    n2, m2 = len(b), len(b[0])
    print(n1, m1)
    if m1 != n2:
        return -1
    else:
        return [[sum(a[i][k] * b[k][j] for k in range(m1)) for j in range(m2)] for i in range(n1)]


"""Matrix Transpose
https://www.codewars.com/kata/52fba2a9adcd10b34300094c"""


def transpose(arr):
    return [[row[i] for row in arr] for i in range(len(arr[0]))]


def transpose2(arr):
    return np.transpose(np.array(arr, dtype=object)).tolist()


"""Matrix Determinant
https://www.codewars.com/kata/52a382ee44408cea2500074c"""


def determinant(matrix):
    m = np.array(matrix)
    return round(np.linalg.det(m))


def determinant2(matrix):
    def minor(m, i, j):
        return [row[:j] + row[j + 1:] for row in m[:i] + m[i + 1:]]
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        return sum(matrix[0][i] * (-1) ** i * determinant(minor(matrix, 0, i)) for i in range(len(matrix)))


"""Matrix Trace
https://www.codewars.com/kata/55208f16ecb433c5c90001d2/python"""


def trace(matrix):
    if len(matrix) > 0 and len(matrix) == len(matrix[0]):
        return sum(matrix[i][i] for i in range(len(matrix)))


"""Rotate an array matrix
https://www.codewars.com/kata/525a566985a9a47bc8000670"""


def rotate(matrix, direction):
    if direction == 'clockwise':
        return list(map(list, zip(*matrix[::-1])))
    elif direction == 'counter-clockwise':
        return list(map(list, zip(*matrix)))[::-1]


"""matrix expanding
https://www.codewars.com/kata/5568c4ed1597b393b6000066"""


def expand(maze, fill):
    return np.pad(np.array(maze, dtype=object), len(maze) // 2, 'constant', constant_values=fill)
