# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\xufan\OneDrive\Documents\Python\mine\dlg_setting.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dlg_Setting(object):
    def setupUi(self, Dlg_Setting):
        Dlg_Setting.setObjectName("Dlg_Setting")
        Dlg_Setting.setWindowModality(QtCore.Qt.ApplicationModal)
        Dlg_Setting.resize(368, 213)
        Dlg_Setting.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dlg_Setting)
        self.buttonBox.setGeometry(QtCore.QRect(70, 150, 201, 32))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(Dlg_Setting)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 40, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinBox_rows = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.spinBox_rows.setFont(font)
        self.spinBox_rows.setMinimum(3)
        self.spinBox_rows.setMaximum(10)
        self.spinBox_rows.setObjectName("spinBox_rows")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_rows)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinBox_cols = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.spinBox_cols.setFont(font)
        self.spinBox_cols.setMinimum(3)
        self.spinBox_cols.setMaximum(10)
        self.spinBox_cols.setObjectName("spinBox_cols")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_cols)

        self.retranslateUi(Dlg_Setting)
        self.buttonBox.accepted.connect(Dlg_Setting.accept)
        self.buttonBox.rejected.connect(Dlg_Setting.reject)
        QtCore.QMetaObject.connectSlotsByName(Dlg_Setting)

    def retranslateUi(self, Dlg_Setting):
        _translate = QtCore.QCoreApplication.translate
        Dlg_Setting.setWindowTitle(_translate("Dlg_Setting", "Dialog"))
        self.label.setText(_translate("Dlg_Setting", "行数"))
        self.label_2.setText(_translate("Dlg_Setting", "列数"))
