# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets 
import sqlite3
from PyQt5.QtWidgets import  QApplication , QMainWindow ,QTableWidgetItem ,QMessageBox,QAbstractItemView,QCompleter,QTreeWidgetItem,QLineEdit
import Crypto
from PyQt5.QtGui import QStandardItemModel,QPixmap
from PyQt5.QtCore import QDate 
import sys 


from passwrd import password_1
import time
from datetime import datetime


class password_2(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(password_2,self).__init__(*args,**kwargs)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        
    def setupUi(self, password_2):
        password_2.setObjectName("password_2")
        self.setWindowIcon(QtGui.QIcon('b3d.png'))
        password_2.resize(400, 300)
        self.groupBox = QtWidgets.QGroupBox(password_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 341, 241))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(0, 50, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 100, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(210, 50, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(220, 100, 61, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 190, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.change_password)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(190, 190, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.verify_user)

        self.retranslateUi(password_2)
        QtCore.QMetaObject.connectSlotsByName(password_2)
        self.n=3

    def retranslateUi(self, password_2):
        _translate = QtCore.QCoreApplication.translate
        password_2.setWindowTitle(_translate("Password", "PASSWORD"))
        self.groupBox.setTitle(_translate("Password", "PassWord"))
        self.label.setText(_translate("Password", "username"))
        self.label_2.setText(_translate("Password", "password"))
        self.pushButton_2.setText(_translate("Password", "change password"))
        self.pushButton.setText(_translate("Password", "Done"))
    def verify_user (self) :
        global n
      
        
        user_name =self.lineEdit.text()
        user_password =self.lineEdit_2.text()
        if  user_name and user_password :
            conn = sqlite3.connect('goodlife.db')
            curs=conn.cursor()
            instru=f"""SELECT EXISTS (SELECT (user_name,user_password) FROM safe WHERE  user_name='{user_name}'AND user_password='{user_password}');"""
            data=curs.execute(instru)
            for i in data :
                if i[0]:
                  
                   self.lineEdit.clear()
                   self.lineEdit_2.clear()
                   self.enable()
                   self.close()
                   
                   
                   
                   
                   
                else :
                   if self.n !=0 :
                        QMessageBox.warning(self,'حطأ',f'اعادة المحالولة متبقي {self.n}محاولة')    
                        self.n-=1
                        
                   else :
                      
                      sys.exit()     
        else :
            QMessageBox.warning(self,'خطأ','غير ممكن ادخال فراغ في مربع الادخال')
        conn.close()    
    def change_password (self):
        
        user_name1 =self.lineEdit.text()
        user_password1 =self.lineEdit_2.text()
        
        if  user_name1 and user_password1 :
             
            conn = sqlite3.connect('goodlife.db')
            curs=conn.cursor()
            instru=f"""SELECT EXISTS (SELECT (user_name,user_password) FROM safe WHERE  user_name='{user_name1}'AND user_password='{user_password1}');"""
            data=curs.execute(instru)
            for i in data :
                if i[0]:
                    
                    self.main1()
                    self.delete_password(user_name1,user_password1)
                    self.close()
                
                else :
                  QMessageBox.information(self,'الرجاء','ادخل كلمة المرور الصحيحة قبل تغيير كلمة المرور')
        else :
            QMessageBox.information(self,'الرجاء','ادخل كلمة المرور الصحيحة قبل تغيير كلمة المرور')
        conn.close()    
    def main1(self):
       self.w=password()
       self.w.show()
    def delete_password (self,user_name,user_password):
        conn = sqlite3.connect('goodlife.db')
        curs=conn.cursor()
        instru=f""" DELETE FROM safe WHERE user_name='{user_name}' AND  user_password='{user_password}'"""
        curs.execute(instru)
        conn.commit()
        conn.close()
    def enable (self):
        with open ('var.txt','w') as f:
            f.write('B3d')
    
        
       






     