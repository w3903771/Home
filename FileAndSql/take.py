# -*- codeing = utf-8 -*-
# @Time : 2021-04-16 0:41
# @Author : cAMP-Cascade-DNN
# @File : take.py
# @Software : Pycharm
# @Contact: qq:1071747983
#          mail:wuxiaolong8001@163.com

# -*- 功能说明 -*-

# 调用摄像头 拍摄20张照片并返回图片元组

# -*- 功能说明 -*-

import cv2


class take:
    def __init__(self, name):
        # 初期化USB摄像头
        self.cap = cv2.VideoCapture(name)
        self.cap.set(
            cv2.CAP_PROP_FOURCC,
            cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))  # 视频流格式
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.imamge = []
        self.count = 0

    def get(self):
        while True:
            ret, frame = self.cap.read()
            cv2.imshow('Capture', frame)
            self.count += 1
            self.imamge.append(frame)
            if self.count == 20:
                break
            if cv2.waitKey(1) & 0x00FF == ord('q'):
                break
            # 释放资源和关闭窗口
        print(self.count)
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    t = take()
    t.get()
