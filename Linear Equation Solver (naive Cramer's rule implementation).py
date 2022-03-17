"""numpy, copy are disabled
this is a working algorithm, although it's to slow because of enormous complexity of calculation of
determinant for big systems, so it times out on actual tests"""


import re


# emulate deepcopy
def deepcopy(a):
    return a if not isinstance(a, list) else list(map(deepcopy, a))


def minor(m, i, j):
    return [row[:j] + row[j + 1:] for row in m[:i] + m[i + 1:]]


def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        return sum(matrix[0][i] * (-1) ** i * det(minor(matrix, 0, i)) for i in range(len(matrix)))


def solve(equations):
    # quick fix for one string equations, doubled equation will be deleted later
    if isinstance(equations, str):
        equations = [equations for _ in range(2)]

    # find all variables
    variables = set()
    for eq in equations:
        variables = variables | set(re.findall(r'[a-zA-Z]+', eq))
    variables = sorted(list(variables))

    n = len(variables)
    m = len(equations)
    # verify that system is solvable
    if m > n:
        return

    # initialize matrices
    A = [[0 for column_number in range(n)] for row in range(m)]
    B = [0] * m

    # parsing of the equation
    def matrix_row(eqs):
        for row_number in range(m):
            parsed = re.split('([+=-])', eqs[row_number])
            c = 1
            for i in range(len(parsed)):
                if parsed[i].isdigit() and parsed[i - 1] == '-':
                    B[row_number] -= c * int(parsed[i])
                elif parsed[i].isdigit():
                    B[row_number] += c * int(parsed[i])
            for column_number in range(n):
                var = variables[column_number]
                c = 1  # positive before =, negative after =
                for i in range(len(parsed)):
                    if parsed[i] == '=': c = -1
                    if var in parsed[i] and parsed[i - 1] == '-':
                        a = parsed[i].strip(var) or 1
                        A[row_number][column_number] -= c * int(a)
                    elif var in parsed[i]:
                        a = parsed[i].strip(var) or 1
                        A[row_number][column_number] += c * int(a)

    matrix_row(equations)  # fill the matrix with coefficients

    # delete repeated equations
    if m > n:
        A_B = [A[i] + [B[i]] for i in range(m)]
        for i in range(m):
            for j in range(n + 1):
                if A_B[i][j] == 0:
                    continue
                else:
                    b = A_B[i][j]
                    break
            for j in range(n + 1):
                A_B[i][j] /= b

        i = 0
        while i < m:
            if A_B.count(A_B[i]) > 1:
                A.remove(A[i])
                B.remove(B[i])
                A_B.remove(A_B[i])
                m -= 1
            else:
                i += 1
        n = len(variables)
        m = len(equations)

    # Cramer's Rule
    d = det(A)
    if d == 0:
        return
    res = {}
    for column_number in range(n):
        AB = deepcopy(A)
        for row_number in range(n):
            AB[row_number][column_number] = B[row_number]
        res[variables[column_number]] = det(AB) / d

    return res

equations = "x+y=7z-1", "6x+z=-3y", "4y+10z=-8x"
print(solve(equations))
