from view.Login import Ui_ChatLoginWindow
from view.Chat import Ui_ChatForm
from module.haoyou_select import Ui_ADD
from module.pushbutton import Ui_Zhuce
from socket import *
import sys
import threading
import time
import json

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import module.items
import os


class LoginWindow(QMainWindow, Ui_ChatLoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        qss_file = open('view/qss/Login_style.qss').read()
        self.setStyleSheet(qss_file)
        self.txt_pwd.setEchoMode(QLineEdit.Password)

        ADDR = ('127.0.0.1', 8025)

        self.s = socket()
        self.s.connect(ADDR)
        self.rootname = ''
        self.my_info = {}
        self.friends_list = []

        #信号槽
        self.btn_login.clicked.connect(self.login_click)
        self.chk_register.clicked.connect(self.zhuce_click)


    def zhuce_click(self):
        self.zhuce = Ui_Zhuce(self.s)
        self.zhuce.show()
        self.zhuce.textB()


    def login_click(self):
        self.rootname = self.txt_user.text()
        pwd = self.txt_pwd.text()
        self.s.send(("L " + self.rootname + " " + pwd).encode())
        data = self.s.recv(128).decode()
        print("login_click>data", data)
        if data == "True":
            print("登陆成功")

            data = json.loads(self.s.recv(4096).decode())

            self.friends_list = data
            print("login_click>friends",self.friends_list)

            data = json.loads(self.s.recv(1024).decode())
            self.my_info = data
            print("login_click>my_info", self.my_info)

            # miss_msg = json.loads(self.s.recv(4096).decode())

            self.hide()
            self.dia = Mychat(self.my_info, self.s, self.friends_list)
            self.dia.show()

        else:
            QMessageBox.information(self, "提示", "用户名或密码错误！",
                                              QMessageBox.Yes)
            self.txt_user.clear()
            self.txt_pwd.clear()


class Mychat(QMainWindow, Ui_ChatForm):
    def __init__(self, my_info, s, friend_list):
        super().__init__()
        self.setupUi(self)
        qss_file = open('view/qss/Chat_style.qss').read()
        self.setStyleSheet(qss_file)
        self.my_info = my_info
        self.s = s
        self.friend_list = friend_list
        print("Mychat> friendlist>", friend_list)
        # self.threads = []
        # self.friend_info = {}

        friend_list.insert(0, ['小Root', 1000, 'images/avatar0.jpg'])
        self.friend_list = friend_list
        self.listWidget1_1._set_items(self.friend_list)
        # self.show_item()

        self.history_list = {}

        self.chat_th = threading.Thread(target=self.Recv)  # 创建接收信息线程
        self.chat_th.setDaemon(True)
        self.chat_th.start()

        self.send_Button.clicked.connect(self.Send)
        self.quit_Button.clicked.connect(self.Quit)
        self.pushButton_4.clicked.connect(self.play_xinxi)
        self.pushButton_2.clicked.connect(self.play_flie)
        self.pushButton.clicked.connect(self.play_jiahaoyou)

        self.pushButton_7.clicked.connect(self.show_item)

        self.pushButton_3.clicked.connect(self.play_feiji)


        self.listWidget1_1.set_doubleclick_slot(self.chat)


        print("进入了Mychat")

        self.chat3()

    def play_feiji(self):
        os.system("python ./feiji/start.py")

    def show_item(self):
        self.listWidget1_1._set_items(self.friend_list)
        print("show_item>end")

    def play_jiahaoyou(self):
        # os.system("python ./haoyou_select.py")
        self.add = Ui_ADD(self.my_info,self.s)
        self.add.show()
        # self.s.send(("P " + self.my_info['rootname']).encode())

    def play_flie(self):
        os.system("python ./xiazai.py")


    def play_xinxi(self):
        os.system("python ./chengyuan.py")



    def closeEvent(self, QCloseEvent):
        print("进入closeEvent")
        self.s.send(('Q ' + self.my_info["rootname"]).encode())



    def Quit(self):
        self.s.send(('Q ' + self.my_info["rootname"]).encode())
        sys.exit()

    def chat3(self):
        self.friend_info = dict(zip(
            ["type", "rootname", "nickname", "gender", "tel", "address", "email", "birthday", "avatar", "style",
             "onlinestatus"],
            ["I", "1000", "小Root", "女", '861008610010', '野生技术协会', '10086@10010.com', '1月1日', 'images/avatar0.jpg',
             '人生苦短,我用Python', '在线']))
        self.showinit(self.friend_info)

        self.s.send(('T ' + '离线消息').encode())
        time.sleep(0.5)
        self.s.send(json.dumps(self.my_info).encode())
        print("init执行完毕")
        self.textBrowser.clear()


    def chat(self, name, mac):
        if mac =="1000":
            self.chat3()
        else:
            print("chat>mac", mac)
            self.s.send(('C ' + self.my_info["rootname"] + " " + mac).encode())
            self.textBrowser.clear()
            time.sleep(0.5)
            print("chathistory>",self.history_list)
            for line in self.history_list:
                self.textBrowser.append(line)


    def showinit(self, friend_info):
        print("进入了showinit")
        self.chatname_label.setText(friend_info["nickname"])
        print("1")
        self.my_avatar_label.setStyleSheet("background-color: gainsboro;border-image: url('%s');" % self.my_info["avatar"])
        self.f_avatar_label.setStyleSheet("background-color: gainsboro;border-image: url('%s');" % friend_info["avatar"])
        print("2")
        self.f_nickname_label.setText(friend_info["nickname"])
        print("3")
        self.style_label.setText(friend_info["style"])
        print("4")
        self.address_label.setText(friend_info["address"])
        print("5")
        self.email_label.setText(friend_info["email"])
        print("6")
        self.tel_label.setText(friend_info["tel"])
        print("7")
        self.birthday_label.setText(friend_info["birthday"])
        print("8")
        self.onlinestatus_label.setText(friend_info["onlinestatus"])

        print("showinit执行完毕")

    def Send(self):  # 发送消息
        data = self.textEdit.toPlainText()
        print("Send:", data)

        if self.friend_info["rootname"] == "1000":
            tldata = "T " + data
            text = self.my_info["nickname"] + '  ' + "%02d:%02d:%02d" % time.localtime()[3:6] + '\n' + data +'\n'
            self.s.send(tldata.encode())
            time.sleep(1)
            self.s.send(json.dumps(self.my_info).encode())
            print("Send>end")
        else:
            text = self.my_info["nickname"] + '  ' + "%02d:%02d:%02d" % time.localtime()[3:6] + '\n' + data +'\n'
            tldata = self.my_info["rootname"] + ' ' + self.friend_info["rootname"] + ' ' + text
            print(text)
            self.s.send(tldata.encode())

        self.textBrowser.append(text)

        # 每次发送完消息，清空发送框
        self.textEdit.setText("")

    def Recv(self):  # 接受消息
        while True:
            try:
                data = json.loads(self.s.recv(4096).decode())
            except Exception as e:
                print(e)
            print("Recv:", data)
            # 好友信息
            if data["type"] == "I":
                self.friend_info = data
                self.showinit(self.friend_info)
            # 历史记录
            elif data["type"] == "H":
                self.history_list = data["record"]
                print("历史记录>", self.history_list)

            elif data["type"] == "M":
                print("执行到了type=M")
                for line in data["miss_msg"]:
                    self.textBrowser.append(line)

            elif data["type"] == "P":
                self.friend_list = data["friends_list"]
                self.friend_list.insert(0, ['小Root', 1000, 'images/avatar0.jpg'])
                print('data["type"] == "P"', self.friend_list)

            elif data["type"] == "F":
                print("执行到了type=F")
                self.add.recvinfo(data["info"])
                self.s.send(("P " + self.my_info['rootname']).encode())
                # if data["info"]:
                #     self.friend_list.append([data["info"][1] , data["info"][0], data["info"][7]])

            elif data["type"] == "V":
                print("执行到了type=F")
                self.add.recvinfo1(data["info"])
                self.s.send(("P " + self.my_info['rootname']).encode())

            # 聊天信息
            elif data["type"] == "S":
                if data["rootname"] == self.friend_info["rootname"]:
                    self.textBrowser.append(data["msg"])
                elif data["rootname"] == self.my_info["rootname"]:
                    self.textBrowser.append("该好友未上线, 可能暂时无法回复您的信息\n")
                else:
                    # 有新消息提示
                    self.textBrowser.append("有来自  %s  的一条新的消息" % data["rootname"] + "\n")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat = LoginWindow()
    chat.show()
    sys.exit(app.exec_())


