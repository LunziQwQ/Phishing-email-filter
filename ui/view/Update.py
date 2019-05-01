# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kiven\PycharmProjects\Phishing-email-filter\ui\view\Update.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(506, 243)
        self.mian_version_label = QtWidgets.QLabel(Dialog)
        self.mian_version_label.setGeometry(QtCore.QRect(40, 30, 171, 41))
        self.mian_version_label.setObjectName("mian_version_label")
        self.mian_version_num_label = QtWidgets.QLabel(Dialog)
        self.mian_version_num_label.setGeometry(QtCore.QRect(230, 40, 72, 15))
        self.mian_version_num_label.setObjectName("mian_version_num_label")
        self.library_version_label = QtWidgets.QLabel(Dialog)
        self.library_version_label.setGeometry(QtCore.QRect(40, 80, 191, 31))
        self.library_version_label.setObjectName("library_version_label")
        self.library_version_num_label = QtWidgets.QLabel(Dialog)
        self.library_version_num_label.setGeometry(QtCore.QRect(250, 90, 72, 15))
        self.library_version_num_label.setObjectName("library_version_num_label")
        self.library_quantity_label = QtWidgets.QLabel(Dialog)
        self.library_quantity_label.setGeometry(QtCore.QRect(40, 130, 221, 21))
        self.library_quantity_label.setObjectName("library_quantity_label")
        self.library_dimensionality_label = QtWidgets.QLabel(Dialog)
        self.library_dimensionality_label.setGeometry(QtCore.QRect(40, 160, 261, 16))
        self.library_dimensionality_label.setObjectName("library_dimensionality_label")
        self.library_status_label = QtWidgets.QLabel(Dialog)
        self.library_status_label.setGeometry(QtCore.QRect(40, 190, 261, 16))
        self.library_status_label.setObjectName("library_status_label")
        self.mian_update_btn = QtWidgets.QPushButton(Dialog)
        self.mian_update_btn.setGeometry(QtCore.QRect(380, 40, 91, 31))
        self.mian_update_btn.setObjectName("mian_update_btn")
        self.library_update_btn = QtWidgets.QPushButton(Dialog)
        self.library_update_btn.setGeometry(QtCore.QRect(380, 90, 91, 31))
        self.library_update_btn.setObjectName("library_update_btn")
        self.library_quantity_num_label = QtWidgets.QLabel(Dialog)
        self.library_quantity_num_label.setGeometry(QtCore.QRect(270, 130, 72, 15))
        self.library_quantity_num_label.setObjectName("library_quantity_num_label")
        self.library_dimensionality_num_label = QtWidgets.QLabel(Dialog)
        self.library_dimensionality_num_label.setGeometry(QtCore.QRect(310, 160, 72, 15))
        self.library_dimensionality_num_label.setObjectName("library_dimensionality_num_label")
        self.library_status_num_label = QtWidgets.QLabel(Dialog)
        self.library_status_num_label.setGeometry(QtCore.QRect(250, 190, 72, 15))
        self.library_status_num_label.setObjectName("library_status_num_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Update"))
        self.mian_version_label.setText(_translate("Dialog", "Main program version:"))
        self.mian_version_num_label.setText(_translate("Dialog", "TextLabel"))
        self.library_version_label.setText(_translate("Dialog", "Feature library version:"))
        self.library_version_num_label.setText(_translate("Dialog", "TextLabel"))
        self.library_quantity_label.setText(_translate("Dialog", "Feature library\'s Quantity:"))
        self.library_dimensionality_label.setText(_translate("Dialog", "Feature library\'s Dimensionality:"))
        self.library_status_label.setText(_translate("Dialog", "Feature library\'s Status:"))
        self.mian_update_btn.setText(_translate("Dialog", "update"))
        self.library_update_btn.setText(_translate("Dialog", "update"))
        self.library_quantity_num_label.setText(_translate("Dialog", "TextLabel"))
        self.library_dimensionality_num_label.setText(_translate("Dialog", "TextLabel"))
        self.library_status_num_label.setText(_translate("Dialog", "TextLabel"))

