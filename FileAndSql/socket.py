# -*- codeing = utf-8 -*-
# @Time : 2021-04-22 16:18
# @Author : cAMP-Cascade-DNN
# @File : socket.py
# @Software : Pycharm
# @Contact: qq:1071747983
#          mail:wuxiaolong8001@163.com

# -*- 功能说明 -*-

# socket服务端类 对三种传感器消息进行分类处理并返回数值
import struct
import sys
import socket


# -*- 功能说明 -*-
class socket:
    def __init__(self):
        # 建立一个服务端
        self.host = socket.gethostname()  # 获取本地主机名
        self.port = 8001
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 服务器之间网络通信 流式TCP
        try:
            self.server.bind((self.host, self.port))  # 绑定要监听的端口
            self.server.listen(5)  # 开始监听 表示可以使用五个链接排队
        except socket.error as msg:
            print(msg)

    def get(self):
        while True:  # 接受新的conn套接字
            conn, addr = self.server.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
            print(conn, addr)
            while True:
                data = conn.recv(1024)  # 接收数据
                head_size = struct.calcsize('')  # 设置头消息大小
                head = conn.recv(head_size)  # 接受头消息 图片/传感器 传感器标号
                flag = struct.unpack('', head)

                print('recive:', data.decode())  # 打印接收到的数据
                conn.send(data.upper())  # 然后再发送数据
            conn.close()
