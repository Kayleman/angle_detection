# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt
# import time
# from watchdog.observers import Observer
# from watchdog_img import CreatedEventHandler
class Ad3:
    # 坐标原点偏移
    def __init__(self):
        # self.start_x = 762
        # self.end_x = 1718
        #
        # self.start_y = 597
        # self.end_y = 984

        self.start_x = 890
        self.end_x = 1689

        self.start_y = 732
        self.end_y = 1090

    # offset_x = 762  # test_1-18
    # offset_y = 597

    # offset_x = 710  # short_13
    # offset_y = 587

    # offset_x = 795  # short_12
    # offset_y = 855

    # offset_x = 1013 # short_10
    # offset_y = 1005

    # offset_x = 950 # long
    # offset_y = 925

    # offset_x = 420 # short_case
    # offset_y = 268

    #
    # def watch_path(path):
    #     event_handler = CreatedEventHandler()
    #     observer = Observer()
    #     observer.schedule(event_handler, path, recursive=True)
    #     observer.start()
    #     try:
    #         while True:
    #             time.sleep(1)
    #     except KeyboardInterrupt:
    #         observer.stop()
    #     observer.join()

    def hough_change(self, canny_img, img):
        # cv2.HoughLines()返回值是个二维矩阵，为(rho,theta)，
        # 其中rho的单位是像素长度（也就是直线到图像原点(0,0)点的距离），
        # 而theta的单位是弧度。
        # 这个函数有四个输入，第一个是二值图像，这里为canny变换后的图像，
        # 二三参数分别是rho和theta的精确度，可以理解为步长。
        # 第四个参数为阈值T，认为当累加器中的值高于T是才认为是一条直线。
        # lines = cv2.HoughLines(canny_img, 1, np.pi / 18000, 200) # short_10 and short_12 and short_13

        lines = cv2.HoughLines(canny_img, 2, np.pi / 18000, 200)
        roi_copy = canny_img.copy()
        img_copy = img.copy()
        lines2d = lines[:, 0, :]  # 提取为为二维
        lines2d = lines2d[np.lexsort(lines2d[:, ::-1].T)]  # 将数组按照第一列rho的值进行递增排序
        rho_left_up = []
        angle_left_up = []
        flag_left_up = False

        rho_left_down = []
        angle_left_down = []
        flag_left_down = False

        rho_right_up = []
        angle_right_up = []
        flag_right_up = False

        rho_right_down = []
        angle_right_down = []
        flag_right_down = False

        # angle_left = []
        # angle_right_1 = []
        # angle_right_2 = []

        for rho, theta in lines2d[:]:

            # print("-------------")
            # print(rho)
            # print(theta)
            # print(theta * 180 / np.pi)

            angle_line = theta * 180 / np.pi
            if 120 < angle_line < 140:
                if -50 < rho < 0:
                    rho_left_down.append(rho)
                    angle_left_down.append(angle_line)
                    flag_left_down = True
                if -100 < rho < -50:
                    rho_left_up.append(rho)
                    angle_left_up.append(angle_line)
                    flag_left_up = True
            elif 30 < angle_line < 50:
                if 600 < rho < 650:
                    rho_right_up.append(rho)
                    angle_right_up.append(angle_line)
                    flag_right_up = True
                if 650 < rho < 700:
                    rho_right_down.append(rho)
                    angle_right_down.append(angle_line)
                    flag_right_down = True

                    # a = np.cos(theta)
                    # b = np.sin(theta)
                    # x0 = a * rho
                    # y0 = b * rho
                    # x1 = int(x0 + 500 * (-b))
                    # y1 = int(y0 + 500 * a)
                    # x2 = int(x0 - 1000 * (-b))
                    # y2 = int(y0 - 1000 * a)
                    #
                    # cv2.line(roi_copy, (x1, y1), (x2, y2), (255, 255, 0), 5)
                    #
                    # cv2.line(img_copy, (x1 + offset_x, y1 + offset_y),
                    #          (x2 + offset_x, y2 + offset_y), (0, 255, 0), 5)
        if flag_left_up:
            rho_left_up_mean = np.mean(np.array(rho_left_up))
            angle_left_up_mean = np.mean(np.array(angle_left_up))
            theta_left_up_mean = angle_left_up_mean * np.pi / 180
            self.draw_line(roi_copy, img_copy, rho_left_up_mean, theta_left_up_mean)

        if flag_left_down:
            rho_left_down_mean = np.mean(np.array(rho_left_down))
            angle_left_down_mean = np.mean(np.array(angle_left_down))
            theta_left_down_mean = angle_left_down_mean * np.pi / 180
            self.draw_line(roi_copy, img_copy, rho_left_down_mean, theta_left_down_mean)

        if flag_right_up:
            rho_right_up_mean = np.mean(np.array(rho_right_up))
            angle_right_up_mean = np.mean(np.array(angle_right_up))
            theta_right_up_mean = angle_right_up_mean * np.pi / 180
            self.draw_line(roi_copy, img_copy, rho_right_up_mean, theta_right_up_mean)

        if flag_right_down:
            rho_right_down_mean = np.mean(np.array(rho_right_down))
            angle_right_down_mean = np.mean(np.array(angle_right_down))
            theta_right_down_mean = angle_right_down_mean * np.pi / 180
            self.draw_line(roi_copy, img_copy, rho_right_down_mean, theta_right_down_mean)

        # angle_left_mean = np.mean(np.array(angle_left))
        # angle_right_mean_1 = np.mean(np.array(angle_right_1))
        # angle_right_mean_2 = np.mean(np.array(angle_right_2))
        angle_min = []
        if flag_left_up and flag_right_up:
            angle_res_1 = 180 - (angle_left_up_mean - angle_right_up_mean)
            angle_min.append(angle_res_1)
            if angle_res_1 < 89 or angle_res_1 > 91:
                pass
            print("The angle 1 is:", angle_res_1)

        if flag_left_up and flag_right_down:
            angle_res_2 = 180 - (angle_left_up_mean - angle_right_down_mean)
            angle_min.append(angle_res_2)
            print("The angle 2 is:", angle_res_2)

        if flag_left_down and flag_right_up:
            angle_res_3 = 180 - (angle_left_down_mean - angle_right_up_mean)
            angle_min.append(angle_res_3)
            print("The angle 3 is:", angle_res_3)

        if flag_left_down and flag_right_down:
            angle_res_4 = 180 - (angle_left_down_mean - angle_right_down_mean)
            angle_min.append(angle_res_4)
            print("The angle 4 is:", angle_res_4)

        angle_min = np.min(np.array(angle_min))
        # print("The min angle is:", angle_min)
        # print("--------------------")
        return roi_copy, img_copy, angle_min
        # print("%.2f" % angle_min)
        # f = open('/test.txt', 'w')
        # f.write("The min angle is:", angle_min)
        # f.close()

        # a = np.cos(theta)
        # b = np.sin(theta)
        # x0 = a * rho
        # y0 = b * rho
        # x1 = int(x0 + 500 * (-b))
        # y1 = int(y0 + 500 * a)
        # x2 = int(x0 - 1000 * (-b))
        # y2 = int(y0 - 1000 * a)
        # cv2.line(roi_copy, (x1, y1), (x2, y2), (255, 255, 0), 5)
        #
        # cv2.line(img_copy, (x1 + offset_x, y1 + offset_y),
        #          (x2 + offset_x, y2 + offset_y), (0, 255, 0), 5)

    def draw_line(self, roi_copy, img_copy, rho, theta):
        offset_x = self.start_x
        offset_y = self.start_y
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 500 * (-b))
        y1 = int(y0 + 500 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)

        cv2.line(roi_copy, (x1, y1), (x2, y2), (255, 255, 0), 15)

        cv2.line(img_copy, (x1 + offset_x, y1 + offset_y),
                 (x2 + offset_x, y2 + offset_y), (0, 255, 0), 15)

    def detect_img(self, img_path):
        img = cv2.imread(img_path)
        # 路径自己选择
        # img = cv2.imread("images/test_1.bmp")
        # img = cv2.imread("images/2.png")
        # img = cv2.imread("images/23.bmp")
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        roi = img_gray[self.start_y:self.end_y, self.start_x:self.end_x]  # test
        # roi = img_gray[587:742, 710:1176]  # short_13
        # roi = img_gray[855:1198, 795:1750]  # short_12
        # roi = img_gray[1005:1198, 1013:1550] # short_10
        # roi = img_gray[925:1210, 950:1730]  # 普通的roi
        # roi = img_gray[268:342, 420:595]  # 短边大区域roi
        roi = cv2.GaussianBlur(roi, (3, 3), 0)
        roi_canny = cv2.Canny(roi, 50, 150, apertureSize=3)
        # roi_left = img[925:1210, 950:1350]
        # roi_right = img[925:1210, 1351:1730]
        #
        # roi_left = cv2.GaussianBlur(roi_left, (3, 3), 0)
        # canny_left = cv2.Canny(roi_left, 50, 150)
        #
        # roi_right = cv2.GaussianBlur(roi_right, (3, 3), 0)
        # canny_right = cv2.Canny(roi_right, 50, 150)

        # line_left, theta1 = hough_change(canny_left)
        # line_right, theta2 = hough_change(canny_right);
        roi_line, img_line, final_angle = self.hough_change(roi_canny, img)
        # print("This angle is :", )
        # angle = 180 - (theta1 - theta2) * 180
        # print(angle)

        # cv2.namedWindow('Canny', 0)
        # cv2.resizeWindow('Canny', 640, 480)
        # cv2.imshow('Canny', canny)

        # plt.subplot(321), plt.imshow(canny_left, 'gray'), plt.title('Canny')
        # plt.subplot(322), plt.imshow(roi_left, 'gray'), plt.title('Original')
        # plt.subplot(323), plt.imshow(canny_right, 'gray'), plt.title('Canny')
        # plt.subplot(324), plt.imshow(roi_right, 'gray'), plt.title('Original')
        # plt.subplot(325), plt.imshow(line_left), plt.title('Line_left')
        # plt.subplot(326), plt.imshow(line_right), plt.title('Line_right')

        # plt.subplot(221), plt.imshow(img), plt.title('Original Image')
        # plt.xticks(())  # ignore xticks
        # plt.yticks(())  # ignore yticks
        #
        # plt.subplot(222), plt.imshow(img_line), plt.title('Original Image With Line')
        # plt.xticks(())  # ignore xticks
        # plt.yticks(())  # ignore yticks
        #
        #
        # plt.subplot(223), plt.imshow(roi_canny, 'gray'), plt.title('ROI of Image')
        # plt.xticks(())  # ignore xticks
        # plt.yticks(())  # ignore yticks
        #
        # plt.subplot(224), plt.imshow(roi_line, 'gray'), plt.title('ROI With Line')
        # plt.xticks(())  # ignore xticks
        # plt.yticks(())  # ignore yticks
        plt.subplot(111), plt.imshow(img_line), plt.title('Original Image With Line')
        plt.xticks(())  # ignore xticks
        plt.yticks(())  # ignore yticks

        plt.show()
        # cv2.namedWindow('img_line', 0)
        # cv2.resizeWindow('img_line', 640, 480)
        # cv2.imshow('img_line', img_line)
        # # cv2.imwrite("line.png", line)
        # cv2.waitKey(1000)
        # cv2.destroyAllWindows()
        return final_angle

if __name__ == "__main__":
    ad3 = Ad3()
    final_angle = ad3.detect_img("images2018-5-4/test0.jpg")
