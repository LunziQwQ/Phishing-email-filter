# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kiven\PycharmProjects\Phishing-email-filter\ui\view\Congratulation.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(333, 150)
        self.update_completed_label = QtWidgets.QLabel(Dialog)
        self.update_completed_label.setGeometry(QtCore.QRect(60, 30, 331, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.update_completed_label.setFont(font)
        self.update_completed_label.setObjectName("update_completed_label")
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(120, 100, 93, 28))
        self.ok_btn.setObjectName("ok_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Congratulation"))
        self.update_completed_label.setText(_translate("Dialog", "Update Completed~"))
        self.ok_btn.setText(_translate("Dialog", "OK"))

