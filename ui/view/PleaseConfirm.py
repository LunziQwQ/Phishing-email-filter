# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kiven\PycharmProjects\Phishing-email-filter\ui\view\PleaseConfirm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 134)
        self.update_confirm_label = QtWidgets.QLabel(Dialog)
        self.update_confirm_label.setGeometry(QtCore.QRect(40, 20, 401, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.update_confirm_label.setFont(font)
        self.update_confirm_label.setObjectName("update_confirm_label")
        self.yes_btn = QtWidgets.QPushButton(Dialog)
        self.yes_btn.setGeometry(QtCore.QRect(60, 80, 121, 31))
        self.yes_btn.setObjectName("yes_btn")
        self.no_btn = QtWidgets.QPushButton(Dialog)
        self.no_btn.setGeometry(QtCore.QRect(210, 80, 121, 31))
        self.no_btn.setObjectName("no_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Please Confirm"))
        self.update_confirm_label.setText(_translate("Dialog", "Whether to confirm the update ?"))
        self.yes_btn.setText(_translate("Dialog", "Yes"))
        self.no_btn.setText(_translate("Dialog", "NO"))

