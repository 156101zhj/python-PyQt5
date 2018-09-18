# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from socket import *
import multiprocessing as mp
import os
import signal
import sys
import time

# 文件库
FILE_PATH = "C:/Users/admin/Desktop/"

# 服务器功能


class TftpServer(object):

    def __init__(self, connfd):
        self.connfd = connfd

    def handler(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data[0] == 'Q':
                print(self.connfd.getpeername, "客户端退出")
                self.connfd.close()
                sys.exit(0)
            elif data[0] == "L":
                self.do_list()
            elif data[0] == "G":
                filename = data[2:]
                self.do_get(filename)
            elif data[0] == "P":
                filename = data[2:]
                self.do_put(filename)

    def do_list(self):
        # 获取列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        files = ""
        for file in file_list:
            if file[0] != '.' and \
                    os.path.isfile(FILE_PATH + file):
                files = files + file + '#'
        # 发送给客户端
        self.connfd.send(files.encode())

    def do_get(self, filename):
        try:
            fd = open(FILE_PATH + filename, 'rb')
        except:
            self.connfd.send("文件不存在".encode())
            return
        self.connfd.send(b'OK')
        time.sleep(0.1)

        # 发送文件
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

        print("文件发送完成")

    def do_put(self, filename):
        try:
            fd = open(FILE_PATH + filename, 'wb')
        except:
            self.connfd.send("无法上传".encode())
            return
        self.connfd.send(b'OK')

        while True:
            data = self.connfd.recv(1024)
            if data == b"##":
                break
            fd.write(data)
        fd.close()
        print("上传完毕")

# 控制程序流程　创建套接字，接收链接，创建子进程


def main():
    HOST = "0.0.0.0"
    PORT = 8888
    ADDR = (HOST, PORT)

    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    print("Listen to port 8888....")
    # signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            connfd, addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit("退出服务器")
        except Exception as e:
            print(e)
            continue
        print("客户端登录：", addr)
        tftp = TftpServer(connfd)
        p = mp.Process(target=tftp.handler)
        p.start()
        time.sleep(0.1)
        p.join()

if __name__ == "__main__":
    main()
