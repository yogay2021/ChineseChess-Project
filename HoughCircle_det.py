import cv2 as cv
import matplotlib as plt
import numpy as np

img_ori = cv.imread("./data/IPM_data/IPM_result.jpg", 1)
img = img_ori.copy()


img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur_img = cv.GaussianBlur(img, (7, 7), 0)

circle = cv.HoughCircles(
    blur_img,
    cv.HOUGH_GRADIENT,
    1,
    60,
    param1=20,
    param2=40,
    minRadius=20,
    maxRadius=40)

for i in circle[0, :]:  # 遍历矩阵的每一行的数据
    # 绘制圆形
    cv.circle(img_ori, (int(i[0]), int(i[1])), int(i[2]), (255, 0, 0), 3)
    # 绘制圆心
    cv.circle(img_ori, (int(i[0]), int(i[1])), 8, (255, 0, 0), -1)
    print((int(i[0]), int(i[1])))

cv.imshow("0",blur_img)
cv.imshow("1", img_ori)
cv.waitKey(0)