#!/usr/bin/env python
# encoding: utf-8
import cv2
import numpy as np

img = cv2.imread("images/test_1.bmp")

img = cv2.GaussianBlur(img, (3, 3), 0)
edges = cv2.Canny(img, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 118)
result = img.copy()

# 经验参数
minLineLength = 30
maxLineGap = 30
lines = cv2.HoughLinesP(edges, 1, np.pi / 1800, 100, minLineLength, maxLineGap)
lines2d = lines[:, 0, :]  # 提取为为二维
for x1, y1, x2, y2 in lines2d:
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

cv2.namedWindow("Result",0)
cv2.resizeWindow("Result", 640, 480)
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()