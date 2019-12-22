# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Expense_Tracker.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(584, 162)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(430, 40, 131, 331))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Log = QtWidgets.QRadioButton(Dialog)
        self.Log.setGeometry(QtCore.QRect(50, 30, 281, 31))
        self.Log.setObjectName("Log")
        self.Display = QtWidgets.QRadioButton(Dialog)
        self.Display.setGeometry(QtCore.QRect(50, 90, 251, 31))
        self.Display.setObjectName("Display")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Log.setText(_translate("Dialog", "Log an Expense"))
        self.Display.setText(_translate("Dialog", "Display Expense"))

