# -*- codeing = utf-8 -*-
# @Time : 2021/3/31 14:43
# @Author : cAMP-Cascade-DNN
# @File : Face_Trains.py
# @Software : Pycharm
# @Contact: qq:1071747983
#          mail:wuxiaolong8001@163.com

# -*- 功能说明 -*-
'''
根据Project/Detaction/resources/face_trainning_images文件夹中的人脸图片进行训练
调用前需要在文件夹中存放图片
调用后文件夹将自动清空

调用函数train()
'''
# -*- 功能说明 -*-

import os

import cv2
import numpy as np
from PIL import Image


class Face_Trains():

    def __init__(self):

        self.code_path = os.path.dirname(os.path.abspath(__file__))  # 获取代码路径
        self.project_path = os.path.dirname(self.code_path)  # 获取识别项目路径
        self.source_path = os.path.join(
            self.project_path, "resources")  # 获取依赖数据路径
        self.photo_path = os.path.join(
            self.source_path, "face_trainning_images")  # 获取训练集路径
        self.train_path = os.path.join(
            self.project_path,
            "Trainning result")  # 获取训练数据保存路径

        # 人脸数据路径
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        # recognizer = cv2.face.EigenFaceRecognizer_create()
        # recognizer = cv2.face.FisherFaceRecognizer_create()
        self.cvo = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
        self.cvo.load(
            os.path.join(self.source_path, 'haarcascade_frontalface_alt2.xml'))

    def getImagesAndLabels(self, path):
        '''
            生成图片标签列表
        '''
        imagePaths = [os.path.join(path, f)
                      for f in os.listdir(path)]  # 列表生成式产生图像路径列表
        faceSamples = []
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')  # 转为灰度图
            img_numpy = np.array(PIL_img, 'uint8')  # 从PIL图转为numpy数组
            id = int(os.path.split(imagePath)[-1].split("."))
            faces = self.cvo.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x: x + w])
                ids.append(id)
        return faceSamples, ids

    '''
        利用photo_path的图片进行训练 
        如果图片数量低于10张 返回错误1
    '''
    def train(self):
        if len(os.listdir(self.photo_path))<=10:
            return 1
        else:
            faces, ids = self.getImagesAndLabels(self.photo_path)
            self.recognizer.train(faces, np.array(ids))
            trainpath = os.path.join(self.train_path, "trainer.yml")
            self.recognizer.write(trainpath)
            os.remove(self.photo_path) #删除并重建图片文件夹 不考虑子文件夹
            os.mkdir(self.photo_path)


if __name__ == '__main__':
    ft = Face_Trains()