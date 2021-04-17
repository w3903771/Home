# -*- codeing = utf-8 -*-
# @Time : 2021/4/6 8:42
# @Author : cAMP-Cascade-DNN
# @File : Face_Rec.py
# @Software : Pycharm
# @Contact: qq:1071747983
#          mail:wuxiaolong8001@163.com

'''# -*- 功能说明 -*-

调用此类后 根据传入的图片地址与yml训练数据进行识别 返回正常 异常情况判断
俩个函数 一个判断是否是人 一个判断是否与yml符合 如不符合 调用文件类 进行储存 再返回结果与路径

'''  # -*- 功能说明 -*-

import os

from cv2 import cv2


class Face_Rec:
    def __init__(self):
        self.code_path = os.path.dirname(os.path.abspath(__file__))  # 获取代码路径
        self.project_path = os.path.dirname(self.code_path)  # 获取识别项目路径
        self.source_path = os.path.join(
            self.project_path, "Trainning result")  # 获取依赖数据路径
        self.train_path = os.path.join(
            self.source_path,
            "faceTrainer.yml")  # 获取训练数据保存路径

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read(self.train_path)
        # recognizer = cv2.face.EigenFaceRecognizer_create()
        # recognizer = cv2.face.FisherFaceRecognizer_create()
        self.cvo = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
        self.cvo.load(
            os.path.join(self.source_path, 'haarcascade_frontalface_alt2.xml'))

    def isperson(self, photo_path):
        img = cv2.imread(photo_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.cvo.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        if faces == []:
            return 0
        else:
            return 1

    def ishost(self, photo_path):
        idnum = 0
        img = cv2.imread(photo_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.cvo.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            idnum, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])
            if confidence < 100:
                id = 0
                confidence = "{0}%".format(round(100 - confidence))
            else:
                idnum = "unknown"
                confidence = "{0}%".format(round(100 - confidence))
            cv2.putText(img, str(idnum), (x + 5, y - 5), self.font, 1, (0, 0, 255), 3)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), self.font, 1, (0, 0, 255), 3)
            if id == 0:
                return False
            else:
                return True, img


if __name__ == "__main__":
    a = Face_Rec()
