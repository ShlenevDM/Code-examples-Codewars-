from fractions import Fraction


def solve(system):
    A = [[Fraction(x) for x in row.split()] for row in system.split('\n')]
    n, m = len(A), len(A[0]) - 1

    col_space = []
    row_space = []
    # from A to U
    row, col = 0, 0

    while row < n:
        if A[row] == [0] * (m + 1):
            row += 1
        elif A[row][:-1] == [0] * m and A[-1] != 0:
            return 'SOL=NONE'
        else:
            while A[row][col] == 0 and col < m:
                for i in range(row + 1, n):
                    if A[i][row] != 0:
                        A[i], A[row] = A[row], A[i]
                        break
                else:
                    col += 1

            pivot = A[row][col]
            A[row] = [el / pivot for el in A[row]]
            for j in range(row + 1, n):
                c = A[j][col]
                for k in range(col, m + 1):
                    A[j][k] -= c * A[row][k]

            row_space.append(row)
            col_space.append(col)
            row += 1
            col += 1

    # from U to R
    for (row, col) in zip(row_space, col_space):
        for j in range(row):
            c = A[j][col]
            for k in range(col, m + 1):
                A[j][k] -= c * A[row][k]

    # particular solution
    x_particular = [0] * m
    for (row, col) in zip(row_space, col_space):
        x_particular[col] = A[row][-1]

    # special solutions
    x_special = []
    nullspace = [x for x in range(m) if x not in col_space]
    for ncol in nullspace:
        sol = [0] * m
        sol[ncol] = 1
        for (row, col) in zip(row_space, col_space):
            sol[col] = - A[row][ncol]
        x_special.append(sol)

    res = 'SOL=('
    for x in x_particular:
        if x.denominator == 1:
            res += f'{x.numerator}'
        else:
            res += f'{x.numerator}/{x.denominator}'
        res += ';'
    res = res[:-1]
    res += ')'

    for n, sol in enumerate(x_special):
        res += f'+q{n + 1}*('
        for x in sol:
            if x.denominator == 1:
                res += f'{x.numerator}'
            else:
                res += f'{x.numerator}/{x.denominator}'
            res += ';'
        res = res[:-1]
        res += ')'

    return res


lgs0 = '\n'.join(['1 3 0 2 1'
                     , '0 0 1 4 6'
                     , '1 3 1 6 7'])

lgs1 = '\n'.join(['1 2 0 0 7'
                     , '0 3 4 0 8'
                  , '0 0 0 0 0'
                     , '0 0 5 6 9'])

lgs2 = '\n'.join(['1 5/2 1/2 0 4 1/8'
                 ,'0 5 2 -5/2 6 2'])

lgs8 = '\n'.join(['1/20 -10/3 -10/9 -13',
                  '-29 8 -27/4 0',
                  '-26 -14 25 10/7'])
lgs9 = '1 2 2\n1 2 2\n2 4 4'

lgs10 = '0 0 0 0\n0 0 0 0'

print(solve(lgs1), sep='\n')
