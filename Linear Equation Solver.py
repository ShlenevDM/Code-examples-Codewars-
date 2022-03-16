import re

equations = ("2x-y+3x=-2y+3x+9y", "-y+x+2y=5")

# find all variables
variables = set()
for eq in equations:
    variables = variables | set(re.findall(r'[a-zA-Z]+', eq))
variables = sorted(list(variables))

# verify number of equations and variables
n = len(variables)
m = len(equations)

# initialize matrices
A = [[0 for row_number in range(n)] for column_number in range(n)]
B = [0] * n


# parsing of the equation
def matrix_row(eqs):
    for row_number in range(n):
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


matrix_row(equations)  # not to forget to call this function

# minor
def minor(m, i, j):
    return [row[:j] + row[j + 1:] for row in m[:i] + m[i + 1:]]


# det
def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        return sum(matrix[0][i] *(-1) ** i * det(minor(matrix, 0, i)) for i in range(len(matrix)))

