import re
equations = "x+y=7z-1", "6x+z=-3y", "4y+1z=-8x"


# find all variables
variables = set()
for eq in equations:
    variables = variables | set(re.findall(r'[a-zA-Z]+', eq))
variables = sorted(list(variables))

n = len(variables)
m = len(equations)
#print(n, m)

# initialize the matrix
A = [[0 for col in range(n)] for row in range(m)]
B = [0] * m

for row_number in range(m):
    parsed = re.split('([+=-])', equations[row_number])
    c = -1
    for i in range(len(parsed)):
        if parsed[i] == '=': c = 1
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

print('A: ')
for row in A:
    print(row)
print()
print('B:', B)

for col in range(n):
    a = max(abs(A[row][col]) for row in range(col, m))
    i = [abs(A[row][col]) for row in range(len(A))].index(a)
    print(i)


