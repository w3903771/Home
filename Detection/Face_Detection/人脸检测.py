#-*- codeing = gbk -*-
import os

import cv2


def recognize():

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path=input("请输入训练数据保存路径: ")
    path=os.path.join(path,"trainer.yml")
    recognizer.read(path)
    cvo = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    cvo.load('C:/Anaconda3/envs/tensorflow/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    font = cv2.FONT_HERSHEY_SIMPLEX

    idnum = 0

    names = [u'吴小龙', 'Bob']

    cam = cv2.VideoCapture(0)
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = cvo.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
            flags = cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
            idnum, confidence = recognizer.predict(gray[y:y+h, x:x+w])
            if confidence < 100:
                idnum = names[idnum-1]
                confidence = "{0}%".format(round(100 - confidence))
            else:
                idnum = "unknown"
                confidence = "{0}%".format(round(100 - confidence))

            cv2.putText(img, str(idnum), (x+5, y-5), font, 1, (0, 0, 255), 3)
            cv2.putText(img, str(confidence), (x+5, y+h-5), font, 1, (0, 0, 255), 3)

        cv2.imshow('Camera', img)
        k = cv2.waitKey(10)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    recognize()