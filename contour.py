# coding=utf-8
# @Time    : 000007/5/7 20:24
# @Author  : KayleZhuang
# @Site    : 
# @File    : contour.py
# @Software: PyCharm Community Edition
#
#                            _ooOoo_
#                           o8888888o
#                           88" . "88
#                           (| -_- |)
#                           O\  =  /O
#                        ____/`---'\____
#                      .'  \\|     |//  `.
#                     /  \\|||  :  |||//  \
#                    /  _||||| -:- |||||-  \
#                    |   | \\\  -  /// |   |
#                    | \_|  ''\---/''  |   |
#                    \  .-\__  `-`  ___/-. /
#                  ___`. .'  /--.--\  `. . __
#               ."" '<  `.___\_<|>_/___.'  >'"".
#              | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#              \  \ `-.   \_ __\ /__ _/   .-` /  /
#         ======`-.____`-.___\_____/___.-`____.-'======
#                            `=---='
#        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                      Buddha Bless, No Bug !
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images2018-5-4/test6_begin.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret1, th1 = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
print(ret1)
ret2, th2 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(ret2)
plt.figure()
plt.subplot(221), plt.imshow(img_gray, 'gray')
plt.subplot(222), plt.hist(img_gray.ravel(),256)#.ravel方法将矩阵转化为一维
plt.subplot(223), plt.imshow(th1, 'gray')
plt.subplot(224), plt.imshow(th2, 'gray')
plt.show()



