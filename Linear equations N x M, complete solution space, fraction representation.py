from fractions import Fraction


def solve(system):
    A = [[Fraction(x) for x in row.split()] for row in system.split('\n')]
    n, m = len(A), len(A[0]) - 1
    for i in range(n):
        pivot = A[i][i]
        A[i] = [x / pivot for x in A[i]]
        for j in range(i + 1, n):
            c = A[j][i]
            for k in range(i, m + 1):
                A[j][k] -= c * A[i][k]
    print(*A, sep='\n')
    print()
    for i in range(1, n):
        for j in range(i):
            c = A[j][i]
            for k in range(i, m + 1):
                A[j][k] -= c * A[i][k]
    return A


lgs0 = '\n'.join(['1 2 5 6 7'
                 , '2 3 4 0 8'
                 , '3 4 5 6 9'])

lgs1 = '\n'.join(['1 2 0 0 7'
                 , '0 3 4 0 8'
                 , '0 0 5 6 9'])

lgs8 = '\n'.join(['1/20 -10/3 -10/9 -13',
                  '-29 8 -27/4 0',
                  '-26 -14 25 10/7'])
lgs9 = '1 2 2\n1 2 2\n2 4 4'

lgs10 = '0 0 0 0\n0 0 0 0'

print(*solve(lgs8), sep='\n')