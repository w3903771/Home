# -*- codeing = utf-8 -*-
# @Time : 2021/03/20 18:06
# @Author : Done
# @File : DY
# @File : get_picture.py
# @Software : Pycharm
# @Contact: qq:2905747104

# -*- 功能说明 -*-
# 从共享文件夹中得到图片并且保存到本地文件夹
# -*- 功能说明 -*-


import os
import shutil


class GetImage:

    def __init__(self):
        self.code_path = os.path.dirname(os.path.abspath(__file__))  # 获取代码路径
        self.project_path = os.path.dirname(self.code_path)
        self.project_path = os.path.dirname(self.project_path)  # 获取识别项目路径
        self.resource_path = os.path.join(
            self.project_path, "Resources")  # 获取资源文件夹路径
        self.facephoto_path = os.path.join(
            self.resource_path, "../Resources/FaceImage")  # 获取人脸图片路径
        self.ohterphoto_path = os.path.join(
            self.resource_path, "OhterImage")  # 获取其它图片路径

        self.path = 'E:\\smart_home\\get_img\\Images'  # 共享文件夹的路径
        self.rmface_path = os.path.join(self.path, "../Resources/FaceImage")
        self.rmother_path = os.path.join(self.path, "../Resources/OtherImage")
        self.num = 5  # 设定的单位时间取照片数

    def getFaceToLocal(self):
        if len(os.listdir(self.rmface_path)) == self.num:
            for root, dirs, files in os.walk(self.path):
                for i in range(len(files)):
                    if (files[i][-3:] == 'jpg'):
                        file_path = root + '/' + files[i]
                        new_file_path = self.new_path + '/' + files[i]
                        shutil.move(file_path, new_file_path)

    def getOtherToLocal(self):
        if len(os.listdir(self.rmother_path)) == self.num:
            for root, dirs, files in os.walk(self.path):
                for i in range(len(files)):
                    if (files[i][-3:] == 'jpg'):
                        file_path = root + '/' + files[i]
                        new_file_path = self.new_path + '/' + files[i]
                        shutil.move(file_path, new_file_path)