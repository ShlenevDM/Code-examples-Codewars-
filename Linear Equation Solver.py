"""https://www.codewars.com/kata/56d6d927c9ae3f115b0008dd
NumPy is disabled for this kata"""


import re


def solve(*equations):
    """Gaussian elimination"""
    # find all variables
    variables = set()
    for eq in equations:
        variables = variables | set(re.findall(r'[a-zA-Z]+', eq))
    variables = sorted(list(variables))

    m = len(variables)
    n = len(equations)

    # initialize matrix
    A = [[0 for column_number in range(m + 1)] for row in range(n)]

    # parsing of the equation
    def parsing(eqs):
        for row_number in range(n):
            parsed = re.split('([+=-])', eqs[row_number])
            c = -1
            for i in range(len(parsed)):
                if parsed[i] == '=': c = 1
                if parsed[i].isdigit() and parsed[i - 1] == '-':
                    A[row_number][m] -= c * int(parsed[i])
                elif parsed[i].isdigit():
                    A[row_number][m] += c * int(parsed[i])
            for column_number in range(m):
                var = variables[column_number]
                c = 1  # positive before =, negative after =
                for i in range(len(parsed)):
                    if parsed[i] == '=': c = -1
                    if var == parsed[i].strip('0123456789') and parsed[i - 1] == '-':
                        a = parsed[i].strip(var) or 1
                        A[row_number][column_number] -= c * int(a)
                    elif var == parsed[i].strip('0123456789'):
                        a = parsed[i].strip(var) or 1
                        A[row_number][column_number] += c * int(a)

    parsing(equations)  # fill the matrix with coefficients

    # row echelon
    eps = 10 ** -6
    for i in range(min(n, m)):
        rest = [t[i] for t in A[i:]]
        q = max(rest, key=abs)
        s = i + rest.index(q)
        A[i], A[s] = A[s], A[i]

        if abs(A[i][i]) < eps:
            return

        pivot = A[i][i]

        for r in A[i + 1:]:
            c = r[i] / pivot
            for k in range(i, m + 1):
                r[k] -= c * A[i][k]

    # remove zero rows at the end
    for row in A[min(n, m):]:
        if abs(row[-1]) > eps:
            return
        else:
            A.remove(row)
            n -= 1

    # check if system is solvable
    if m != n:
        return

    res = dict()
    for i in range(1, m + 1):
        res[variables[-i]] = (A[-i][m] - sum(A[-i][m - j] * res[variables[-j]] for j in range(1, i))) / A[-i][m - i]

    return res