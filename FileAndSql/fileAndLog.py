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
            t = time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{mm}%S{s}').format(y='年', m='月', d='日', h='时', mm='分', s='秒')
            image_path = os.path.join(self.errors_path, "%s 检测到陌生人.jpg" % (t))
            cv2.imencode('.jpg', img)[1].tofile(image_path)
            test_path = self.errors_path + "\errorlog.txt"

            f = open(test_path, "a")
            f.write(t + " 图像检测发现有陌生人长期停留\n")

        if flag == 2:
            # t = time.strftime(r"%Y年%m月%d日 %H时%M分%S秒",)
            t = time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{mm}%S{s}').format(y='年', m='月', d='日', h='时', mm='分', s='秒')
            image_path = os.path.join(self.errors_path, "%s 检测到火焰.jpg" % (t))
            cv2.imencode('.jpg', img)[1].tofile(image_path)
            test_path = self.errors_path + "\errorlog.txt"

            f = open(test_path, "a")
            f.write(t + " 图像检测发现有火焰\n")


if __name__ == '__main__':
    a = fileAndLog()
    a.save(1, 1)
