import cv2
import numpy as np

# 自定义卷积核
kernel_sharpen_1 = np.array([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]], np.float32)
kernel_sharpen_2 = np.array([
    [1, 1, 1],
    [1, -7, 1],
    [1, 1, 1]], np.float32)
kernel_sharpen_3 = np.array([
    [-1, -1, -1, -1, -1],
    [-1, 2, 2, 2, -1],
    [-1, 2, 8, 2, -1],
    [-1, 2, 2, 2, -1],
    [-1, -1, -1, -1, -1]]) / 8.0
# 图像锐化
kernel_sharpen_4 = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]], np.float32)
# 图像模糊
kernel_sharpen_5 = np.array([
    [0.0625, 0.125, 0.0625],
    [0.125, 0.25, 0.125],
    [0.0625, 0.125, 0.125]], np.float32)
# 索贝尔
kernel_sobel_y = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]], np.float32)
kernel_sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]], np.float32)
# 平滑算子
kernel_smooth_x = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]], np.float32)
kernel_smooth_y = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])
# 浮雕
kernel_float = np.array([
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2]], np.float32)
# 大纲outline
kernel_outline = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]], np.float32)
# 拉普拉斯算子
kernel_nabla = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]], np.float32)


# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 定义一个核
# dst = cv.filter2D(image, -1, kernel=kernel)

def filt(img, *kernels):
    for kernel in kernels:
        img = cv2.filter2D(img, -1, kernel=kernel)
    return img


def pre_process(img):
    # Your Code Here:
    v_img = None
    cv2.flip(img, -1, v_img)
    return v_img


def draw_bars(img):
    #
    pass
