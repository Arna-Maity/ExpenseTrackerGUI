# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Expense_Log.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(664, 459)
        self.ExpenseLog = QtWidgets.QTableView(Form)
        self.ExpenseLog.setEnabled(True)
        self.ExpenseLog.setGeometry(QtCore.QRect(40, 160, 571, 261))
        self.ExpenseLog.setShowGrid(True)
        self.ExpenseLog.setGridStyle(QtCore.Qt.SolidLine)
        self.ExpenseLog.setSortingEnabled(False)
        self.ExpenseLog.setObjectName("ExpenseLog")
        self.ExpenseLog.horizontalHeader().setCascadingSectionResizes(False)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(40, 60, 138, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 60, 138, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(470, 60, 138, 31))
        self.radioButton_3.setObjectName("radioButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Expense Log View"))
        self.radioButton.setText(_translate("Form", "Work Profile"))
        self.radioButton_2.setText(_translate("Form", "Home Profile"))
        self.radioButton_3.setText(_translate("Form", "Show All"))

