# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Form implementation generated from reading ui file 'haoyou.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_MainWindow(QtWidgets.QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 325)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 221, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 50, 72, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.findId)

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

    def findId(self):
        self.textBrowser.clear()
        ID = self.lineEdit.text()
        db = pymysql.connect("localhost", "root", "123456")
        cursor = db.cursor()
        cursor.execute("use rootdb;")
        cursor.execute(
            "select rootname,nickname,address from users where rootname = %s;" % ID)
        data = list(cursor.fetchall())
        if data == []:
            self.textBrowser.append('查无此人')
        else:
            s = '账号   昵称         地址\n'
            for i in data[0]:
                s += str(i) + '  '
            self.textBrowser.append(s)
            cursor.execute(
                "insert into friends(rootname,f_rootname) values (%s,%s);" % (113564098, ID))
            db.commit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "查找"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
