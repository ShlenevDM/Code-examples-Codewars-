import re
equations = "x+y=7z-1", "6x+z=-3y", "4y+10z=-8x"


# find all variables
variables = set()
for eq in equations:
    variables = variables | set(re.findall(r'[a-zA-Z]+', eq))
variables = sorted(list(variables))

n = len(variables)
m = len(equations)
#print(n, m)

# initialize the matrix
A = [[0 for column_number in range(n + 1)] for row in range(m)]

for row_number in range(m):
    parsed = re.split('([+=-])', equations[row_number])
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
            if var in parsed[i] and parsed[i - 1] == '-':
                a = parsed[i].strip(var) or 1
                A[row_number][column_number] -= c * int(a)
            elif var in parsed[i]:
                a = parsed[i].strip(var) or 1
                A[row_number][column_number] += c * int(a)

print(A)

D = []

for column_number in range(n):
    a = max(A[row_number][column_number] for row_number in range(len(A)))
    i = [A[row_number][column_number] for row_number in range(len(A))].index(a)
    #for j in range(n + 1): A[i][j] /= a
    D.append(A.pop(i))

for row in D: print(row)

for row in D:
    pass



