import re


def solve(*equations):
    # find all variables
    variables = set()
    for eq in equations:
        variables = variables | set(re.findall(r'[a-zA-Z]+', eq))
    variables = sorted(list(variables))

    n = len(variables)
    m = len(equations)

    print(m, n)

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

    print(*A, sep='\n')
    print()

    for i in range(m - 1):
        #print(A[i])
        if i == m:
            print('B')
            break
        #print(i)
        if [round(el, 5) for el in A[i]] == [0] * (n + 1):
            A.remove(A[i])
            m -= 1
            break

        elif round(A[i][i], 10) == 0:
            t = max(A[row][i] for row in range(i + 1, m))
            q = [A[row][i] for row in range(i + 1, m)].index(t)
            if round(t, 6) == 0:
                return
            else:
                A[i], A[q] = A[q], A[i]

        #print(m)

        if [round(el, 5) for el in A[i]] == [0] * (n + 1):
            A.remove(A[i])
            m -= 1

        #print(A[i])

        pivot = A[i][i]
        for j in range(i + 1, m):
            c = A[j][i] / pivot
            for k in range(i, n + 1):
                A[j][k] -= c * A[i][k]
                A[j][k] = round(A[j][k], 10)

    if [round(el, 5) for el in A[-1]] == [0] * (n + 1):
        A.remove(A[-1])
        m -= 1

    print(*A, sep='\n')

    if n != m:
        return

    res = dict()
    for i in range(1, n + 1):
        res[variables[-i]] = (A[-i][n] - sum(A[-i][n - j] * res[variables[-j]] for j in range(1, i))) / A[-i][n - i]

    return res





#print(solve('131t+272z-228s+360x-44r+184y+75v+49v-177w+257t+144u-210p+28q+4r=30p+91w-26928', '-135s+75z-7v-45s+315z+39v-153q+461u-830p-402q-595y+100t+640w+80x-203r+159059-557r=52v-139u+145q-53001+245y', '-87v-94y+15p+87u-19r+392-7q+50r-76w-86x+53q+14t+48r-29z-97s+37v=-8y-997', '46w-26s-76x-14q-15p-35w+26z+87v-277-11s+15u-24y+93r+48s+2z+27t=-34t+47t-12w-66z+788+38t', '84t+9v+67u-33x+32x-69y-35q-2s-94w+69p+63z-96r-49q=-42v+50s+13p-28q-8390', '-3t+7t+60w-76r+60u-18s+6x+6t+29z-83p-2v-70q+27w+2x-84y=-10z-21206+23w', '-67p+87v+21q-8w-20x-20t-46u+5y+27r-16y+52z+1438-70s-33u+4v=10q-4446+16s', '-10r-80x+51q-72s+8v-53z-55t-88w-68y-71u-1051+8p+21u=42t+498+453+24p-48z', '-2x+22q+22r-54w-93r+27p-33y-61y-109v-1395-73u-72s+2z+93t-32p=-33u-18v+3992', '-21u+44s+82w+10p-38t-29z+16y+3r-3s+42v+64q-90x+177=29v-24y-44s-14q-67v-414+4s', '60r-316u-268p-46y+208z+44q-344s+364v-47t-32w-33t+27x=44x-23536-63r+63x+15r-2y', '90x+46y+33u+43t+10u+7q-67w-58p+68z+1699-57s+31v-12u-10r+5u=-5033-54t+2p', '-53p+43u-25w+49t+y-83v-14s-88r+28z-9t-7z+33q-46x=-45y-4823+49p-17p', '-15r-84w+33u-29x-79y+90t+13p+35s-76q+21s+7v-z=2580-27z-24s'))
