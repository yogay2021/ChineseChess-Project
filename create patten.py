import cv2
import numpy as np
img = cv2.imread("E:\\Project\\Python\\Chinses_chess Project\\data\\patten_source\\zu.jpg",0)

# 高斯滤波
blurimg = cv2.GaussianBlur(img, (7, 7), 0)

# OTSU二值化处理
ret, th = cv2.threshold(blurimg,0,255,cv2.THRESH_OTSU)

# 开运算
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(th, kernel, iterations=1)

# 重设尺寸
result = cv2.resize(dilation,(180,180))
print(result.size)

# cv2.imshow("result",result)
# cv2.waitKey(0)
# cv2.imwrite("E:\\Project\\Python\\Chinses_chess Project\\data\\patten\\zu.jpg", result)