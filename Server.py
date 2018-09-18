# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# import gevent
# from gevent import monkey
# monkey.patch_all()  # 必须在引入socket之前调用
from socket import *
import time
import sys
import threading
from select import *
import module.mysqlRoot as Conn

import json
import urllib.request

STATIC_DIR = './static'  # 存放文件上传的路径
ADDR = ("0.0.0.0", 8025)

clients = {}  # 记录在线的客户端的套接字
connects = {}  # 将聊天双方的套接字绑定在一起

rlist = []
wlist = []
xlist = []

class Root_Server(object):

    def __init__(self, addr):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(addr)
        self.sockfd.listen(5)

        Conn.main()

        self.tuling_th = []
        self.api_url = "http://openapi.tuling123.com/openapi/api/v2"

        rlist.append(self.sockfd)
        xlist.append(self.sockfd)

    def serve_forever(self):
        while True:
            print("等待root客户端连接...")
            rs, ws, xs = select(rlist, wlist, xlist)
            print(rs)
            for r in rs:
                if r is self.sockfd:
                    connfd, addr = self.sockfd.accept()
                    print("有root客户端连接:", addr)
                    rlist.append(connfd)
                else:
                    self.handler(r)
                    # wlist.append(r)
            for x in xs:
                if x is self.sockfd:
                    x.close()

            # for w in ws:
            #     self.handler(w)
            #     wlist.remove(w)

    def handler(self, connfd):
        data = connfd.recv(1024).decode()
        print("handler>data:", data)
        if not data:
            rlist.remove(connfd)
            connfd.close()
        # "Q my_rootname" 退出
        elif data[0] == 'Q':
            my_rootname = data.split(' ')[1]
            print(connfd.getpeername(), "root客户端退出")
            self.quit(connfd, my_rootname)
        # "L my_rootname pwd" 登录
        elif data[0] == "L":
            my_rootname = data.split(' ')[1]
            pwd = data.split(' ')[-1]
            self.login(connfd, my_rootname, pwd)

        elif data[0] == "Z":
            info_dict = json.loads(connfd.recv(4096).decode())
            self.zhuce(info_dict)

        elif data[0] == "T":
            msg = data[2:]

            my_info_dict = json.loads(connfd.recv(4096).decode())
            print("handler>T>my_info_dict",my_info_dict)
            Tl = threading.Thread(
                target=self.get_turing_text, args=(connfd, msg, my_info_dict))
            self.tuling_th.append(Tl)
            Tl.start()
        # "C friend_rootname" 将好友和自己绑定
        elif data[0] == "C":
            # Tl.join()
            my_rootname = data.split(' ')[1]
            friend_rootname = data.split(' ')[2]
            self.chat(connfd, my_rootname, friend_rootname)

        elif data[0] == "F":
            rootname = data.split(" ")[1]
            f_rootname = data.split(" ")[2]
            self.select_id(connfd, rootname, f_rootname)

        elif data[0] == "V":
            rootname = data.split(" ")[1]
            f_rootname = data.split(" ")[2]
            self.del_id(connfd, rootname, f_rootname)

        elif data[0] == "P":
            rootname = data.split(" ")[-1]
            self.friends_list(connfd, rootname)

        else:
            my_rootname = data.split(' ')[0]
            print(">>", my_rootname)
            friend_rootname = data.split(' ')[1]
            print(">>", friend_rootname)

            msg = data[len(my_rootname) + len(friend_rootname) + 2:]
            print("..", msg)
            Conn.insert_history(my_rootname, friend_rootname, msg)

            print("chat>send")

            text = dict(zip(["type", "rootname", "msg"],
                            ["S", my_rootname, msg]))
            if friend_rootname in clients:
                connects[connfd].send(json.dumps(text).encode())
            else:
                clients[my_rootname].send(json.dumps(text).encode())

        # connfd.close()

    def friends_list(self,connfd, rootname):
        friends = Conn.select_friends(rootname)
        friends_list = [list(x) for x in friends]
        p = dict(zip(["type","friends_list"],["P",friends_list]))
        print("friend_list>",p)
        connfd.send(json.dumps(p).encode())


    def select_id(self, connfd, rootname, f_rootname):
        data = Conn.select_users(f_rootname)
        if data:
            connfd.send(json.dumps({"type":"F","info":data}).encode())
            Conn.insert_friends(rootname, f_rootname)
        else:
            connfd.send(json.dumps({"type": "F", "info": "nois"}).encode())

    def del_id(self, connfd, rootname, f_rootname):
        data = Conn.select_users(f_rootname)
        if data:
            connfd.send(json.dumps({"type":"V","info":data}).encode())
            Conn.delete_friends(rootname, f_rootname)
        else:
            connfd.send(json.dumps({"type": "V", "info": "nois"}).encode())

    def get_turing_text(self, connfd, text, my_info_dict):
        if text == "离线消息":
            miss_msg = Conn.selectlast_online_history(my_info_dict["last_online"], my_info_dict["rootname"])
            print("miss_msg>", miss_msg)
            if miss_msg == ():
                connfd.send(json.dumps(dict(zip(["type", "miss_msg"],
                                                ['M'] + [["你的离线消息为空哦~\n\n有什么话都可以对小Root说哦~\n"]]))).encode())
            else:
                connfd.send(json.dumps(dict(zip(["type", "miss_msg"],
                                                ['M'] + [[str(x[0]) for x in miss_msg] + [
                                                    "上面是您的好友给你发的离线消息哦~\n小Root还能帮你各种忙哦~" + "\n"]][::-1]))).encode())
        else:
            req = {
                "perception":
                    {
                        "inputText":
                            {
                                "text": text
                            },

                        "selfInfo":
                            {
                                "location":
                                    {
                                        "city": "武汉",
                                        "province": "湖北省",
                                        "street": "东湖"
                                    }
                            }
                    },

                "userInfo":
                    {
                        "apiKey": "dbecb8157b834e21b26a87cb67792788",
                        "userId": "OnlyUseAlphabet"
                    }
            }
            req = json.dumps(req).encode('utf8')

            http_post = urllib.request.Request(self.api_url, data=req, headers={
                                               'content-type': 'application/json'})
            response = urllib.request.urlopen(http_post)
            response_str = response.read().decode('utf8')
            # print(response_str)
            response_dic = json.loads(response_str)
            # print(response_dic)

            intent_code = response_dic['intent']['code']
            results_text = response_dic['results'][0]['values']['text']
            # print('Turing的回答：')
            # print('code：' + str(intent_code))
            # print('text：' + results_text)

            msg = "小Root  %02d:%02d:%02d" % time.localtime()[3:6] + '\n' + results_text + '\n'
            print(msg)
            text = dict(zip(["type", "rootname", "nickname", "msg"],
                            ["S", "1000", "小Root", msg]))
            connfd.send(json.dumps(text).encode())

    def login(self, connfd, rootname, pwd):
        my_info = Conn.login(rootname, pwd)
        print("login>my_info:", my_info)
        if my_info:
            connfd.send(b"True")
            clients[rootname] = connfd
            friends = Conn.select_friends(rootname)
            friends_list = [x for x in friends]
            print("friends_list",friends_list)
            connfd.send(json.dumps(friends_list).encode())

            my_info_dict = dict(zip(["type", "rootname", "nickname", "gender", "tel", "address", "email", "birthday", "avatar", "style", "onlinestatus", "last_online"],
                                    ["I"] + [str(x) for x in my_info]))
            time.sleep(1)
            connfd.send(json.dumps(my_info_dict).encode())

            Conn.updatestatus_users(rootname, "在线")
        else:
            connfd.send(b'False')

    def zhuce(self, info):
        Conn.insert_users(info["rootname"], info["nickname"], info["pwd"], info["gender"], info["tel"], info["address"], info["email"], info["birthday"], info["avatar"], info["style"],
                          info["onlinestatus"])

    def quit(self, connfd, my_rootname):

        del clients[my_rootname]

        print("quit>clients",clients)
        print("quit>connects",connects)
        Conn.updatestatus_users(my_rootname, '离线')

        rlist.remove(connfd)
        connfd.close()

    def chat(self, connfd, my_rootname, friend_rootname):
        print("chat>clients:", clients)
        # 好友信息
        friend_info = Conn.select_users(friend_rootname)
        friend_info_dict = dict(zip(["type", "rootname", "nickname", "gender", "tel", "address", "email", "birthday", "avatar", "style", "onlinestatus"],
                                    ["I"] + [str(x) for x in friend_info]))

        connfd.send(json.dumps(friend_info_dict).encode())

        # 历史记录
        history = Conn.selectfive_history(my_rootname, friend_rootname)
        history_dict = dict(zip(["type", "record"],
                                ['H'] + [[str(x[0]) for x in history][::-1]]))

        print("历史记录:", history_dict)
        connfd.send(json.dumps(history_dict).encode())

        if friend_rootname in clients:
            connects[connfd] = clients[friend_rootname]
            # connects[clients[friend_rootname]] = connfd


if __name__ == '__main__':
    rootServer = Root_Server(ADDR)
    rootServer.serve_forever()
