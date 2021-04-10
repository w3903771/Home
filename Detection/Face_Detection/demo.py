import os

import cv2

'''
通过摄像头进行视频保存
'''
def capture():
    name = input('my name:')
    path = os.path.join(name, "../video")
    if not os.path.isdir(path):
        os.mkdir(path) # 创建文件夹

    cvo = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    cvo.load('C:/Anaconda3/envs/tensorflow/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')

    cam = cv2.VideoCapture(0)
    width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cam.get(cv2.CAP_PROP_FPS)  # 获取视频的帧率
    fourcc = int(cam.get(cv2.CAP_PROP_FOURCC))  # 编码
    count = 1

    while cam.isOpened():
        # 读取摄像头
        ret, frame = cam.read()
        if ret == True:
            # 灰度
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 识别面部
            faces = cvo.detectMultiScale(
                gray,  # 灰度图片
                scaleFactor=1.3,  # 补偿参数
                minNeighbors=5,  # 物体数
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            # 画框
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255,), 2)
                new_frame = cv2.resize(frame[y:y + h, x:x + w], (92, 112))  # 剪切的新图
                cv2.imwrite('%s/%s.png' % (path, str(count)), new_frame)
                count + 1
            newname="My Camera"+str(count)
            cv2.imshow(newname, frame)
            print(count)
            if (cv2.waitKey(1) & 0xFF) == ord('q'):
                break
        else:
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    capture()
