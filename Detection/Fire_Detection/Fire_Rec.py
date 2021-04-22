import cv2
import os

redThre = 115
saturationTh = 45  # 饱和度 为HIS颜色空间概念


class Fire_Recognition:

    def fire_reconfnition(self, image):
        image_h, image_w, image_c = image.shape  # 图片长 宽 位深
        image_B, image_G, image_R = cv2.split(image)  # 通道拆分 cv2按bgr顺序保存
        image_B = image_B.tolist()  # 矩阵转换为列表
        image_R = image_R.tolist()
        image_G = image_G.tolist()

        image_fire = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转化为灰度图像

        for i in range(image_h):
            for j in range(image_w):
                R = image_R[i][j]
                G = image_G[i][j]
                B = image_B[i][j]
                image_max = max(image[i][j])
                image_min = min(image[i][j])
                allrgb = int(R) + int(G) + int(B)

                if allrgb != 0:
                    s = (1 - 3.0 * image_min / allrgb)  # HSI中饱和度s的计算 即颜色深度
                else:
                    s = 1  # r+g+b为0 图像为黑色 饱和度为1
                # print('s=%s'%s,'st=%s'%((255 - R) * saturationTh / redThre))
                '''
                RGB 判据
                rule1: R>=G>=B
                rule2: R>=RT
                rule3: S>=((255-R)*ST/RT)
                '''
                if (R > redThre
                        and R >= G >= B
                        and s > 0.20
                        and s > ((255 - R) * saturationTh / redThre)):
                    image_fire[i][j] = 255
                else:
                    image_fire[i][j] = 0
        '''
        二值化处理 retVal（得到的阈值值）,image(阈值化后的图像)=cv2.threshould(原图片,阈值, 填充色, 阈值类型) 
        此处是黑白二值 高于阈值0（白）即为255（黑）
        '''
        score, mid_picture = cv2.threshold(image_fire, 0, 255, cv2.THRESH_BINARY)
        '''
         findContours二值图像轮廓检测函数
           mod：检测轮廓的方法。有四种方法。
            —CV_RETR_EXTERNAL：只检测外轮廓。忽略轮廓内部的洞。
            —CV_RETR_LIST：检测所有轮廓，但不建立继承(包含)关系。
            —CV_RETR_TREE：检测所有轮廓，并且建立所有的继承(包含)关系
            —CV_RETR_CCOMP：检测所有轮廓，但是仅仅建立两层包含关系。外轮廓放到顶层，外轮廓包含的第一层内轮廓放到底层，
            如果内轮廓还包含轮廓，那就把这些内轮廓放到顶层去。
            
          method：表示一条轮廓的方法。
            – CV_CHAIN_APPROX_NONE：把轮廓上所有的点存储。
            – CV_CHAIN_APPROX_SIMPLE：只存储水平，垂直，对角直线的起始点。对drawContours函数来说，这两种方法没有区别。
        '''
        contours, point = cv2.findContours(mid_picture, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # Rect boundingRect(InputArray points)获得由points点集构成的包围轮廓的最小正矩形
        bounding_boxs = [cv2.boundingRect(cnt) for cnt in contours]
        for member in bounding_boxs:
            [x, y, w, h] = member
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # cv2.imshow("erzhi", image) #有框的原图
        # cv2.imshow("fire", image_fire) #黑白图
        # cv2.waitKey(1)
        print(len(bounding_boxs))
        if len(bounding_boxs) >= 16:
            return True, image
        else:
            return False, image
