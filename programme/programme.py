import math
import numpy as np
from itertools import permutations
import random
import cv2

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
    l = len(centers)
    if l <= 1:
        return []
    distance = dict()
    for i in range(l):
        distance[(centers[i], centers[i])] = 0
        for j in range(i + 1, l):
            dis = np.sqrt(sum([(centers[i][_] - centers[j][_]) ** 2 for _ in range(len(centers[i]))]))
            distance[(centers[i], centers[j])] = dis
            distance[(centers[j], centers[i])] = dis
    con = [centers[0]]
    not_con = centers[1:]
    optimal = []
    for _ in range(l - 1):
        a, b = con[0], not_con[0]
        length_ab = distance[(a, b)]
        for m in con:
            for n in not_con:
                lg = distance[(m, n)]
                if lg < length_ab:
                    length_ab = lg
                    a, b = m, n
        ia, ib = centers.index(a), centers.index(b)
        optimal.append([ia, ib])
        na, nb = sum([i.count(ia) for i in optimal]), sum([i.count(ib) for i in optimal])
        con.append(b)
        not_con.remove(b)
    return optimal


if __name__ == '__main__':
    # test = [(114, 293), (147, 113), (156, 167), (185, 236), (201, 121), (251, 158), (255, 297), (265, 243), (305, 118), (313, 174)]
    # test = [(114, 293), (147, 113), (156, 167), (185, 236), (201, 121), (251, 158), (255, 297), (265, 243), (305, 118),
    #         (313, 174)]
    test = []
    for i in range(30):
        test.append((random.randint(1,640), random.randint(1,480)))
    img = np.zeros((480, 640, 3), np.uint8)
    img0 = np.zeros((480,640,3), np.uint8)
    img0.fill(255)
    img.fill(255)
    for i, point in enumerate(test):
        cv2.circle(img, point, 7, (0, 0, 0), -1)
        cv2.circle(img0, point, 7, (0, 0, 0), -1)
        cv2.putText(img, str(i), point, 0, 2, (128, 128, 128))
        cv2.putText(img0, str(i), point, 0, 2, (128, 128, 128))
    ans = programme(test)
    # ans0 = programme0(test)
    print(ans)
    # print(ans0)
    # for i in range(len(ans)):
    #     # cv2.line(img, test[ans[i]], test[ans[i+1]], (255, 0, 0), 5)
    #     cv2.line(img0, test[ans0[i]], test[ans0[i+1]], (0, 0, 255), 5)
    for u, v in ans:
        cv2.line(img, test[u], test[v], (0, 0, 255), 5)
    cv2.imshow("test0", img0)
    cv2.imshow("test", img)
    cv2.waitKey()

