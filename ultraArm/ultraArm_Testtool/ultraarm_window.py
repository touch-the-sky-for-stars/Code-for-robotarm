# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowmain.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.compile_program = QtWidgets.QPushButton(self.centralwidget)
        self.compile_program.setGeometry(QtCore.QRect(20, 20, 111, 41))
        self.compile_program.setObjectName("compile_program")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 41, 41))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(270, 20, 121, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(440, 20, 111, 41))
        self.run_button.setObjectName("run_button")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 90, 761, 471))
        self.textBrowser.setObjectName("textBrowser")
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(610, 20, 111, 41))
        self.close_button.setObjectName("close_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.compile_program.setText(_translate("MainWindow", "编译程序"))
        self.label.setText(_translate("MainWindow", "程序："))
        self.comboBox.setItemText(0, _translate("MainWindow", "滑块控制"))
        self.comboBox.setItemText(1, _translate("MainWindow", "rviz2"))
        self.run_button.setText(_translate("MainWindow", "运行"))
        self.close_button.setText(_translate("MainWindow", "  关闭"))

