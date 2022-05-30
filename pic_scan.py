# -*- Coding = utf-8 -*-
# @time: 2022/5/30 14:35
# Author:Zhangxuan
# @file:pic_scan.PY
# @SOFTWARE:PV_Panel_Defects

from matplotlib import pyplot as plt
import cv2
img = cv2.imread(r'./sample/0009.png', cv2.IMREAD_GRAYSCALE)
print(img, img.shape)
plt.imshow(img, cmap='gray')
plt.show()
plt.clf()
# img = cv2.imread(r'./labels/0008.png')
# print(img.shape)
img2 = cv2.threshold(img, 150, 225, cv2.THRESH_TOZERO)[1]
print(img2)
plt.imshow(img2, cmap='gray')
plt.show()
