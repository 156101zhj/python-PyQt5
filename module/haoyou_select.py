# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Form implementation generated from reading ui file 'document_up_down.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# from xiazai import Ui_MainWindow


class Ui_ADD(QtWidgets.QMainWindow):

    def __init__(self, my_info, s):
        super().__init__()
        self.setupUi(self)
        self.my_info = my_info
        self.s = s

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 325)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(255, 50, 50, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.findId)

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(300, 50, 50, 30))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.clicked.connect(self.delId)


        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 120, 321, 131))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit.setPlaceholderText("请输入ID")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def recvinfo(self,data):
        if data == "nois":
            self.textBrowser.append('查无此人')
        else:
            self.textBrowser.append("好友添加成功")

    def recvinfo1(self,data):
        if data == "nois":
            self.textBrowser.append('查无此人')
        else:
            self.textBrowser.append("好友删除成功")

    def findId(self):
        self.textBrowser.clear()
        ID = self.lineEdit.text()
        self.s.send(("F"+ " " + self.my_info["rootname"] + " " + ID).encode())

    def delId(self):
        self.textBrowser.clear()
        ID = self.lineEdit.text()
        self.s.send(("V"+ " " + self.my_info["rootname"] + " " + ID).encode())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "添加"))
        self.pushButton1.setText(_translate("MainWindow", "删除"))
