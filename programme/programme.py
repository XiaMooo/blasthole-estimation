import numpy as np


def euclideanDistance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))


def programme(centers):
    n = len(centers)
    distance = [[0] * n for _ in range(n)]
    visited = [False] * n
    for i in range(n):
        for j in range(i + 1, n):
            dis = euclideanDistance(centers[i], centers[j])
            distance[i][j] = dis
            distance[j][i] = dis
    s = float("inf")

    def bt():
        pass
