# -*- codeing = utf-8 -*-
# @Time : 2021-04-12 15:25
# @Author : cAMP-Cascade-DNN
# @File : Face_Get.py
# @Software : Pycharm
# @Contact: qq:1071747983
#          mail:wuxiaolong8001@163.com

# -*- 功能说明 -*-

# 由人类采集窗口调用 仅用于采集主人人脸

import os

# -*- 功能说明 -*-
import cv2


class Face_Get:
    def __init__(self):
        self.cvo = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
        self.cvo.load(
            os.path.join(self.source_path, 'haarcascade_frontalface_alt2.xml'))

        self.code_path = os.path.dirname(os.path.abspath(__file__))  # 获取代码路径
        self.project_path = os.path.dirname(self.code_path)  # 获取识别项目路径
        self.source_path = os.path.join(
            self.project_path, "resources")  # 获取依赖数据路径
        self.photo_path = os.path.join(
            self.source_path, "face_trainning_images")  # 获取图片保存路径

        self.cam = cv2.VideoCapture(0)
        self.count = 0
        self.fpsc = 0

    def capture(self):
        while True:
            # 从摄像头读取图片
            sucess, img = self.cam.read()
            self.fpsc += 1
            # 转为灰度图片
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 检测人脸
            faces = self.cvo.detectMultiScale(
                gray,  # 灰度图片
                scaleFactor=1.3,  # 补偿参数
                minNeighbors=5,  # 物体数
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            for (x, y, w, h) in faces:
                if (self.fpsc % 2 == 0):
                    # 调整图像大小
                    new_frame = cv2.resize(img[y:y + h, x:x + w], (100, 140))
                    self.count += 1
                    path = os.path.join(self.photo_path, '%s.jpg' % (self.count))
                    # 保存图像
                    cv2.imwrite(path, new_frame)
            if self.count >= 30:  # 得到1000个样本后退出摄像
                break
        self.cam.release()
        cv2.destroyAllWindows()
