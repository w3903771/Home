# -*- codeing = utf-8 -*-
# @Time : 2021-04-15 16:25
# @Author : cAMP-Cascade-DNN
# @File : remoteSHH.py
# @Software : Pycharm
# @Contact: qq:1071747983
#          mail:wuxiaolong8001@163.com

# -*- 功能说明 -*-

# 通过ssh协议，利用paramiko库进行对树莓派的远程命令控制

# -*- 功能说明 -*-
import paramiko


class SHH:
    def __init__(self):
        # 输入用户名、密码、ip等
        self.ip = "192.168.137.69"
        self.port = 22
        self.user = "pi"
        self.password = "raspberry"
        # 创建一个ssh对象
        self.ssh = paramiko.SSHClient()
        # 自动选择yes
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def run(self, command):
        # 建立连接
        self.ssh.connect(self.ip, self.port, self.user, self.password, timeout=10)
        stdin, stdout, stderr = self.ssh.exec_command(command)
        err_list = stderr.readlines()
        if len(err_list) > 0:
            for err_content in err_list:
                print('ERROR:' + err_content)
            exit()
        for item in stdout:
            print(item)
        # 关闭连接
        self.ssh.close()

    def clear(self):
        # 建立连接
        self.ssh.connect(self.ip, self.port, self.user, self.password, timeout=10)
        command1 = 'rm -f ' + self.remotepath  # 清空共享文件夹
        command2 = 'mkdir' + self.remotepath  # 重建文件夹
        command3 = 'mkdir ' + self.remotepath + '\faceImage'
        command4 = 'mkdir ' + self.remotepath + '\otherImage'
        command = []
        command.append(command1)
        command.append(command2)
        command.append(command3)
        command.append(command4)
        for i in range(1, 5):
            stdin, stdout, stderr = self.ssh.exec_command(command[i])
            # 输出命令执行结果
            err_list = stderr.readlines()
            if len(err_list) > 0:
                for err_content in err_list:
                    print('ERROR:' + err_content)
                exit()
            for item in stdout:
                print(item)
        # 关闭连接
        self.ssh.close()
