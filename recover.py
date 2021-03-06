# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recover.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets 
import sqlite3
from PyQt5.QtWidgets import  QApplication , QMainWindow ,QTableWidgetItem ,QMessageBox,QAbstractItemView,QCompleter,QTreeWidgetItem

from PyQt5.QtGui import QStandardItemModel,QPixmap
from PyQt5.QtCore import QDate 
import sys 

import time
from datetime import datetime


class Form(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(Form,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.set_completer()
    def setupUi(self, back):
        back.setObjectName("back")
        back.resize(400, 217)
        self.comboBox = QtWidgets.QComboBox(back)
        self.comboBox.setGeometry(QtCore.QRect(250, 70, 141, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.spinBox = QtWidgets.QSpinBox(back)
        self.spinBox.setGeometry(QtCore.QRect(130, 70, 42, 22))
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(back)
        self.label.setGeometry(QtCore.QRect(240, 40, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(back)
        self.label_2.setGeometry(QtCore.QRect(110, 40, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(back)
        self.pushButton.setGeometry(QtCore.QRect(250, 140, 111, 23))
        self.pushButton.clicked.connect(self.recovery)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(back)
        QtCore.QMetaObject.connectSlotsByName(back)
        self.setWindowIcon(QtGui.QIcon('b3d.png'))

    def retranslateUi(self, back):
        _translate = QtCore.QCoreApplication.translate
        back.setWindowTitle(_translate("back", "???????? ??????????"))
        self.label.setText(_translate("back", "???????? ?????? ???????????? "))
        self.label_2.setText(_translate("back", "??????????"))
        self.pushButton.setText(_translate("back", "??????????"))
    def recovery (self):
        element=self.comboBox.currentText()
        number=self.spinBox.value()
        if number >-1 and element != '' :
    
            conn=sqlite3.connect('mytable.db') 
            curs=conn.cursor()
            curs2=conn.cursor()
            curs3=conn.cursor()
            curs.execute(f"UPDATE tasks SET number= number +{number} WHERE name= '{element}'") 
           
            curs3.execute(f"INSERT INTO bill_register (element,number,date) VALUES('=>{element}','{number}',date('now'));")
            data= curs2.execute(f"SELECT * FROM selling_register WHERE name = '{element}' AND number={number} ")
            if data.fetchone() :
                curs2.execute(f"DELETE FROM selling_register  WHERE ROWID IN (SELECT ROWID FROM selling_register  WHERE  name='{element}' AND number = {number}  ORDER BY ROWID DESC LIMIT 1);")
            else :
                curs2.execute(f"UPDATE selling_register SET number = number - {number} WHERE ROWID IN ( SELECT ROWID  FROM selling_register WHERE name = '{element}' AND number >= {number}  ORDER BY ROWID DESC LIMIT 1   ) ;")

            

            conn.commit()
            conn.close()
            self.comboBox.clear()
            self.set_completer()
        self.comboBox.setCurrentText('')

    def set_completer (self)  :
        
        lst=[]
        
        conn = sqlite3.connect('mytable.db')
        curs =conn.cursor()
        database_data= curs.execute('SELECT name FROM selling_register ')
        for indx, i in enumerate(database_data):
               
            x=str(i).replace('(','')
            x=x.replace(')','')
            x=x.replace(',','')
            x=x.replace("'","")
            if x not in lst :

                lst.append(x)
              
        self.completer=QCompleter(lst)
        self.comboBox.setCompleter(self.completer)
           
        conn.close() 