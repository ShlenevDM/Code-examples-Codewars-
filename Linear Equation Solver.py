import re

equations = ("2x-y+3x=-2y+3x+9y", "-y+x+2y=5")

# find all variables
variables = set()
for eq in equations:
    variables = variables | set(re.findall(r'[a-zA-Z]+', eq))
variables = sorted(list(variables))
# print(variables)

# verify number of equations and variables
n = len(variables)
m = len(equations)

# initialize matrices
A = [[0 for row_number in range(n)] for column_number in range(n)]
B = [0] * n


# parsing of the equation
def matrix_row(eqs):
    for row_number in range(n):
        parsed = re.split('([+=-])', equations[row_number])
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


matrix_row(equations)
print(A)
print(B)
"""def sum_coef(regex, eq):
    return sum(map(int, re.findall(regex, eq)))

# fill matrices with coefficients
for i in range(n):
    left, right = re.split(r'=', equations[i])
    B[i] = sum_coef(r'[+-]?\d+\b', right) - sum_coef(r'[+-]?\d+\b', left)

print(B)

eq = re.split('([+-])', 'x-y+3x-1')
for v in variables:
    for i in range(len(eq)):
        if v in eq[i] and eq[i - 1] == '-': print('-'+eq[i].strip(v))
        elif v in eq[i]: print(eq[i].strip(v))
    print()"""
