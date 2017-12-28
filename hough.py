# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/19.bmp")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.GaussianBlur(img_gray, (3, 3), 0)
edges = cv2.Canny(img_gray, 50, 150, apertureSize=3)

# cv2.HoughLines()返回值是个二维矩阵，为(rho,theta)，
# 其中rho的单位是像素长度（也就是直线到图像原点(0,0)点的距离），
# 而theta的单位是弧度。
# 这个函数有四个输入，第一个是二值图像，这里为canny变换后的图像，
# 二三参数分别是rho和theta的精确度，可以理解为步长。
# 第四个参数为阈值T，认为当累加器中的值高于T是才认为是一条直线。

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
lines1 = lines[:,0,:]#提取为为二维
for rho,theta in lines1[:]:
# for rho, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# cv2.namedWindow('Canny', 0)
# cv2.resizeWindow('Canny', 640, 480)
# cv2.namedWindow('Result', 0)
# cv2.resizeWindow('Result', 640, 480)
# cv2.imshow('Canny', edges)
# cv2.imshow('Result', result)
plt.imshow(img, 'gray')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()