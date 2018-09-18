from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from module.turles1 import *
import random
from PyQt5.QtCore import Qt, QEvent, QRegExp
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator
import module.mysqlRoot as Conn
import time
import json

class Ui_ZC2(QtWidgets.QMainWindow):

    def __init__(self,L,T,W,text1,s):
        super().__init__()
        self.setupUi(self)
        self.L = L
        self.T = T
        self.W = W
        self.text = text1
        self.s = s

    def setupUi(self, MainWindow):

        path2 = "./zc/test-1.png"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 556)
        MainWindow.setStyleSheet("background-image:url(%s)" % path2)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 140, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 80, 401, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 240, 54, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pwText = QtWidgets.QLineEdit(self.centralwidget)
        self.pwText.setGeometry(QtCore.QRect(180, 240, 191, 20))
        self.pwText.setStyleSheet("style={\n"
                                  "placeholder=\"请输入密码\"\n"
                                  "}")
        self.pwText.setObjectName("pwText")
        self.pwText.setPlaceholderText("密码6-15位，只能有数字和字母")
        self.pwText.setEchoMode(QLineEdit.Password)
        regx = QRegExp("[0-9A-Za-z]{14}$")
        validator = QRegExpValidator(regx, self.pwText)
        self.pwText.setValidator(validator)


        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(93, 290, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pwText_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.pwText_2.setGeometry(QtCore.QRect(180, 290, 191, 20))
        self.pwText_2.setStyleSheet("placeholder：“密码由6-20位数字或字母组成”；")
        self.pwText_2.setObjectName("pwText_2")
        self.pwText_2.setEchoMode(QLineEdit.Password)
        regx = QRegExp("[0-9A-Za-z]{14}")
        validator = QRegExpValidator(regx, self.pwText_2)
        self.pwText_2.setValidator(validator)


        self.randomText = QtWidgets.QLabel(self.centralwidget)
        self.randomText.setGeometry(QtCore.QRect(240, 160, 221, 16))
        self.randomText.setText("")
        self.randomText.setObjectName("randomText")
        self.liButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.liButton.setGeometry(QtCore.QRect(180, 330, 185, 41))
        self.liButton.setObjectName("liButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(170, 130, 201, 51))
        self.textBrowser.setStyleSheet("font: 75 italic 24pt \"幼圆\";\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(145, 241, 249, 255), stop:1 rgba(255, 255, 255, 255));")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(380, 280, 131, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("color: rgb(255, 0, 0);\n")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #设置信号槽
        self.liButton.clicked.connect(self.back_out)

    def back_out(self):
        rootname = self.text
        nickname = self.W[0]
        pwd = self.pwText.text()
        gender = self.L[0]
        tel = self.W[3]
        address = self.W[5]
        email = self.W[4]
        birthday = self.W[2]
        avatar = self.T[0]
        style = self.W[1]
        onlinestatus = "离线"



        info_dict = {
            "rootname":rootname,
            "nickname":nickname,
            "pwd":pwd,
            "gender":gender,
            "tel":tel,
            "address":address,
            "email":email,
            "birthday":birthday,
            "avatar":avatar,
            "style":style,
            "onlinestatus":onlinestatus
        }

        self.s.send("Z".encode())
        time.sleep(0.5)
        self.s.send(json.dumps(info_dict).encode())
        self.textBrowser_2.clear()

        pa = ""
        if self.pwText_2.text() == self.pwText.text():
            pa += "设置成功，请返回登录"
            self.textBrowser_2.append(pa)
            print(self.pwText.text())
            time.sleep(1)
            self.hide()

        else:
            pa += "两次密码不一致，请重新输入"
            self.textBrowser_2.append(pa)
            self.pwText.clear()
            self.pwText_2.clear()



    def zhanghao(self, text):
        self.textBrowser.append(text)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        MainWindow.setWindowTitle(_translate("MainWindow", "注册中"))
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))
        self.label.setText(_translate("MainWindow", "您好！"))
        self.label_2.setText(_translate("MainWindow", "账号："))
        self.label_3.setText(_translate("MainWindow", "恭喜您注册成功。请对你的账号做相应的设置！"))
        self.label_5.setText(_translate("MainWindow", "密码："))
        self.label_6.setText(_translate("MainWindow", "确认密码："))
        self.liButton.setText(_translate("MainWindow", "设置完成"))
