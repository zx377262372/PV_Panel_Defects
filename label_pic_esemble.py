# -*- Coding = utf-8 -*-
# @time: 2022/5/30 14:04
# Author:Zhangxuan
# @file:label_pic_esemble.PY
# @SOFTWARE:PV_Panel_Defects
import os
import shutil

path = './pics/'
dirpath = './labels/'
dirpath2 = './sample/'
for eachfile in os.listdir(path):
    if os.path.isdir(path + eachfile):
        print(path, eachfile)
        if os.path.exists(path + eachfile + '/label.png'):
            shutil.copy(path + eachfile + '/label.png', dirpath + eachfile.split('_')[1] + '.png')
            print(eachfile + ' successfully moved')
        if os.path.exists(path + eachfile + '/img.png'):
            shutil.copy(path + eachfile + '/img.png', dirpath2 + eachfile.split('_')[1] + '.png')