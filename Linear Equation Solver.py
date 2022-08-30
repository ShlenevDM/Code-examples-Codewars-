import re


def solve(*equations):
    """Gaussian elimination"""
    # find all variables
    variables = set()
    for eq in equations:
        variables = variables | set(re.findall(r'[a-zA-Z]+', eq))
    variables = sorted(list(variables))

    n = len(variables)
    m = len(equations)

    # initialize matrix
    A = [[0 for column_number in range(n + 1)] for row in range(m)]

    # parsing of the equation
    def parsing(eqs):
        for row_number in range(m):
            parsed = re.split('([+=-])', eqs[row_number])
            c = -1
            for i in range(len(parsed)):
                if parsed[i] == '=': c = 1
                if parsed[i].isdigit() and parsed[i - 1] == '-':
                    A[row_number][n] -= c * int(parsed[i])
                elif parsed[i].isdigit():
                    A[row_number][n] += c * int(parsed[i])
            for column_number in range(n):
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

    for i in range(n):
        try:
            if [round(el, 6) for el in A[i]] == [0] * (n + 1):
                A.remove(A[i])
                m -= 1
            elif round(A[i][i], 10) == 0:
                t = max(A[row][i] for row in range(i + 1, m))
                q = [A[row][i] for row in range(i + 1, m)].index(t)
                A[i], A[q] = A[q], A[i]
            if [round(el, 5) for el in A[i]] == [0] * (n + 1):
                A.remove(A[i])
                m -= 1
            if [round(el, 5) for el in A[i]] == [0] * (n + 1):
                A.remove(A[i])
                m -= 1

            pivot = A[i][i]
            for j in range(i + 1, m):
                c = A[j][i] / pivot
                for k in range(i, n + 1):
                    A[j][k] -= c * A[i][k]
                    A[j][k] = round(A[j][k], 10)
        except IndexError:
            pass

    if [round(el, 6) for el in A[-1]] == [0] * (n + 1):
        A.remove(A[-1])
        m -= 1
    if [round(el, 6) for el in A[-1]] == [0] * (n + 1):
        A.remove(A[-1])
        m -= 1

    if n != m:
        return

    res = dict()
    for i in range(1, n + 1):
        res[variables[-i]] = (A[-i][n] - sum(A[-i][n - j] * res[variables[-j]] for j in range(1, i))) / A[-i][n - i]

    return res