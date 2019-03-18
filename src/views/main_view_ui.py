# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(93, 86)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setObjectName("vboxlayout")
        self.spinBox_amount = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_amount.setObjectName("spinBox_amount")
        self.vboxlayout.addWidget(self.spinBox_amount)
        self.label_even_odd = QtWidgets.QLabel(self.centralwidget)
        self.label_even_odd.setObjectName("label_even_odd")
        self.vboxlayout.addWidget(self.label_even_odd)
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setEnabled(False)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.vboxlayout.addWidget(self.pushButton_reset)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))

