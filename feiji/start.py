# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Form implementation generated from reading ui file 'document_up_down.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import os

path2 = "feiji-background_1.png"


class Ui_MainWindow_file(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 230, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{background-color:black;\
                                            color: white;   border-radius: 10px;  border: 2px groove gray;\
                                            border-style: outset;}"
                                      "QPushButton:hover{background-color:white; color: black;}"
                                      "QPushButton:pressed{background-color:rgb(85, 170, 255);\
                                                           border-style: inset; }")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 信号槽
        self.pushButton.clicked.connect(self.show_main)

    def show_main(self):
        MainWindow.close()
        os.system("python ./feiji/main.py")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setStyleSheet("border-image:url(%s)" % path2)
        MainWindow.setWindowTitle(_translate("MainWindow", "游戏中"))
        self.pushButton.setText(_translate("MainWindow", "开始游戏"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_file()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
