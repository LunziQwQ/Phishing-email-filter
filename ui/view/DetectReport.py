# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kiven\PycharmProjects\Phishing-email-filter\ui\view\DetectReport.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(951, 849)
        self.total_progressBar = QtWidgets.QProgressBar(Dialog)
        self.total_progressBar.setGeometry(QtCore.QRect(150, 10, 791, 21))
        self.total_progressBar.setProperty("value", 37)
        self.total_progressBar.setObjectName("total_progressBar")
        self.total_progress_label = QtWidgets.QLabel(Dialog)
        self.total_progress_label.setGeometry(QtCore.QRect(20, 10, 121, 16))
        self.total_progress_label.setObjectName("total_progress_label")
        self.total_feedback_tableWidget = QtWidgets.QTableWidget(Dialog)
        self.total_feedback_tableWidget.setGeometry(QtCore.QRect(20, 640, 911, 171))
        self.total_feedback_tableWidget.setAutoScroll(True)
        self.total_feedback_tableWidget.setAutoScrollMargin(0)
        self.total_feedback_tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.total_feedback_tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.total_feedback_tableWidget.setObjectName("total_feedback_tableWidget")
        self.total_feedback_tableWidget.setColumnCount(4)
        self.total_feedback_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.total_feedback_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_feedback_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_feedback_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_feedback_tableWidget.setHorizontalHeaderItem(3, item)
        self.total_feedback_tableWidget.horizontalHeader().setDefaultSectionSize(225)
        self.current_feedback_label = QtWidgets.QLabel(Dialog)
        self.current_feedback_label.setGeometry(QtCore.QRect(20, 70, 161, 21))
        self.current_feedback_label.setObjectName("current_feedback_label")
        self.current_feedback_tableWidget = QtWidgets.QTableWidget(Dialog)
        self.current_feedback_tableWidget.setGeometry(QtCore.QRect(20, 100, 911, 531))
        self.current_feedback_tableWidget.setAutoScrollMargin(0)
        self.current_feedback_tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.current_feedback_tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.current_feedback_tableWidget.setObjectName("current_feedback_tableWidget")
        self.current_feedback_tableWidget.setColumnCount(5)
        self.current_feedback_tableWidget.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(8, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(9, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(9, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(10, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(10, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(11, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(11, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(11, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(12, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(12, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(12, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_feedback_tableWidget.setItem(12, 4, item)
        self.current_email_subject_label = QtWidgets.QLabel(Dialog)
        self.current_email_subject_label.setGeometry(QtCore.QRect(150, 40, 781, 16))
        self.current_email_subject_label.setText("")
        self.current_email_subject_label.setObjectName("current_email_subject_label")
        self.email_subject_label = QtWidgets.QLabel(Dialog)
        self.email_subject_label.setGeometry(QtCore.QRect(20, 40, 121, 21))
        self.email_subject_label.setObjectName("email_subject_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Detect Report"))
        self.total_progress_label.setText(_translate("Dialog", "Total Progress"))
        item = self.total_feedback_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Subject"))
        item = self.total_feedback_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Status"))
        item = self.total_feedback_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Result"))
        item = self.total_feedback_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Threat Score"))
        self.current_feedback_label.setText(_translate("Dialog", "Current Feedback:"))
        item = self.current_feedback_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Url Basic : have ip"))
        item = self.current_feedback_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Url Basic : netloc too long"))
        item = self.current_feedback_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Url Basic : have unusual"))
        item = self.current_feedback_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Url Basic : in phish tank"))
        item = self.current_feedback_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "Url Basic: have redirect"))
        item = self.current_feedback_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "Url Advance : low pr"))
        item = self.current_feedback_tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "Url_Advance : create less 3 month"))
        item = self.current_feedback_tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "Html : have script"))
        item = self.current_feedback_tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "Plain : abnormal time"))
        item = self.current_feedback_tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "Plain : inducible title"))
        item = self.current_feedback_tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "Plain : inducible content"))
        item = self.current_feedback_tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "Accessory : unusual size"))
        item = self.current_feedback_tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Dialog", "Accessory : trick type"))
        item = self.current_feedback_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Safe"))
        item = self.current_feedback_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Dangerous"))
        item = self.current_feedback_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Undetected"))
        item = self.current_feedback_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Count"))
        item = self.current_feedback_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Current Status"))
        __sortingEnabled = self.current_feedback_tableWidget.isSortingEnabled()
        self.current_feedback_tableWidget.setSortingEnabled(False)
        self.current_feedback_tableWidget.setSortingEnabled(__sortingEnabled)
        self.email_subject_label.setText(_translate("Dialog", "Email Subject:"))

