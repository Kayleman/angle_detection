# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/test_1.bmp")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img)
plt.show()
# cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

# roi = img_gray[925:1210, 950:1730]
# roi = cv2.GaussianBlur(roi, (3, 3), 0)