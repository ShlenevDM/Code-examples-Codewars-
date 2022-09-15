def closest_points(coord):
    n = len(coord)
    dist = dict()
    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = coord[i], coord[j]
            d = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
            if d in dist:
                dist[d].append((p1, p2))
            else:
                dist[d] = [(p1, p2)]
    distance = min(dist)
    pairs = dist[distance]
    return [n, pairs, distance]


print(closest_points([(8, 14), (16, 5), (5, 5), (15, 18), (17, 10), (0, 14), (4, 15), (19, 17), (13, 16), (10, 18), (14, 13), (12, 14), (11, 15), (7, 15)]))