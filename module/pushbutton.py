# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pushbutton.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from module.two import Ui_Two


class Ui_Zhuce(QtWidgets.QMainWindow):
    def __init__(self, s):
        super().__init__()
        self.setupUi(self)
        self.s = s

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 692)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 580, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 201, 20))
        self.label.setStyleSheet("font: 75 16pt \"华文新魏\";")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 70, 391, 481))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #信号槽
        self.pushButton.clicked.connect(self.show_main)

    #读出文件注册须知
    def textB(self):
        print("textB")
        fd = open("./module/zhuce.txt")
        while True:
            f = fd.readline()
            self.textBrowser.append(f)
            if not f:
                break


    def show_main(self):
        self.hide()
        self.two = Ui_Two(self.s)
        self.two.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "注册"))
        self.pushButton.setText(_translate("MainWindow", "同意"))
        self.label.setText(_translate("MainWindow", "请仔细阅读以下条例："))

