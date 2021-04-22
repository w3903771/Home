# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys

import cv2

sys.path.append("..")
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, QThread, QTimer, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

from Detection.Face_Detection.Face_Rec import *
from FileAndSql.remoteSSH import SSH
from FileAndSql.fileAndLog import fileAndLog
from imageCollect import imageCollect
import resource_qrc_rc

count = 0  # 人脸检测数清0
detecttime = 0  # 人脸检测起始时间清0


class Ui_doorWindow(object):

    def setupUi(self, doorWindow):
        doorWindow.setObjectName("doorWindow")
        doorWindow.resize(1080, 800)
        doorWindow.setStyleSheet("#doorWindow{border-image: url(:/Resources/background.png);}\n""")
        self.centralwidget = QtWidgets.QWidget(doorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 16, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 17, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 19, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 8, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 18, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 12, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 0, 20, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 4, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 0, 6, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 0, 7, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 0, 23, 1, 1)
        self.ErrorText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ErrorText.setObjectName("ErrorText")
        self.gridLayout.addWidget(self.ErrorText, 15, 1, 1, 12)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem14, 1, 0, 1, 1)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 3, 1, 1, 1)
        self.NormalFace = QtWidgets.QLabel(self.centralwidget)
        self.NormalFace.setFrameShape(QtWidgets.QFrame.Box)
        self.NormalFace.setText("")
        self.NormalFace.setObjectName("NormalFace")
        self.gridLayout.addWidget(self.NormalFace, 2, 14, 14, 9)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 0, 9, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem16, 14, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem17, 7, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem18, 10, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem19, 16, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem20, 0, 11, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem21, 0, 13, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem22, 0, 5, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem23, 9, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setMinimumSize(QtCore.QSize(100, 60))
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 16, 15, 3, 4)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem24, 0, 12, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem25, 0, 15, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem26, 5, 0, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem27, 0, 1, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setEnabled(False)
        self.stopButton.setMinimumSize(QtCore.QSize(100, 60))
        self.stopButton.setObjectName("stopButton")
        self.gridLayout.addWidget(self.stopButton, 16, 19, 3, 1)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem28, 15, 0, 1, 1)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 1, 14, 1, 1)
        self.ErrorFace = QtWidgets.QLabel(self.centralwidget)
        self.ErrorFace.setFrameShape(QtWidgets.QFrame.Box)
        self.ErrorFace.setText("")
        self.ErrorFace.setObjectName("ErrorFace")
        self.gridLayout.addWidget(self.ErrorFace, 4, 1, 10, 12)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem29, 0, 10, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem30, 0, 14, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem31, 17, 0, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem32, 0, 3, 1, 1)
        spacerItem33 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem33, 6, 0, 1, 1)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem34, 0, 21, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem35, 13, 0, 1, 1)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem36, 0, 18, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem37, 0, 22, 1, 1)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem38, 0, 4, 1, 1)
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 14, 1, 1, 1)
        spacerItem39 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem39, 8, 0, 1, 1)
        spacerItem40 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem40, 0, 0, 1, 1)
        self.registButton = QtWidgets.QPushButton(self.centralwidget)
        self.registButton.setMinimumSize(QtCore.QSize(100, 60))
        self.registButton.setObjectName("registButton")
        self.gridLayout.addWidget(self.registButton, 16, 20, 3, 1)
        spacerItem41 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem41, 11, 0, 1, 1)
        self.Button_OpenPhoto = QtWidgets.QPushButton(self.centralwidget)
        self.Button_OpenPhoto.setMinimumSize(QtCore.QSize(100, 60))
        self.Button_OpenPhoto.setObjectName("Button_OpenPhoto")
        self.gridLayout.addWidget(self.Button_OpenPhoto, 16, 7, 3, 6)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        doorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(doorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        doorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(doorWindow)
        self.statusbar.setObjectName("statusbar")
        doorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(doorWindow)
        QtCore.QMetaObject.connectSlotsByName(doorWindow)



    def retranslateUi(self, doorWindow):
        _translate = QtCore.QCoreApplication.translate
        doorWindow.setWindowTitle(_translate("doorWindow", "智能门禁"))
        self.label2.setText(_translate("doorWindow", "人脸检测显示窗口"))
        self.startButton.setText(_translate("doorWindow", "开始检测"))
        self.stopButton.setText(_translate("doorWindow", "停止检测"))
        self.label1.setText(_translate("doorWindow", "实时监控窗口"))
        self.label3.setText(_translate("doorWindow", "异常人脸记录："))
        self.registButton.setText(_translate("doorWindow", "主人人脸记录"))
        self.Button_OpenPhoto.setText(_translate("doorWindow", "查看异常人脸记录"))


class MyThread(QObject):
    startsig = pyqtSignal(int)  # 开始识别信号
    endsig = pyqtSignal(int, int)  # 识别结束 界面更新信号

    def __init__(self):
        super(MyThread, self).__init__()
        self.facerec = Face_Rec()

    def work(self, f):
        if f == 1:
            global img2
            flag, ishost, img2 = self.facerec.isHost(img1)
            self.endsig.emit(flag, ishost)  # 采用信号可使线程自动结束


class MainWindow(QtWidgets.QMainWindow, Ui_doorWindow):  # 继承qtdesiner的MinWindow 确保window为qtwidgets 不然massagebox无法启用

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.code_path = os.path.dirname(os.path.abspath(__file__))  # 获取代码路径
        self.project_path = os.path.dirname(self.code_path)  # 获取识别项目路径
        self.photo_path = r'\\192.168.137.69\pi\share\faceImage'
        self.source_path = os.path.join(
            self.project_path, "Resources")  # 获取依赖数据路径
        self.errors_path = os.path.join(
            self.source_path, "Errors")  # 获取依赖数据路径
        self.imagePath = os.path.join(self.photo_path, r'1.jpg')

        # 设置按钮响应
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.Button_OpenPhoto.clicked.connect(self.open)
        self.registButton.clicked.connect(self.collect)

        self.thread = QThread()
        self.myThread = MyThread()
        self.myThread.moveToThread(self.thread)
        self.myThread.startsig.connect(self.myThread.work)
        self.myThread.endsig.connect(self.update)
        self.thread.start()

        self.ssh = SSH()
        self.log = fileAndLog()
        self.timer = QTimer()
        self.timer.timeout.connect(self.run)

    def run(self):
        if len(os.listdir(self.photo_path)) == 1:
            global img1
            img1 = cv2.imread(self.imagePath)
            # height, width, bytesPerComponent = img1.shape
            # bytesPerLine = bytesPerComponent * width
            # show = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
            # showImage = QImage(show.data, width, height, bytesPerLine,
            #                    QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
            self.NormalFace.setPixmap(
                QPixmap(self.imagePath).scaled(493, 572))
            QApplication.processEvents()
            self.myThread.startsig.emit(1)
            os.remove(self.imagePath)

    def start(self):

        self.startButton.setEnabled(False)  # 禁止重复开始
        self.stopButton.setEnabled(True)
        self.ssh.startFace()
        time.sleep(2)
        self.timer.start(500)

    def update(self, flag, ishost):
        global detecttime, count
        if flag:
            height, width, bytesPerComponent = img2.shape
            bytesPerLine = bytesPerComponent * width
            show = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
            showImage = QImage(show.data, width, height, bytesPerLine,
                               QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
            self.ErrorFace.setPixmap(
                QPixmap.fromImage(showImage).scaled(466, 298))
        else:
            self.ErrorFace.clear()
        QApplication.processEvents()
        if flag and ishost:
            print(time.time() - detecttime, count)
            if detecttime == 0:  # 起始时间未记录则记录开始检测到人脸的时间
                detecttime = time.time()
            count = count + 1
            if time.time() - detecttime > 120 and count > 100:  # 停留时间超过2分钟 识别次数超过20次 记录为异常
                count = 0
                detecttime = 0
                logtext = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                logtext += " 图像检测发现有陌生人长期停留"
                self.log.save(img1, 1)  # 保存图片，写入日志
                self.ErrorText.appendPlainText(logtext)  # 插入窗口日志

            elif time.time() - detecttime > 180 and count < 5:  # 无人或正常人经过 记录清空
                count = 0
                detecttime = 0

    def stop(self):
        replay = QMessageBox.question(self, "", "确认停止嘛", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if replay == QMessageBox.Yes:
            self.ssh.stopFace()  # 树莓派结束拍摄
            self.timer.stop()  # 结束识别
            self.NormalFace.clear()
            self.ErrorFace.clear()
            self.ssh.clear()  # 清空文件夹
            self.startButton.setEnabled(True)
            self.stopButton.setEnabled(False)

    def collect(self):
        self.imageget = imageCollect()
        self.imageget.show()

    def closeEvent(self, event):
        self.ssh.stopFace()
        self.ssh.clear()  # 清空文件夹
        event.accept()

    def open(self):
        os.system("explorer.exe %s" % self.errors_path)

class doorWindow(QMainWindow):
    def __init__(self):
        QDialog.__init__(self)
        super().__init__()
        self.child = MainWindow()
        self.child.setupUi(self)
