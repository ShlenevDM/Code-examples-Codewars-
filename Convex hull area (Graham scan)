def hull_method(pointlist):
    pointlist = list(map(list, set(map(tuple, pointlist))))
    #print(pointlist)
    p0 = min(pointlist, key=lambda x: (x[1], x[0]))
    pointlist.remove(p0)
    cross = lambda p1, p2, p3: (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    points = sorted(pointlist, key=lambda pi: ((-(pi[0] - p0[0]) / ((pi[0] - p0[0]) ** 2 + ((pi[1] - p0[1]) ** 2)) ** 0.5), (pi[0] - p0[0]) ** 2 + ((pi[1] - p0[1]) ** 2)))
    print([p0] + points)
    res = [p0, points.pop(0)]
    for point in points:
        while True:
            p1, p2 = res[-2:]
            #print(p1, p2, point)
            if cross(p1, p2, point) <= 0 and len(res) > 2:
                res.pop(-1)
            elif cross(p1, p2, point) <= 0 and len(res) == 2:
                res.pop(-1)
                break
            else:
                break
        res.append(point)
    return points


print(hull_method([[32, 32], [79, 41], [80, 12], [96, 86], [96, 61], [37, 44], [88, 61], [47, 88], [65, 0], [46, 83], [55, 54], [57, 47], [22, 68], [2, 31], [64, 22], [25, 40], [68, 39], [48, 35], [11, 38], [67, 94], [10, 0], [41, 0], [96, 26]]))
