m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


def rotate(matrix, direction):
    if direction == 'clockwise':
        return list(map(list, zip(*matrix[::-1])))
    elif direction == 'counter-clockwise':
        return list(map(list, zip(*matrix)))[::-1]


print(rotate(m, 'clockwise'))
print(rotate(m, 'counter-clockwise'))
