from itertools import combinations

def biggest_triang_int(point_list, center, r):
    xc, yc, zc = center
    inside = []
    for point in point_list:
        x, y, z = point
        d = ((x - xc) ** 2 + (y - yc) ** 2 + (z - zc) ** 2) ** 0.5
        if d < r and abs(d - r) / r > 10 ** (-10):
            inside.append(point)
    triangles = combinations(inside, 3)
    for triangle in triangles:
        print(triangle)
    return triangles

points_list1 = [[1,2,-4], [-3, 2, 4], [7, 8, -4], [2, 3, 5], [-2, -1, 1]]
sphere_center1 = [1, 2, -2]
radius1 = 8
print(biggest_triang_int(points_list1, sphere_center1, radius1))