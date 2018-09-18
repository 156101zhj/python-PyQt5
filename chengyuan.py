# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chengyuan.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

path = './img/1.jpg'
path2 = './img/2.jpg'
path3 = './img/3.jpg'
path4 = './img/4.jpg'
path5 = './img/5.jpg'
path6 = './img/6.jpg'
path7 = './img/7.jpg'
flag = 0
flag2 = 0
flag3 = 0
flag4 = 0
flag5 = 0
flag6 = 0
flag7 = 0
class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 90, 88, 88))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('border-image:url(%s)'%path)
        self.pushButton.clicked.connect(self.change)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 90, 88, 88))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet('border-image:url(%s)'%path2)
        self.pushButton_2.clicked.connect(self.change2)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 90, 88, 88))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet('border-image:url(%s)'%path3)
        self.pushButton_3.clicked.connect(self.change3)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 90, 88, 88))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet('border-image:url(%s)'%path4)
        self.pushButton_4.clicked.connect(self.change4)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 240, 88, 88))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet('border-image:url(%s)'%path5)
        self.pushButton_5.clicked.connect(self.change5)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 240, 88, 88))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet('border-image:url(%s)'%path6)
        self.pushButton_6.clicked.connect(self.change6)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 240, 88, 88))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet('border-image:url(%s)'%path7)
        self.pushButton_7.clicked.connect(self.change7)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 330, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 330, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 330, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 370, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 420, 541, 161))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        fd = open('./xiangqing.txt')
        while True:
            f = fd.readline()
            self.textBrowser.append(f)
            if not f:
                break;



        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(280, 10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(38)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def change(self):
        global flag
        if flag :
            self.pushButton.setStyleSheet('border-image:url(%s)' % path)
            self.pushButton.setText('')
            flag -= 1
        else:
            self.pushButton.setStyleSheet('border-image:url()')
            self.pushButton.setText('haha')
            flag += 1

    def change2(self):
        global flag2
        if flag2 :
            self.pushButton_2.setStyleSheet('border-image:url(%s)' % path2)
            self.pushButton_2.setText('')
            flag2 -= 1
        else:
            self.pushButton_2.setStyleSheet('border-image:url()')
            self.pushButton_2.setText('haha')
            flag2 += 1

    def change3(self):
        global flag3
        if flag3 :
            self.pushButton_3.setStyleSheet('border-image:url(%s)' % path3)
            self.pushButton_3.setText('')
            flag3 -= 1
        else:
            self.pushButton_3.setStyleSheet('border-image:url()')
            self.pushButton_3.setText('haha')
            flag3 += 1

    def change4(self):
        global flag4
        if flag4 :
            self.pushButton_4.setStyleSheet('border-image:url(%s)' % path4)
            self.pushButton_4.setText('')
            flag4 -= 1
        else:
            self.pushButton_4.setStyleSheet('border-image:url()')
            self.pushButton_4.setText('haha')
            flag4 += 1

    def change5(self):
        global flag5
        if flag5 :
            self.pushButton_5.setStyleSheet('border-image:url(%s)' % path5)
            self.pushButton_5.setText('')
            flag5 -= 1
        else:
            self.pushButton_5.setStyleSheet('border-image:url()')
            self.pushButton_5.setText('haha')
            flag5 += 1

    def change6(self):
        global flag6
        if flag6:
            self.pushButton_6.setStyleSheet('border-image:url(%s)' % path6)
            self.pushButton_6.setText('')
            flag6 -= 1
        else:
            self.pushButton_6.setStyleSheet('border-image:url()')
            self.pushButton_6.setText('haha')
            flag6 += 1

    def change7(self):
        global flag7
        if flag7:
            self.pushButton_7.setStyleSheet('border-image:url(%s)' % path7)
            self.pushButton_7.setText('')
            flag7 -= 1
        else:
            self.pushButton_7.setStyleSheet('border-image:url()')
            self.pushButton_7.setText('haha')
            flag7 += 1


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "项目成员："))
        self.pushButton.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", ""))
        self.pushButton_3.setText(_translate("MainWindow", ""))
        self.pushButton_4.setText(_translate("MainWindow", ""))
        self.pushButton_5.setText(_translate("MainWindow", ""))
        self.pushButton_6.setText(_translate("MainWindow", ""))
        self.pushButton_7.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "张豪杰"))
        self.label_3.setText(_translate("MainWindow", "胡崖"))
        self.label_4.setText(_translate("MainWindow", "刘毅"))
        self.label_5.setText(_translate("MainWindow", "徐聪"))
        self.label_6.setText(_translate("MainWindow", "卢勇"))
        self.label_7.setText(_translate("MainWindow", "袁之恒"))
        self.label_8.setText(_translate("MainWindow", "吕祥昊"))
        self.label_9.setText(_translate("MainWindow", "项目信息："))
        self.label_10.setText(_translate("MainWindow", "Root"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())