import cv2
import numpy as np


def multi_transform(img, pts1):

    # 选定四点在逆变换后图像中坐标
    pts2 = np.float32([[0, 0], [700, 0], [0, 700], [700, 700]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    output = cv2.warpPerspective(img, matrix, (700, 700))

    for i in range(0, 4):
        cv2.circle(img, (int(pts1[i][0]), int(pts1[i][1])), 6, (0, 0, 255), cv2.FILLED)

    for i in range(0, 4):
        cv2.circle(output, (int(pts2[i][0]), int(pts2[i][1])), 6, (0, 0, 255), cv2.FILLED)

    # cv2.imwrite("./data/IPM_data/IPM_result.jpg",output)
    cv2.imshow("src image", img)
    cv2.imshow("output image", output)
    cv2.waitKey(0)

if __name__ == '__main__':
    img = cv2.imread("./data/IPM_data/IPM0.png")
    # pst1为指定的四点在原图中的坐标
    pts1 = np.float32([[330, 40],  # p1左上
                       [1713, 15],  # p2右上
                       [150, 1437],  # p3左下
                       [1922, 1432]])  # p4右下
    multi_transform(img, pts1)