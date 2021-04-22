# -*- codeing = utf-8 -*-
# @Time : 2021/4/6 8:42
# @Author : cAMP-Cascade-DNN
# @File : Face_Rec.py
# @Software : Pycharm
# @Contact: qq:1071747983
#          mail:wuxiaolong8001@163.com

'''# -*- 功能说明 -*-

调用此类后 根据传入的图片与yml训练数据进行识别 

'''  # -*- 功能说明 -*-

import os

from cv2 import cv2


class Face_Rec:
    def __init__(self):
        self.code_path = os.path.dirname(os.path.abspath(__file__))  # 获取代码路径
        self.project_path = os.path.dirname(self.code_path)  # 获取识别项目路径
        self.host_source_path = os.path.join(
            self.project_path, "Trainning result")  # 获取依赖数据路径
        self.person_source_path = os.path.join(
            self.project_path, "resources")  # 获取依赖数据路径
        self.train_path = os.path.join(
            self.host_source_path,
            "faceTrainer.yml")  # 获取训练数据保存路径

        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read(self.train_path)
        self.cvo = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
        self.cvo.load(
            os.path.join(self.person_source_path, 'haarcascade_frontalface_alt.xml'))

    def isHost(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.cvo.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=3,
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        if faces == ():  # 人脸坐标为空 即未检测到有人的存在
            return False, False, img
        else:
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                idnum, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])  # 生成预测id与置信度 对于LBPH 置信度应低于50
                if confidence <= 100:
                    id = "Host"
                    confidence = "{0}%".format(round(100 - confidence))
                else:
                    id = "Stranger"
                    confidence = "{0}%".format(round(100 - confidence))
                cv2.putText(img, str(id), (x + 5, y - 5), self.font, 1, (0, 0, 255), 3)
                # cv2.putText(img, str(confidence), (x + 5, y + h - 5), self.font, 1, (0, 0, 255), 3)
                if id == "Stranger":
                    return 1, False, img
                else:
                    return 1, True, img


if __name__ == "__main__":
    a = Face_Rec()
