# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Form implementation generated from reading ui file 'xiazai.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from socket import *
import sys
import time
# from erji import *
# 默认路径是桌面
lujing = 'C:/Users/Administrator/Desktop/'



class Ui_MainWindow1(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 517)
        MainWindow.setStyleSheet("background-image:url('back1.png')")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 50, 751, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.clear()
        ADDR = ('127.0.0.1', 8888)
        s = socket()
        s.connect(ADDR)
        s.send(b'L')
        data = s.recv(1024).decode()
        if data == 'OK':
            data = s.recv(4096).decode()
            files = data.split('#')
            for file in files:
                self.textBrowser.append(file)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 400, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loadfile)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 10, 361, 41))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 200, 311, 41))
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(370, 200, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("请输入文件名")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 400, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.save_path)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 280, 301, 20))
        self.label_3.setObjectName("label_3")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(370, 270, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.append(lujing)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 400, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.flush)

        # MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 23))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 下载
    def loadfile(self):
        word = self.lineEdit.text()
        global lujing
        path = lujing + word
        ADDR = ('127.0.0.1', 8888)
        s = socket()
        s.connect(ADDR)
        s.send(('G ' + word).encode())
        data = s.recv(1024).decode()
        if data == 'OK':
            fd = open(path, 'wb')
            while True:
                data = s.recv(1024)
                if data == b"##":
                    break
                fd.write(data)
            fd.close()

    # 选择保存路径

    def save_path(self):
        l = []
        openfile_name = QFileDialog.getExistingDirectory()
        l.append(openfile_name)
        global lujing
        if l[0]:
            lujing = l[0] + "/"
        self.textBrowser_2.clear()
        self.textBrowser_2.append(lujing)
    # 刷新

    def flush(self):
        self.textBrowser.clear()
        ADDR = ('127.0.0.1', 8888)
        s = socket()
        s.connect(ADDR)
        s.send(b'L')
        data = s.recv(1024).decode()
        if data == 'OK':
            data = s.recv(4096).decode()
            files = data.split('#')
            for file in files:
                self.textBrowser.append(file)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        MainWindow.setWindowTitle(_translate("MainWindow", "下载中"))
        self.pushButton.setText(_translate("MainWindow", "下载"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">下载文件列表</span></p></body></html>"))
        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">请在此输入您要下载的文件名:</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "选择下载路径"))
        self.label_3.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">您选择的下载路径是:</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "刷新"))


class Ui_MainWindow(QtWidgets.QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(542, 442)
        MainWindow.setStyleSheet("background-image:url('upload.png')")
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        # 上传按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 320, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.upfile)

        # 开始下载
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 320, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.jump_to_erji)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 542, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)   #该行会使得屏幕下方出现一片空白
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 上传
    def upfile(self):
        l = []
        openfile_name = QFileDialog.getOpenFileName(self)
        l.append(openfile_name)
        if l[0][0]:
            ADDR = ('127.0.0.1', 8888)
            s = socket()
            s.connect(ADDR)
            lujing = l[0][0]
            fd = open(lujing, 'rb')
            filename = lujing.split('/')[-1]
            s.send(("P " + filename).encode())
            data = s.recv(1024).decode()
            if data == 'OK':
                while True:
                    data = fd.read(1024)
                    if not data:
                        time.sleep(0.1)
                        s.send(b'##')
                        break
                    s.send(data)

    # 这一块注意，是重点从主界面跳转到Demo1界面，主界面隐藏，如果关闭Demo界面，主界面进程会触发self.form.show()会再次显示主界面5
    def jump_to_erji(self):
        self.MainWindow.hide()
        MainWindow1 = QtWidgets.QDialog()
        ui = Ui_MainWindow1()
        # MainWindow = QtWidgets.QMainWindow()
        ui.setupUi(MainWindow1)
        MainWindow1.show()
        MainWindow1.exec_()
        self.MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "上传文件"))
        self.pushButton_4.setText(_translate("MainWindow", "下载文件"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
