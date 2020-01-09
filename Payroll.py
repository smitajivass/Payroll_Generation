# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Payroll.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox
from PyQt5.QtCore import QSize, QRect 


from PayrollGenerationFile_New import *

import config
class Ui_Payroll(object):

    def OK(self):
         year = str(self.comboBox.currentText())
         Month = str(self.comboBox_2.currentText())  
         config.filename = str("Employee_Detail_")+ str(Month)+"_"+str(year)+".csv"
         print(config.filename)
         config.payrolltitle = str("Payroll Generation - ") + str(Month)+" "+str(year)
         self.window = QtWidgets.QWidget()
         self.ui = Ui_Form()
         self.ui.setupUi(self.window)
         Payroll.hide()
         self.window.show()


    def setupUi(self, Payroll):
        
        Payroll.setObjectName("Payroll")
        Payroll.resize(624, 455)
        self.comboBox = QtWidgets.QComboBox(Payroll)
        self.comboBox.setGeometry(QtCore.QRect(90, 240, 86, 25))
        self.comboBox.setObjectName("Year")
        self.comboBox.addItem("2012")
        self.comboBox.addItem("2013")
        self.comboBox.addItem("2014")
        self.comboBox.addItem("2015")
        self.comboBox.addItem("2016")
        self.comboBox.addItem("2017")
        self.comboBox.addItem("2018")
        self.comboBox.addItem("2019")
        self.comboBox.addItem("2020")
        self.comboBox.addItem("2021")
        self.comboBox.addItem("2022")
        self.comboBox.addItem("2023")
        self.comboBox_2 = QtWidgets.QComboBox(Payroll)
        self.comboBox_2.setGeometry(QtCore.QRect(290, 240, 86, 25))
        self.comboBox_2.setObjectName("Month")
        self.comboBox_2.addItem("Jan")
        self.comboBox_2.addItem("Feb")
        self.comboBox_2.addItem("Mar")
        self.comboBox_2.addItem("Apr")
        self.comboBox_2.addItem("May")
        self.comboBox_2.addItem("Jun")
        self.comboBox_2.addItem("Jul")
        self.comboBox_2.addItem("Aug")
        self.comboBox_2.addItem("Sep")
        self.comboBox_2.addItem("Oct")
        self.comboBox_2.addItem("Nov")
        self.comboBox_2.addItem("Dec")
        self.label = QtWidgets.QLabel(Payroll)
        self.label.setGeometry(QtCore.QRect(30, 240, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Payroll)
        self.label_2.setGeometry(QtCore.QRect(200, 240, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Payroll)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Payroll)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Payroll)
        self.pushButton.setGeometry(QtCore.QRect(40, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.OK)

        self.retranslateUi(Payroll)
        QtCore.QMetaObject.connectSlotsByName(Payroll)



    def retranslateUi(self, Payroll):
        _translate = QtCore.QCoreApplication.translate
        Payroll.setWindowTitle(_translate("Payroll", "Form"))
        self.label.setText(_translate("Payroll", "Year"))
        self.label_2.setText(_translate("Payroll", "Month"))
        self.label_3.setText(_translate("Payroll", "Payroll Generation File "))
        self.label_4.setText(_translate("Payroll", "Select Year and Month which salary need to be calculated"))
        self.pushButton.setText(_translate("Payroll", "OK"))

  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Payroll = QtWidgets.QWidget()
    ui = Ui_Payroll()
    ui.setupUi(Payroll)
    Payroll.show()
    sys.exit(app.exec_())
