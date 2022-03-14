import re

equations = ("2x-y+3x-1=-2y+3x+9y+9", "-y+8+x+2y=15")

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
def equation_parsed(eq):
    left, right = eq.split('=')
    left_parsing = re.split('([+-])', left)
    right_parsing = re.split('([+-])', right)
    return left_parsing, right_parsing

print(equation_parsed('x-y+8+x+2y=15'))

"""def sum_coef(regex, eq):
    return sum(map(float, re.findall(regex, eq)))

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