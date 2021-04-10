import os

import cv2


def capture(des, id):
    cvo = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    cvo.load('C:/Anaconda3/envs/tensorflow/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    cam = cv2.VideoCapture(0)
    count = 0
    fpsc=0

    while True:
        # 从摄像头读取图片
        sucess, img = cam.read()
        fpsc+=1
        # 转为灰度图片
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 检测人脸
        faces = cvo.detectMultiScale(
            gray,  # 灰度图片
            scaleFactor=1.3,  # 补偿参数
            minNeighbors=5,  # 物体数
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255,), 2)
            if(fpsc%2==0):
                # 调整图像大小
                new_frame = cv2.resize(gray[y:y + h, x:x + w], (100, 140))
                count += 1
                print('保存第 %s 张图像' % count)
                path = os.path.join(des, '%s.%s.jpg' % (id, count))
                print('save_image_dir: ', path)
                # 保存图像
                cv2.imwrite(path, new_frame)
        cv2.imshow('Video', img)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
        elif count >= 60:  # 得到1000个样本后退出摄像
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    des = input("请输入将要保存的图片路径: ")
    id = input("请输入用户ID: ")
    if not os.path.isdir(des):
        os.mkdir(des)  # 创建文件夹
    capture(des, id)
