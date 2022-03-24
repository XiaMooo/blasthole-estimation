import numpy as np
from itertools import permutations

def euclideanDistance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

def programme0(centers):
    n = len(centers)
    ans = []
    centers = np.array(centers)
    distance = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dis = euclideanDistance(centers[i], centers[j])
            distance[i][j] = dis
            distance[j][i] = dis
    s = 0
    sMin = float("inf")
    for lst in permutations(range(n)):
        s = 0
        for i in range(1, n):
            s += distance[lst[i]][lst[i-1]]
        if s <= sMin:
            sMin = s
            ans = lst[:]
    return ans


def programme(centers):
    n = len(centers)
    centers = np.array(centers)
    distance = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dis = euclideanDistance(centers[i], centers[j])
            distance[i][j] = dis
            distance[j][i] = dis
    s = 0
    sMin = float("inf")
    stack = []
    ans = []

    def bt():
        nonlocal s
        nonlocal n
        nonlocal sMin
        nonlocal ans
        if len(stack) == n:
            if s < sMin:
                ans = stack[:]
                sMin = s
            return
        for i in range(n):
            if i in stack:
                continue
            stack.append(i)
            s += distance[stack[-1]][stack[-2]] if len(stack) > 1 else 0
            bt()
            s -= distance[stack[-1]][stack[-2]] if len(stack) > 1 else 0
            stack.pop()

    bt()

    return ans


if __name__ == '__main__':
    import time
    t0 = time.time()
    test = [(114, 293), (147, 113), (156, 167), (185, 236), (201, 121), (251, 158), (255, 297), (265, 243), (305, 118), (313, 174)]
    test = np.array(test)
    ans = programme(test)
    print(ans)
    print(f'Time Cost:{time.time() - t0}s.')
