# -*- codeing = utf-8 -*-
# @Time : 2021-04-20 23:47
# @Author : cAMP-Cascade-DNN
# @File : fileAndLog.py
# @Software : Pycharm
# @Contact: qq:1071747983
#          mail:wuxiaolong8001@163.com

# -*- 功能说明 -*-

#

# -*- 功能说明 -*-
import os
import time
import cv2


class fileAndLog:
    def __init__(self):
        self.code_path = os.path.dirname(os.path.abspath(__file__))  # 获取代码路径
        self.project_path = os.path.dirname(self.code_path)  # 获取识别项目路径
        self.source_path = os.path.join(
            self.project_path, "Resources")  # 获取依赖数据路径
        self.errors_path = os.path.join(
            self.source_path, "Errors")  # 获取依赖数据路径

    def save(self, img, flag):
        if flag == 1:
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            image_path = os.path.join(self.errors_path, t)
            test_path = os.path.join(self.errors_path, "errorlog.txt")
            print(image_path)
            # cv2.imwrite(image_path,img)
            f = open(test_path, "a")
            f.write(t + " 图像检测发现有陌生人长期停留")
