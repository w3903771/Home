# -*- codeing = utf-8 -*-
# @Time : 2021-04-15 16:25
# @Author : cAMP-Cascade-DNN
# @File : remoteSSH.py
# @Software : Pycharm
# @Contact: qq:1071747983
#          mail:wuxiaolong8001@163.com

# -*- 功能说明 -*-

# 通过ssh协议，利用paramiko库进行对树莓派的远程命令控制

# -*- 功能说明 -*-
import paramiko


class SSH:
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
        stdin, stdout, stderr = self.ssh.exec_command('cd /home/pi/code' + ';' + command)
        # err_list = stderr.readlines()
        # if len(err_list) > 0:
        #     for err_content in err_list:
        #         print('ERROR:' + err_content)
        #     exit()
        # for item in stdout:
        #     print(item)
        # # 关闭连接
        self.ssh.close()

    def startFace(self):
        self.run('sudo sh runFace.sh')

    def startOther(self):
        self.run('sudo sh runOther.sh')

    def stopFace(self):
        self.run('sudo sh flag1.sh')

    def stopOther(self):
        self.run('sudo sh flag2.sh')

    def clear(self):
        self.run('sudo sh clear.sh')

    def clearFace(self):
        self.run('sudo sh clearFace.sh')

    def clearOther(self):
        self.run('sudo sh clearOther.sh')

if __name__ == "__main__":
    ssh = SSH()
    ssh.stopOther()
    # ssh.startFace()
    exit(1)
