# Closest pair of points, O(n ** 2)

from collections import defaultdict


def closest_points(coord):
    n = len(coord)
    dist = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = coord[i], coord[j]
            d2 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
            dist[d2].append(sorted([p1, p2]))
    dist2_min = min(dist)
    pairs = dist[dist2_min]
    return [n, pairs, round(dist2_min ** 0.5, 4)]


print(closest_points([(8, 14), (16, 5), (5, 5), (15, 18), (17, 10), (0, 14), (4, 15), (19, 17), (13, 16), (10, 18), (14, 13), (12, 14), (11, 15), (7, 15)]))