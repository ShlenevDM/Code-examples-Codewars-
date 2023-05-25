def draw_triangle(triangle, n):
    res = [[0 for j in range(n)] for i in range(n)]
    (x1, y1), (x2, y2), (x3, y3) = triangle
    s = 1 if (x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3) < 0 else -1
    for px in range(n):
        for py in range(n):
            if s * ((x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)) <= 0 and s * (
                    (x3 - x2) * (py - y2) - (y3 - y2) * (px - x2)) <= 0 and s * (
                    (x3 - x1) * (py - y3) - (y3 - y1) * (px - x3)) >= 0:
                res[py][px] = 1
    return res


print(*draw_triangle([(1, -49997), (2, 3), (3, 50002)], 6), sep='\n', end='\n-------\n')
print(*draw_triangle([(2, 1), (0, 3), (5, 4)], 6), sep='\n')
