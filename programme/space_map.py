import numpy as np

THETA = 43
PHI = 28.5
SHIFT = [0, 0, 0]


def mapping(point, shape):
    dx = point[0] - shape[1] / 2
    dy = point[1] - shape[0] / 2
    z = point[2]
    tanx = 2 * dx / shape[0] * np.tan(np.deg2rad(THETA))
    tany = 2 * dy / shape[1] * np.tan(np.deg2rad(PHI))
    x = z * tanx
    y = - z * tany
    return int(x) + SHIFT[0], int(y) + SHIFT[1], z + SHIFT[2]
