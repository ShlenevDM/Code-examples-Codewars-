import re

equations = ("x-y+3x-1=-2y+3x+9y+9", "-3y+8+2x+2y=15")

# find all variables
variables = set()
for eq in equations:
    variables = variables | set(re.findall(r'[a-zA-Z]+', eq))
variables = sorted(list(variables))
#print(variables)

# verify number of equations and variables
n = len(variables)
m = len(equations)

# initilize matrices
A = [[0]*n]*n
B = [0]*n
"""print(A)
print(B)"""

# parcing of the equation
"""def matrix_row(eqs):
    for row_number in range(n):
        parsed = re.split('([+=-])', equations[row_number])
        for column_number in range(n):
            var = variables[column_number]
            c = 1   # positive before =, negative after =
            for i in range(len(parsed)):
                if parsed[i] == '=': c = -1
                if var in parsed[i] and eq[i - 1] == '-':
                    A[row_number][column_number] -= c * int(eq[i].strip(var))
                elif var in parsed[i]:
                    A[row_number][column_number] += c * int(eq[i].strip(var))"""
def matrix_row(eqs):
    parsed = []
    for row_number in range(len(eqs)):
        parsed.append(re.split('([+=-])', eqs[row_number]))
    return parsed


print(matrix_row(equations))
#print(A)




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