from itertools import combinations


def biggest_triang_int(point_list, center, r):
    xc, yc, zc = center
    inside = []
    for point in point_list:
        x, y, z = point
        d = ((x - xc) ** 2 + (y - yc) ** 2 + (z - zc) ** 2) ** 0.5
        if d < r and abs(d - r) / r > 10 ** (-10):
            inside.append(point)
    if not inside:
        return []
    three_dots = combinations(inside, 3)
    triangles = dict()
    for triangle in three_dots:
        (x1, y1, z1), (x2, y2, z2), (x3, y3, z3) = triangle
        s = 0.5 * (
                ((z3 - z1) * (y2 - y1) - (y3 - y1) * (z2 - z1)) ** 2 +
                ((z2 - z1) * (x3 - x1) - (z3 - z1) * (x2 - x1)) ** 2 +
                ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) ** 2
        ) ** 0.5
        if s >= 10 ** (-8):
            triangles[(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)] = s
    n = len(triangles)
    s_max = triangles[max(triangles, key=triangles.get)]
    max_triangle = []
    for triangle in triangles:
        if triangles[triangle] == s_max:
            max_triangle.append(list(map(list, triangle)))
    if len(max_triangle) == 1:
        max_triangle = max_triangle[0]
    return [n, s_max, max_triangle]


points_list1 = [[1, 2, -4], [-3, 2, 4], [7, 8, -4], [2, 3, 5], [-2, -1, 1]]
sphere_center1 = [1, 2, -2]
radius1 = 8
print(biggest_triang_int(points_list1, sphere_center1, radius1))

points_list2 = [[1, 2, -4], [-3, 2, 4], [7, 8, -4],
                [2, 3, 5], [-2, -1, 1], [3, 2, 6], [1, 4, 0],
                [-4, -5, -6], [4, 5, 6], [-2, -3, -5], [-1, -2, 4],
                [-3, -2, -6], [-1, -4, 0], [2, 1, -1]]
sphere_center2 = [0, 0, 0]
radius2 = 8
print(biggest_triang_int(points_list2, sphere_center2, radius2))
