import cv2
import os
img_ori = cv2.imread("E:\\Project\\Python\\Chinses_chess Project\\data\\patten\\zu.jpg",1)
output_path = "E:/Project/Python/Chinses_chess Project/data/dataset_rotation/zu/"
# 旋转生成数据集
col = img_ori.shape[0]
row = img_ori.shape[1]
for theta in range(360):
    RotationMatrix = cv2.getRotationMatrix2D((col/2, row/2), theta, 1)
    result = cv2.warpAffine(img_ori, RotationMatrix, (col, row), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
    result_path = os.path.join(output_path, 'zu' + str(theta) + '.jpg')
    cv2.imwrite(result_path, result)
