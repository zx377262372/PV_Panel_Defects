# -*- Coding = utf-8 -*-
# @time: 2022/5/30 15:38
# Author:Zhangxuan
# @file:gray_scale.PY
# @SOFTWARE:PV_Panel_Defects
import os
import cv2
list_dir = os.listdir('./sample/')
for i in list_dir:
    img = cv2.imread(f'./sample/{i}', cv2.IMREAD_GRAYSCALE)
    img_scale = cv2.threshold(img, 150, 225, cv2.THRESH_TOZERO)[1]
    cv2.imwrite(f'./gray_scale/{i}', img_scale)