# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatLoginWindow(object):
    def setupUi(self, ChatLoginWindow):
        ChatLoginWindow.setObjectName("ChatLoginWindow")
        ChatLoginWindow.resize(477, 650)
        ChatLoginWindow.setStyleSheet("background-image:url(\"../images/bg.jpg\")")
        self.centralwidget = QtWidgets.QWidget(ChatLoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_user = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_user.setGeometry(QtCore.QRect(120, 300, 261, 51))
        self.txt_user.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.txt_user.setObjectName("txt_user")
        self.txt_pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_pwd.setGeometry(QtCore.QRect(120, 390, 261, 51))
        self.txt_pwd.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.txt_pwd.setObjectName("txt_pwd")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 470, 281, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chk_remenber = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.chk_remenber.setObjectName("chk_remenber")
        self.horizontalLayout.addWidget(self.chk_remenber)
        self.chk_forget = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.chk_forget.setObjectName("chk_forget")
        self.horizontalLayout.addWidget(self.chk_forget)
        self.chk_register = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.chk_register.setObjectName("chk_register")
        self.horizontalLayout.addWidget(self.chk_register)
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(90, 520, 301, 41))
        self.btn_login.setObjectName("btn_login")
        ChatLoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChatLoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 477, 23))
        self.menubar.setObjectName("menubar")
        ChatLoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChatLoginWindow)
        self.statusbar.setObjectName("statusbar")
        ChatLoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChatLoginWindow)
        QtCore.QMetaObject.connectSlotsByName(ChatLoginWindow)

    def retranslateUi(self, ChatLoginWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatLoginWindow.setWindowTitle(_translate("ChatLoginWindow", "MainWindow"))
        ChatLoginWindow.setFixedSize(ChatLoginWindow.width(), ChatLoginWindow.height())
        self.chk_remenber.setText(_translate("ChatLoginWindow", "记住密码"))
        self.chk_forget.setText(_translate("ChatLoginWindow", "忘记密码"))
        self.chk_register.setText(_translate("ChatLoginWindow", "注册账号"))
        self.btn_login.setText(_translate("ChatLoginWindow", "登录"))

