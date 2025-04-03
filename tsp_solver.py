import math
import random


def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def solve_tsp(points, start_index=None):
    n = len(points)

    if n <= 1:
        return list(range(1, n + 1)), 0

    if start_index is None:
        start_index = random.randint(0, n - 1)

    visited = [False] * n
    path = [start_index]
    visited[start_index] = True
    total_dist = 0

    for _ in range(n - 1):
        last = path[-1]
        nearest = None
        nearest_dist = float('inf')
        for i in range(n):
            if not visited[i]:
                d = distance(points[last], points[i])
                if d < nearest_dist:
                    nearest_dist = d
                    nearest = i
        path.append(nearest)
        visited[nearest] = True
        total_dist += nearest_dist

    total_dist += distance(points[path[-1]], points[path[0]])
    return [i + 1 for i in path], total_dist
