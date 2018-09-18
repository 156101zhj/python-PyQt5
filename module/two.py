# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Form implementation generated from reading ui file 'two.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
# MainWindow.setCentralWidget(self.centralwidget)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from module.turles1 import *
import random
from PyQt5.QtCore import Qt, QEvent, QRegExp
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator
from module.zc2 import Ui_ZC2

path2 = "./zc/test-1.png"
# 设定列表存储用户选定的性别
L = []
# 设定列表存储图片路径
T = []
# 设定列表保存文本
W = []


class Ui_Two(QtWidgets.QMainWindow):
    def __init__(self, s):
        super().__init__()
        self.setupUi(self)
        self.s = s

    def setupUi(self, MainWindow):
        print("two>setupUI")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 695)
        self.setWindowIcon(QtGui.QIcon("bomb.png"))
        MainWindow.setStyleSheet("background-image:url(%s)" % path2)

        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.yzmText = QtWidgets.QLineEdit(self.centralwidget)
        self.yzmText.setGeometry(QtCore.QRect(190, 430, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.yzmText.setFont(font)
        self.yzmText.setObjectName("yzmText")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 430, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.qrButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.qrButton.setGeometry(QtCore.QRect(200, 470, 185, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)

        self.qrButton.setFont(font)
        self.qrButton.setObjectName("qrButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 100, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 197, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 157, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ncText = QtWidgets.QLineEdit(self.centralwidget)
        self.ncText.setGeometry(QtCore.QRect(190, 157, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.ncText.setFont(font)
        self.ncText.setObjectName("ncText")
        self.gxText = QtWidgets.QLineEdit(self.centralwidget)
        self.gxText.setGeometry(QtCore.QRect(190, 197, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.gxText.setFont(font)
        self.gxText.setObjectName("gxText")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 230, 121, 21))
        font = QtGui.QFont()

        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 390, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 350, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.sex_2Button = QtWidgets.QRadioButton(self.centralwidget)
        self.sex_2Button.setGeometry(QtCore.QRect(310, 230, 89, 16))
        self.sex_2Button.setStyleSheet("name=\"sex\";")
        self.sex_2Button.setObjectName("sex_2Button")

        self.emText = QtWidgets.QLineEdit(self.centralwidget)
        self.emText.setGeometry(QtCore.QRect(190, 390, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.emText.setFont(font)
        self.emText.setObjectName("emText")
        self.emText.setPlaceholderText(":xxx@root.com")

        self.phText = QtWidgets.QLineEdit(self.centralwidget)
        self.phText.setGeometry(QtCore.QRect(190, 350, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.phText.setFont(font)
        self.phText.setObjectName("phText")
        self.phText.setPlaceholderText("请输入11位数字")

        regx = QRegExp("^1[0-9]{10}$")
        validator = QRegExpValidator(regx, self.phText)
        self.phText.setValidator(validator)

        self.sex_1Button = QtWidgets.QRadioButton(self.centralwidget)
        self.sex_1Button.setGeometry(QtCore.QRect(200, 230, 89, 16))
        self.sex_1Button.setStyleSheet("name=\"sex\" checked;")
        self.sex_1Button.setObjectName("sex_1Button")

        # on_tellmeButton_clicked
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 310, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.fmText = QtWidgets.QLineEdit(self.centralwidget)
        self.fmText.setGeometry(QtCore.QRect(190, 310, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.fmText.setFont(font)
        self.fmText.setObjectName("fmText")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 270, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gxText_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.gxText_2.setGeometry(QtCore.QRect(190, 270, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.gxText_2.setFont(font)
        self.gxText_2.setObjectName("gxText_2")
        self.txbutton = QtWidgets.QPushButton(self.centralwidget)
        self.txbutton.setGeometry(QtCore.QRect(190, 70, 81, 71))
        self.txbutton.setText("")
        self.txbutton.setObjectName("txbutton")

        path = './avatar0.jpg'
        self.txbutton.setStyleSheet("border-image:url(%s)" % path)

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(400, 430, 131, 20))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")

        # 验证码输出
        self.yzbtun = QtWidgets.QPushButton(self.centralwidget)
        self.yzbtun.setGeometry(QtCore.QRect(300, 420, 75, 41))
        self.yzbtun.setText("")
        self.yzbtun.setObjectName("yzbtun")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # txbutton
        # 信号槽定义信号
        self.txbutton.clicked.connect(self.test1)
        self.yzbtun.clicked.connect(self.test2)
        self.qrButton.clicked.connect(self.show_message)

        self.sex_1Button.toggled.connect(self.changeTitle)
        self.sex_2Button.toggled.connect(self.changeTitle1)

    def changeTitle(self, value):
        L.clear()
        L.append("男")

    def changeTitle1(self, value):
        L.clear()
        L.append("女")

    # 选择图像
    def test1(self):
        print("点击了图片")
        print(L)

        openfile_name = QFileDialog.getOpenFileName(self)
        # print(openfile_name)
        path = openfile_name[0]
        print(path)
        T.append(path)
        # yzbtun
        self.txbutton.setStyleSheet("border-image:url(%s)" % path)

    def test2(self):

        global ceishi
        ceishi = yanzhengma()
        print("ceishi", type(ceishi))

        path1 = './yanzhengma.png'
        self.yzbtun.setStyleSheet("border-image:url(%s)" % path1)

    def show_message(self):

        # 收集所有的文本数据
        nickname = self.ncText.text()
        W.append(nickname)
        style = self.gxText.text()
        W.append(style)
        birthday = self.gxText_2.text()
        W.append(birthday)
        tel = self.phText.text()
        W.append(tel)
        email = self.emText.text()
        W.append(email)
        address = self.fmText.text()
        W.append(address)

        l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        tet = random.sample(l, 8)
        text1 = "1"
        for i in tet:
            text1 += str(i)
        print(text1)

        yzm = ""
        text = self.yzmText.text()
        for i in ceishi:
            yzm += str(i)
        if text == yzm:
            QtWidgets.QMessageBox.information(self, "提示", "恭喜您，注册成功",
                                              QtWidgets.QMessageBox.Yes)


            self.hide()
            self.zc2 = Ui_ZC2(L, T, W, text1, self.s)
            self.zc2.show()
            self.zc2.zhanghao(text1)



        else:
            QtWidgets.QMessageBox.information(self, "提示", "验证码输入错误！",
                                              QtWidgets.QMessageBox.Yes)
            self.yzmText.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        MainWindow.setWindowTitle(_translate("MainWindow", "Root"))
        MainWindow.setWindowIcon(QtGui.QIcon("icon1.png"))
        # self.setWindowIcon(QtGui.QIcon("bomb.png"))
        self.label_2.setText(_translate("MainWindow", "输入验证码："))
        self.qrButton.setText(_translate("MainWindow", "确认"))
        self.label_7.setText(_translate("MainWindow", "上传头像："))
        self.label_4.setText(_translate("MainWindow", "个性签名："))
        self.label_3.setText(_translate("MainWindow", "昵称："))
        self.label_6.setText(_translate("MainWindow", "选择性别："))
        self.label_5.setText(_translate("MainWindow", "输入邮箱号码："))
        self.label.setText(_translate("MainWindow", "输入手机号码："))
        self.sex_2Button.setText(_translate("MainWindow", "女"))
        self.sex_1Button.setText(_translate("MainWindow", "男"))
        self.label_8.setText(_translate("MainWindow", "家庭地址："))
        self.label_9.setText(_translate("MainWindow", "出生日期："))
        self.label_10.setText(_translate("MainWindow", "点击获取验证码"))
