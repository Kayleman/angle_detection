# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images2018-5-4/test16.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

start_x = 974
end_x = 1737

start_y = 811
end_y = 1069
img_roi = img_gray[start_y: end_y, start_x: end_x]

plt.imshow(img_roi)

# plt.imshow(img)
plt.show()
# cv2.namedWindow('img', 0)
# cv2.resizeWindow('img',800, 400)
# cv2.imshow('img', img_gray)
# cv2.waitKey()
# cv2.destroyAllWindows()

# roi = img_gray[925:1210, 950:1730]
# roi = cv2.GaussianBlur(roi, (3, 3), 0)