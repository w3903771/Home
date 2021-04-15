# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kitchenWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow

sys.path.append("..")


class Ui_kitchenWindow(object):
    def setupUi(self, kitchenWindow):
        kitchenWindow.setObjectName("kitchenWindow")
        kitchenWindow.resize(1081, 812)
        kitchenWindow.setStyleSheet("#kitchenWindow{border-image: url(:/Resources/FireRecognition.jpg);}")
        self.centralwidget = QtWidgets.QWidget(kitchenWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(580, 20, 451, 731))
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.label_2 = QtWidgets.QLabel(self.frame2)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame2)
        self.label_3.setGeometry(QtCore.QRect(20, 510, 91, 21))
        self.label_3.setObjectName("label_3")
        self.Button_OpenPhoto = QtWidgets.QPushButton(self.frame2)
        self.Button_OpenPhoto.setGeometry(QtCore.QRect(170, 680, 101, 41))
        self.Button_OpenPhoto.setObjectName("Button_OpenPhoto")
        self.ErrorText = QtWidgets.QPlainTextEdit(self.frame2)
        self.ErrorText.setGeometry(QtCore.QRect(10, 530, 421, 141))
        self.ErrorText.setObjectName("ErrorText")
        self.ErrorImageLable = QtWidgets.QLabel(self.frame2)
        self.ErrorImageLable.setGeometry(QtCore.QRect(10, 50, 421, 441))
        self.ErrorImageLable.setFrameShape(QtWidgets.QFrame.Box)
        self.ErrorImageLable.setText("")
        self.ErrorImageLable.setIndent(6)
        self.ErrorImageLable.setObjectName("ErrorImageLable")
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(10, 10, 561, 731))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.label_1 = QtWidgets.QLabel(self.frame1)
        self.label_1.setGeometry(QtCore.QRect(30, 20, 121, 31))
        self.label_1.setObjectName("label_1")
        self.TemperatureLable = QtWidgets.QLabel(self.frame1)
        self.TemperatureLable.setGeometry(QtCore.QRect(30, 70, 41, 18))
        self.TemperatureLable.setTextFormat(QtCore.Qt.AutoText)
        self.TemperatureLable.setObjectName("TemperatureLable")
        self.SmogLable = QtWidgets.QLabel(self.frame1)
        self.SmogLable.setGeometry(QtCore.QRect(230, 70, 41, 18))
        self.SmogLable.setObjectName("SmogLable")
        self.GasLable = QtWidgets.QLabel(self.frame1)
        self.GasLable.setGeometry(QtCore.QRect(330, 70, 41, 18))
        self.GasLable.setObjectName("GasLable")
        self.FireLable = QtWidgets.QLabel(self.frame1)
        self.FireLable.setGeometry(QtCore.QRect(430, 70, 41, 18))
        self.FireLable.setObjectName("FireLable")
        self.NormalImageLable = QtWidgets.QLabel(self.frame1)
        self.NormalImageLable.setGeometry(QtCore.QRect(20, 60, 521, 551))
        self.NormalImageLable.setFrameShape(QtWidgets.QFrame.Box)
        self.NormalImageLable.setText("")
        self.NormalImageLable.setObjectName("NormalImageLable")
        self.stopButton = QtWidgets.QPushButton(self.frame1)
        self.stopButton.setGeometry(QtCore.QRect(340, 630, 131, 61))
        self.stopButton.setObjectName("stopButton")
        self.startButton = QtWidgets.QPushButton(self.frame1)
        self.startButton.setGeometry(QtCore.QRect(110, 630, 131, 61))
        self.startButton.setObjectName("startButton")
        self.HumidityLable = QtWidgets.QLabel(self.frame1)
        self.HumidityLable.setGeometry(QtCore.QRect(130, 70, 41, 18))
        self.HumidityLable.setObjectName("HumidityLable")
        self.Temperature = QtWidgets.QLabel(self.frame1)
        self.Temperature.setGeometry(QtCore.QRect(80, 70, 51, 18))
        self.Temperature.setLineWidth(1)
        self.Temperature.setObjectName("Temperature")
        self.Humidity = QtWidgets.QLabel(self.frame1)
        self.Humidity.setGeometry(QtCore.QRect(180, 70, 51, 18))
        self.Humidity.setLineWidth(1)
        self.Humidity.setObjectName("Humidity")
        self.Smog = QtWidgets.QLabel(self.frame1)
        self.Smog.setGeometry(QtCore.QRect(280, 70, 51, 18))
        self.Smog.setLineWidth(1)
        self.Smog.setObjectName("Smog")
        self.Fire = QtWidgets.QLabel(self.frame1)
        self.Fire.setGeometry(QtCore.QRect(480, 70, 51, 18))
        self.Fire.setLineWidth(1)
        self.Fire.setObjectName("Fire")
        self.Gas = QtWidgets.QLabel(self.frame1)
        self.Gas.setGeometry(QtCore.QRect(380, 70, 51, 18))
        self.Gas.setLineWidth(1)
        self.Gas.setObjectName("Gas")
        self.NormalImageLable.raise_()
        self.label_1.raise_()
        self.stopButton.raise_()
        self.startButton.raise_()
        self.TemperatureLable.raise_()
        self.SmogLable.raise_()
        self.GasLable.raise_()
        self.HumidityLable.raise_()
        self.FireLable.raise_()
        self.Temperature.raise_()
        self.Humidity.raise_()
        self.Smog.raise_()
        self.Fire.raise_()
        self.Gas.raise_()
        kitchenWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(kitchenWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1081, 26))
        self.menubar.setObjectName("menubar")
        kitchenWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(kitchenWindow)
        self.statusbar.setObjectName("statusbar")
        kitchenWindow.setStatusBar(self.statusbar)

        self.retranslateUi(kitchenWindow)
        QtCore.QMetaObject.connectSlotsByName(kitchenWindow)

    def retranslateUi(self, kitchenWindow):
        _translate = QtCore.QCoreApplication.translate
        kitchenWindow.setWindowTitle(_translate("kitchenWindow", "智能厨房"))
        self.label_2.setText(_translate("kitchenWindow", "异常显示窗口"))
        self.label_3.setText(_translate("kitchenWindow", "异常日志："))
        self.Button_OpenPhoto.setText(_translate("kitchenWindow", "查看异常图片"))
        self.label_1.setText(_translate("kitchenWindow", "检测显示窗口"))
        self.TemperatureLable.setText(_translate("kitchenWindow", "温度："))
        self.SmogLable.setText(_translate("kitchenWindow", "烟雾："))
        self.GasLable.setText(_translate("kitchenWindow", "燃气："))
        self.FireLable.setText(_translate("kitchenWindow", "火焰："))
        self.stopButton.setText(_translate("kitchenWindow", "停止检测"))
        self.startButton.setText(_translate("kitchenWindow", "开始检测"))
        self.HumidityLable.setText(_translate("kitchenWindow", "湿度："))
        self.Temperature.setText(_translate("kitchenWindow", "NULL"))
        self.Humidity.setText(_translate("kitchenWindow", "NULL"))
        self.Smog.setText(_translate("kitchenWindow", "NULL"))
        self.Fire.setText(_translate("kitchenWindow", "NULL"))
        self.Gas.setText(_translate("kitchenWindow", "NULL"))

class kitchenWindow(QMainWindow):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_kitchenWindow()
        self.child.setupUi(self)