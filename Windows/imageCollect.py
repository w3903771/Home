# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageCollect.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import sys

import cv2
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow

from Detection.Face_Detection.Face_Trains import Face_Trains

sys.path.append("..")


class Ui_imageCollect(object):
    def __init__(self):

        self.windows_path = os.path.dirname(
            os.path.abspath(__file__))  # 获取文件夹路径\\192.168.137.69\pi\share
        self.project_path = os.path.dirname(self.windows_path)  # 获取识别项目路径
        self.detection_path = os.path.join(
            self.project_path, "Detection")  # 获取依赖数据路径
        self.source_path = os.path.join(  # 获取资源文件夹路径
            self.detection_path, "resources")
        self.photo_path = os.path.join(
            self.source_path, "face_trainning_images")  # 获取图片保存路径

        self.cvo = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
        self.cvo.load(
            os.path.join(self.source_path, 'haarcascade_frontalface_alt2.xml'))
        self.train = Face_Trains

    def setupUi(self, imageCollect):
        imageCollect.setObjectName("imageCollect")
        imageCollect.resize(558, 647)
        self.centralwidget = QtWidgets.QWidget(imageCollect)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 451, 481))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(200, 530, 161, 51))
        self.startButton.setObjectName("startButton")
        imageCollect.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(imageCollect)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 26))
        self.menubar.setObjectName("menubar")
        imageCollect.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(imageCollect)
        self.statusbar.setObjectName("statusbar")
        imageCollect.setStatusBar(self.statusbar)

        self.retranslateUi(imageCollect)
        QtCore.QMetaObject.connectSlotsByName(imageCollect)

        # 设置按钮响应
        self.startButton.clicked.connect(self.start)

    def retranslateUi(self, imageCollect):
        _translate = QtCore.QCoreApplication.translate
        imageCollect.setWindowTitle(_translate("imageCollect", "智能门禁"))
        self.startButton.setText(_translate("imageCollect", "开始检测"))

    def start(self):
        cam = cv2.VideoCapture(0)
        count = 0
        fpsc = 0
        while True:
            # 从摄像头读取图片
            sucess, img = self.cam.read()
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
                    path = os.path.join(
                        self.photo_path, '%s.jpg' %
                                         (self.count))
                    # 保存图像
                    cv2.imwrite(path, new_frame)
            if self.count >= 30:  # 得到30个样本后退出摄像
                break
        self.cam.release()
        cv2.destroyAllWindows()

        flag = self.train.train()
        if flag == 1:  # 图片训练异常 弹出异常提示
            pass
        elif flag == 0:  # 图片训练完成 退出
            return 0


class imageCollect(QMainWindow):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_imageCollect()
        self.child.setupUi(self)
