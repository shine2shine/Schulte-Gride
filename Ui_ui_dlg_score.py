# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\xufan\OneDrive\Documents\Python\mine\ui_dlg_score.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogScore(object):
    def setupUi(self, DialogScore):
        DialogScore.setObjectName("DialogScore")
        DialogScore.resize(400, 300)
        DialogScore.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogScore)
        self.buttonBox.setGeometry(QtCore.QRect(30, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tableView = QtWidgets.QTableView(DialogScore)
        self.tableView.setGeometry(QtCore.QRect(20, 40, 351, 201))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(DialogScore)
        self.label.setGeometry(QtCore.QRect(30, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(DialogScore)
        self.buttonBox.accepted.connect(DialogScore.accept)
        self.buttonBox.rejected.connect(DialogScore.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogScore)

    def retranslateUi(self, DialogScore):
        _translate = QtCore.QCoreApplication.translate
        DialogScore.setWindowTitle(_translate("DialogScore", "Dialog"))
        self.label.setText(_translate("DialogScore", "成绩"))
