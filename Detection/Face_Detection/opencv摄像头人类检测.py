import cv2

'''
调用opencv通过摄像头进行人脸检测
'''
def detect():
    # cvo = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    # cvo.load('C:/Anaconda3/envs/tensorflow/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    cvo = cv2.CascadeClassifier('haarcascade_upperbody.xml')
    cvo.load('C:/Anaconda3/envs/tensorflow/Lib/site-packages/cv2/data/haarcascade_upperbody.xml')
    cam = cv2.VideoCapture(0)

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
                minNeighbors=5  # 物体数
            )
            # 画框
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255,), 2)
            cv2.imshow("Camera", frame)
            if (cv2.waitKey(1) & 0xFF) == ord('q'):
                break
        else:
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    detect()
