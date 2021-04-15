# -*- codeing = utf-8 -*-
# @Time : 2021/4/14 17:12
# @Author : 名字
# @File : putFaceImage.py
# @Software : Pycharm
# @Contact: qq:
#          mail:

# -*- 功能说明 -*-
# 判断树莓派的指定文件夹是否有文件
# 如果没有则调用拍摄模块
import os


class putFaceImage:
    def __init__(self):
        self.file_dir = '/home/pi/share/faceImage'
        self.files_list = os.listdir(self.file_dir)
        self.files = []
        self.flag = 0  # 监控程序未开始
        self.count = 0

    def Getimage(self):
        while True:
            if len(self.files_list) == 10:
                self.count += 1
            else:
                pass
