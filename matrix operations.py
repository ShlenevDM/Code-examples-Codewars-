def matrix_addition(a, b):
    n, m = len(a), len(a[0])
    return [[a[i][j] + b[i][j] for i in range(n)] for j in range(m)]


def matrix_product(a, b):
    n1, m1 = len(a), len(a[0])
    n2, m2 = len(b), len(b[0])
    print(n1, m1)
    if m1 != n2:
        return -1
    else:
        return [[sum(a[i][k] * b[k][j] for k in range(m1)) for j in range(m2)] for i in range(n1)]

print(matrix_product([[7, 3], [2, 5], [6, 8], [9, 0]], [[7, 4, 9], [8, 1, 5]]))