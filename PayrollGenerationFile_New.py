# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PayrollGenerationFile_New.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox 

import config
class Ui_Form(object):
 
    empdata = [[0]*11]*20 
    empcheck = [[0]*1]*20
    empcheckcount = 0
    empcount = 0
    checkboxes = []


    def btnState(self,checkbox):
        print("btnState")
        global empcount
        global empcheck
        for i,b in enumerate(self.checkboxes):
            if checkbox.isChecked():
                   b.setChecked(True)
            else:
               b.setChecked(False)
  
    
          
    def loadData(self,Form):
        print("File Name= "+config.filename)
        f=open(config.filename,"r")
        emprows, empcols = (20, 11) 
        global empdata
        global empcount
        self.empcount = 0
        while True:
                line=f.readline()
                if ( line == ''):
                        break;
                self.empdata[self.empcount]=line.split(",")
                self.empcount += 1 
        print("loaddata =")
        print(self.empcount)
        
        f.close()
        self.tableWidget.setRowCount(0)
        for row_number in range (0,self.empcount):
                self.tableWidget.insertRow(row_number)
                for colum_number in range (0,11): 
                                             
                        self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(self.empdata[row_number][colum_number])))
	
  

        global empcount

        print("gendata =")
        print(self.empcount)
        y1 = 150        
        for i in range( 0,self.empcount):
            self.name = str("checkbox_")+str(i)
            nameStr = str("checkbox_")+str(i)	
            checkBox = QtWidgets.QCheckBox(Form)
            checkBox.setGeometry(QtCore.QRect(1030, y1, 21, 21))
            checkBox.setText(nameStr)
            y1 +=30
            checkBox.setVisible(True); 
            self.checkboxes.append(checkBox)
        
            
   
    def salarycalculation(self,count,employeedata,isSBI):

        from datetime import date
        today = date.today()
        from datetime import datetime
        now = datetime.now()
        TotalTDS = 0
        TotalSalary = 0

        if isSBI == 1:
            f=open("EmpPay_"+today.strftime("%d-%m-%Y")+"_S_"+now.strftime("%H:%M:%S"+".csv"),"w")
        else:
            f=open("EmpPay_"+today.strftime("%d-%m-%Y")+"_NS_"+now.strftime("%H:%M:%S"+".csv"),"w")
        
        f.write("S.No,Employee Name,Bank Name,Account Number,IFS Code,Salary,TDS\n") 

        for i in range (0, count):

            Gross_salary = int(employeedata[i][7])/int(employeedata[i][6]) * float(employeedata[i][3])
            TDS = (Gross_salary * 10)/100 
            Salary = Gross_salary-TDS
        	
            rowentry = str(i+1) +","+str(employeedata[i][1])+","
            rowentry += str(employeedata[i][8])+","+str(employeedata[i][9])+","
            rowentry += str(employeedata[i][10].replace("\n",""))+","+str(round(Salary,2))+","+str(round(TDS,2))

            TotalSalary += Salary
            TotalTDS += TDS

            f.write(rowentry+"\n")
        
        f.write(",TotalSalary = , "+str(round(TotalSalary,2))+"\n")
        f.write(",TotalTDS = , " +str(round(TotalTDS,2))+"\n")
        f.close()
       

    def GeneratePayrollFile(self):
        global checkboxes
        global empcheck
        global empcount        
        emprows, empcols = (20, 11) 
        empdatasbi = [[0]*empcols]*emprows 
        empsbicount=0
        empdatanonsbi = [[0]*empcols]*emprows 
        empnonsbicount=0
          
        
        for i,b in enumerate(self.checkboxes):
            if b.isChecked():
                self.empcheck[i] = 1	   
            else:
               self.empcheck[i] = 0
            if b.text() == "checkBox":
                if b.isChecked():

                    self.empcheck[0] = 1
                    self.empcheck[1] = 1
                    self.empcheck[2] = 1
                    self.empcheck[3] = 1
                    self.empcheck[4] = 1
                    self.empcheck[5] = 1
                    self.empcheck[6] = 1
                    self.empcheck[7] = 1
                    self.empcheck[8] = 1
                    self.empcheck[9] = 1
                    isAll = 1
                else:
                    self.empcheck[0] = 0
                    self.empcheck[1] = 0
                    self.empcheck[2] = 0
                    self.empcheck[3] = 0
                    self.empcheck[4] = 0
                    self.empcheck[5] = 0
                    self.empcheck[6] = 0
                    self.empcheck[7] = 0
                    self.empcheck[8] = 0
                    self.empcheck[9] = 0
                    isAll = 0
           

  


        for i in range (0,self.empcount):
            if self.empcheck[i] == 1:
                index = i
                if self.empdata[index][8] == "SBI":
                     empdatasbi[empsbicount] = self.empdata[index]
                     empsbicount += 1
                else:
                     empdatanonsbi[empnonsbicount] = self.empdata[index]
                     empnonsbicount += 1
        print("SBI Accounts")
        self.salarycalculation(empsbicount,empdatasbi,1)
        print("Non SBI Accounts")    
        self.salarycalculation(empnonsbicount,empdatanonsbi,0)

    def Message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText("Payroll Generation File has been created successfully !")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        




    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1071, 891)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 1011, 631))
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 790, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.loadData(Form))
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 790, 191, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.GeneratePayrollFile)
        self.pushButton_2.clicked.connect(self.Message)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 120, 911, 17))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(15, 10, 751, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(410, 60, 300, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        checkBox = QtWidgets.QCheckBox(Form)
        checkBox.setGeometry(QtCore.QRect(1030, 120, 21, 21))
        checkBox.setText("checkBox")
        checkBox.stateChanged.connect(lambda:self.btnState(checkBox))

        self.checkboxes.append(checkBox)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Employee ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Employee Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "PT/FT"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Salary"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Paid Leave"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Unpaid leave"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Total No.Of Days"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Worked days"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Bank Name"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Account Number"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "IFS Code"))
        self.pushButton.setText(_translate("Form", "Upload Employee Details"))
        self.pushButton_2.setText(_translate("Form", "Generate Payroll File"))
        self.label_2.setText(_translate("Form", "Payroll Generation File "))

        self.label_2.setText(_translate("Form", config.payrolltitle))

        self.label_3.setText(_translate("Form", "Employee Details"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    sys.exit(app.exec_())
