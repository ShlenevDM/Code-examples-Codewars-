# Hanoi Tower, Hanoi Tower Array codewars.com/kata/5a02a758ffe75f8da5000030


def hanoiArray(n):
    tower = [list(range(n, 0, -1)), [], []]
    res = [str(tower)]

    def move_to(arr, n, i, f):
        if n == 1:
            arr[f].append(arr[i].pop())
            res.append(str(tower))
        else:
            m = 3 - i - f
            move_to(arr, n - 1, i, m)
            move_to(arr, 1, i, f)
            move_to(arr, n - 1, m, f)

    move_to(tower, n, 0, 2)

    return '\n'.join(res)


print(hanoiArray(3))