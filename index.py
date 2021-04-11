from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*

import sys
import datetime
#import mysql.connector
import sqlite3
#import db
from qmain import Ui_MainWindow
from os import path

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self,perant=None):
        super(Main,self).__init__(perant)
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.db_conect()
        self.Ui_chinged()
        self.Daily_movment()
        
        self.Handel_pashbutton()

        self.show_name_client()
        self.show_all_book()

        
        self.open_quran_input()
        self.open_report()
        self.open_settings()
        self.open_daily_movment_tap()

        self.show_user()
        self.tabWidget.setCurrentIndex(0) #open Login
    ##########################
    def Ui_chinged(self):  
        self.tabWidget.tabBar().setVisible(False)  
        
    def db_conect(self):
        #self.db=mysql.connector.connect(host='localhost',user='root',password='20112019',database='quran_db')
        self.db = sqlite3.connect('QTdatabase.db')
        self.cur = self.db.cursor()
        
        
    def Handel_pashbutton(self):
        self.pushButton_18.clicked.connect(self.open_daily_movment_tap)
        self.pushButton_26.clicked.connect(self.open_quran_input)
        self.pushButton_25.clicked.connect(self.open_report)
        self.pushButton_24.clicked.connect(self.open_settings)
        
        self.pushButton_13.clicked.connect(self.add_client)
        self.pushButton_14.clicked.connect(self.check_client)
        self.pushButton_16.clicked.connect(self.edit_client)
        self.pushButton_15.clicked.connect(self.delete_client)

        self.pushButton_17.clicked.connect(self.add_user)
        self.pushButton_22.clicked.connect(self.checked_user)
        self.pushButton_20.clicked.connect(self.edit_user)
        self.pushButton_19.clicked.connect(self.delete_user)
        self.pushButton_21.clicked.connect(self.Accsesing)

        self.pushButton_5.clicked.connect(self.input_quran)
        self.pushButton_8.clicked.connect(self.input_book)

        self.pushButton_12.clicked.connect(self.login)
        self.pushButton_11.clicked.connect(self.report)

    ############################quean
    def Daily_movment(self):  #mathod show all elmeints input quran data
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        self.cur.execute('''select date,Telwah,Moragah,Saveing,name_id from quran_input_data  ''')
        data = self.cur.fetchall()
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1

            row_pisation = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_pisation)

        #############################book
    def show_all_book(self):# mathod show all book
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)
        self.cur.execute('''select data,numper_paper,name_book,name_id from any_book_input  ''')
        data = self.cur.fetchall()
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                   self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))
                   col += 1
            row_pisation = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_pisation)
##################################
    def filter_Daily_movment(self):
        pass
    #########################

    def input_quran(self): #input quran data 
        name_client_index = self.comboBox.currentText()   #من اجل اختيار القيمة الحالية
        #try :
        query = '''select id from client where name=? '''     # ال%s عشان يرجع قيمة ال name_client_index
        self.cur.execute(query,[(name_client_index)])                # مناجل ادخال القيمة
        data=self.cur.fetchone()
        name_client =data[0]                    
            
        name_client = self.comboBox.currentText()
        saveuing = self.lineEdit_2.text()
        moragah = self.lineEdit_3.text()
        telaowah= self.lineEdit_4.text()
        #= self.lineEdit_5.text()
        date = datetime.datetime.now()
        self.cur.execute('''
            insert into  quran_input_data(name_id ,saveing,Moragah,Telwah, date )values(?,?,?,?,?) 
        ''',(name_client,saveuing,moragah,telaowah,date ))
        data =self.db.commit()

        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.Daily_movment()
        #except Exception:
        #    QMessageBox.information(self,'خطأ',' قم بإدخال البيانات كاملة',QMessageBox.Ok)
        #    return  
            

    def show_name_client(self): #show name clients of the conboBox of all program
        self.comboBox.clear()
        self.comboBox_5.clear()
        self.comboBox_4.clear()
        self.comboBox_6.clear()
        self.cur.execute(''' select name from client''')
        all_name= self.cur.fetchall()
        for name in all_name:
            self.comboBox.addItem(str(name[0]))
            self.comboBox_5.addItem(str(name[0]))
            self.comboBox_4.addItem(str(name[0]))
            self.comboBox_6.addItem(str(name[0]))
        self.edit_client()

    ##########################

    
    def input_book(self):
        name_client_index = self.comboBox_5.currentText()   #من اجل اختيار القيمة الحالية
        #try:
        query = '''select id from client where name=? '''     # ال%s عشان يرجع قيمة ال name_client_index
        self.cur.execute(query,[(name_client_index)])                # مناجل ادخال القيمة
        data=self.cur.fetchone()
        name_client =data[0]                    #### ##من اجل اضافة القيمة الى الid يعني القيمة الجديده يكون لها اب مرتبطة ب idحقه###
    
    
        name_client = self.comboBox_5.currentText()
        name_book = self.lineEdit_8.text()
        number_papers = self.lineEdit_10.text()
        date = datetime.datetime.now()
        self.cur.execute('''
            insert into  any_book_input(name_id ,name_book,numper_paper, data )values(?,?,?,?) 
        ''',(name_client,name_book,number_papers,date ))
        data =self.db.commit()
        
        self.lineEdit_8.setText('')
        self.lineEdit_10.setText('')

        self.statusBar().showMessage('تمت الاضافة بنجاح') 
        self.show_all_book()
        #except Exception:
        #    QMessageBox.information(self,'خطأ',' قم بإدخال البيانات كاملة',QMessageBox.Ok)
        #    return  

    ############################
    def report(self): #report sum data with input
        name_client = self.comboBox_6.currentText()
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)
        self.cur.execute(''' select sum(Telwah),sum(Moragah),sum(Saveing) from quran_input_data where name_id=?  ''',(name_client,))
        saves = self.cur.fetchall()
        for row ,form in enumerate(saves):
            for col, item in enumerate(form):
                if col ==0 :
                    sql = '''select sum(Telwah)  from quran_input_data where name_id=?'''
                    self.cur.execute(sql, [(name_client)])
                    Telwah = self.cur.fetchone()
                    self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(Telwah[0])))
                elif col ==1:
                    sql = '''select sum(Moragah)  from quran_input_data where name_id=?'''
                    self.cur.execute(sql, [(name_client)])
                    Moragah = self.cur.fetchone()
                    self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(Moragah[0])))
                elif col ==2:
                    sql = '''select sum(Saveing)  from quran_input_data where name_id=?'''
                    self.cur.execute(sql, [(name_client)])
                    Saveing = self.cur.fetchone()
                    self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(Saveing[0])))
        
    ################################

    def add_client(self):
        name = self.lineEdit_14.text()
        mail = self.lineEdit_15.text()
        phone = self.lineEdit_16.text()
        try :
            self.cur.execute('''
                insert into client(name , mail , phone)values(?,?,?)
            ''',(name,mail,phone))
            self.db.commit()  
            self.lineEdit_14.setText('')      
            self.lineEdit_15.setText('')
            self.lineEdit_16.setText('')
            self.statusBar().showMessage('تمت الاضافة بنجاح') 
            
            self.show_name_client()
        except Exception:
            QMessageBox.information(self,'خطأ',' قم بإدخال البيانات كاملة',QMessageBox.Ok)
            return  

    def check_client(self): #filter client nane 
        name = self.lineEdit_26.text()
        try:
            sql = ('''select * from  client where name=? ''')
            self.cur.execute(sql,([name]))
            data=self.cur.fetchone()
            self.lineEdit_17.setText(data[1])
            self.lineEdit_18.setText(data[2])
            self.lineEdit_19.setText(str(data[3])) 
        except Exception:
            QMessageBox.information(self,'خطأ',' قم بإدخال البيانات كاملة',QMessageBox.Ok)
            return  
    def edit_client(self):
        name = self.lineEdit_17.text()
        mail = self.lineEdit_18.text()
        phone = self.lineEdit_19.text()
        name_search = self.lineEdit_26.text()
        try :
            self.cur.execute('''
                    update client set name=?, mail =? , phone=? where name =?
                ''',(name,mail,phone,name_search))
            self.db.commit()
            self.lineEdit_17.setText('')
            self.lineEdit_18.setText('')
            self.lineEdit_19.setText('')
            self.lineEdit_26.setText('')
            self.statusBar().showMessage('تم التعديل بنجاح')      
        except Exception:
            QMessageBox.information(self,'خطأ',' قم بإدخال البيانات كاملة',QMessageBox.Ok)
            return  
    def delete_client(self):
        name = self.lineEdit_17.text()
        try :
            sql = ('''DELETE FROM client WHERE name =?''')
            self.cur.execute(sql, [(name)])
            self.db.commit()
            self.lineEdit_17.setText('')
            self.lineEdit_18.setText('')
            self.lineEdit_19.setText('')
            self.lineEdit_26.setText('')
            self.statusBar().showMessage('تم الحذف بنجاح')  
        except Exception:
            QMessageBox.information(self,'خطأ',' قم بإدخال البيانات كاملة',QMessageBox.Ok)
            return  
##################################
    def add_user(self):
        name = self.lineEdit_20.text()
        mail = self.lineEdit_21.text()
        phone = self.lineEdit_22.text()
        password = self.lineEdit_23.text()
        agene_password = self.lineEdit_24.text()
        #try :
        if password == agene_password :
            self.cur.execute('''
                insert into users(name , mail , phone,password)values(?,?,?,?)
            ''',(name,mail,phone,password))
            self.db.commit()
            self.lineEdit_20.setText('')      
            self.lineEdit_21.setText('')
            self.lineEdit_22.setText('')      
            self.lineEdit_23.setText('')
            self.lineEdit_24.setText('')
            self.statusBar().showMessage('تمت الاضافة بنجاح') 
            self.show_user()
        #except Exception:
        #    QMessageBox.information(self,'خطأ',' قم بإدخال البيانات كاملة',QMessageBox.Ok)
        #    return  
    def checked_user(self): #filter anme user 
        name = self.lineEdit_35.text()
        password = self.lineEdit_34.text()
        try :
            sql =('''select * from users where name=? and password=? ''')
            self.cur.execute(sql,([name,password]))
            datas = self.cur.fetchall()
            for data in datas:
                self.lineEdit_30.setText(data[1])
                self.lineEdit_33.setText(data[2])
                self.lineEdit_31.setText(str(data[3]))
                self.lineEdit_32.setText(str(data[4]))
        except Exception:
            QMessageBox.information(self,'خطأ',' قم بإدخال البيانات كاملة',QMessageBox.Ok)
            return  

    def edit_user(self):
        name = self.lineEdit_30.text()
        mail = self.lineEdit_33.text()
        phone = self.lineEdit_31.text()
        password_new = self.lineEdit_32.text()
        try:
            self.cur.execute('''
                    update users set name=?, mail =? , phone=? ,password=? where name =? 
                ''',(name,mail,phone,password_new,name))
            self.db.commit()
            self.lineEdit_30.setText('')
            self.lineEdit_33.setText('')
            self.lineEdit_31.setText('')
            self.lineEdit_32.setText('')
            self.lineEdit_35.setText('')
            self.lineEdit_34.setText('')
            self.statusBar().showMessage('تم التعديل بنجاح')     
        except Exception:
            QMessageBox.information(self,'خطأ',' قم بإدخال البيانات كاملة',QMessageBox.Ok)
            return  
    def delete_user(self):
        name = self.lineEdit_35.text()
        password = self.lineEdit_34.text()
        try :
            sql = ('''DELETE FROM users WHERE name =? and password=? ''')
            self.cur.execute(sql, [name,password])
            self.db.commit()
            self.lineEdit_30.setText('')
            self.lineEdit_33.setText('')
            self.lineEdit_31.setText('')
            self.lineEdit_32.setText('')
            self.lineEdit_35.setText('')
            self.lineEdit_34.setText('')
            self.statusBar().showMessage('تم الحذف بنجاح')
        except Exception:
            QMessageBox.information(self,'خطأ',' قم بإدخال البيانات كاملة',QMessageBox.Ok)
            return  
    def show_user(self):
        self.cur.execute('select name from users')
        user_name = self.cur.fetchall()
        for name in user_name:
            self.comboBox_2.addItem(name[0])
#################################

    def Accsesing(self):  ##########مشكلة تكرارالاسم ساقوم بعمل اضافة ابديت بدل الانشاء من جديد ممكن داله #####
        user_name = self.comboBox_2.currentText()
        if self.checkBox_14.isChecked()==True:
            self.cur.execute('''
                insert into accsesing(name_id,quran,report_tab,setting,add_client,edit_client,delete_client,add_user,edit_user,delete_user,Acssesing)
            VALUES(?,?,?,?,?,?,?,?,?,?,?)''',(user_name,1,1,1,1,1,1,1,1,1,1))
            self.db.commit()
            
            self.statusBar().showMessage('تم اضافة كـل الصلاحيات للمستخدم بنجاح')

        else:

            quran_tab =0
            reports_tab = 0 
            setting_tab = 0
            add_client = 0
            edit_client = 0
            delet_client =0
            add_user = 0
            edit_user = 0
            delet_user =0
            accsing_tab = 0

            if self.checkBox_5.isChecked() == True:
                        quran_tab = 1
            if self.checkBox_7.isChecked() == True:
                        reports_tab = 1
            if self.checkBox.isChecked() == True:
                        setting_tab = 1           
            if self.checkBox_2.isChecked() == True:
                        add_client = 1
            if self.checkBox_4.isChecked() == True:
                        edit_client = 1
            if self.checkBox_3.isChecked() == True:
                        delet_client = 1
            if self.checkBox_9.isChecked() == True:
                        add_user = 1
            if self.checkBox_10.isChecked() == True:
                        edit_user = 1
            if self.checkBox_11.isChecked() == True:
                        delet_user = 1
            if self.checkBox_12.isChecked() == True:
                        accsing_tab = 1


            self.cur.execute('''
            insert into accsesing ( name_id,quran,report_tab,setting,add_client,edit_client,delete_client,add_user,edit_user,delete_user,Acssesing)
                VALUES(?,?,?,?,?,?,?,?,?,?,?)''',(user_name,quran_tab,reports_tab,setting_tab,add_client,edit_client,delet_client,add_user,edit_user,delet_user,accsing_tab))
            self.db.commit()
            self.statusBar().showMessage('تم اضافة  الصلاحيات للمستخدم  بنجاح')
    ##########################
    ##############

    def login(self):
        
        name = self.lineEdit_12.text()
        password = self.lineEdit_13.text()
        #try :
        sql =('''select * from users where name=? and password=? ''')
        self.cur.execute(sql,([name,password]))
        datas = self.cur.fetchall()
        for data in datas:
            if data[4]== password and data[1]==name:
                self.tabWidget.setCurrentIndex(1)
                self.cur.execute('select * from accsesing where name_id=? ',(name,))
                accses_uesr = self.cur.fetchone()
                if accses_uesr[2] == 1:
                    self.pushButton_26.setEnabled(True)
                if accses_uesr[3] == 1:
                    self.pushButton_25.setEnabled(True)
                if accses_uesr[4] == 1:
                    self.pushButton_24.setEnabled(True)
                if accses_uesr[5] == 1:
                    self.pushButton_13.setEnabled(True)
                if accses_uesr[6] == 1:
                    self.pushButton_16.setEnabled(True)
                if accses_uesr[7] == 1:
                    self.pushButton_15.setEnabled(True)
                if accses_uesr[8] == 1:
                    self.pushButton_17.setEnabled(True)
                if accses_uesr[9] == 1:
                    self.pushButton_20.setEnabled(True)
                if accses_uesr[10] == 1:
                    self.pushButton_19.setEnabled(True)
                if accses_uesr[11] == 1:
                    self.pushButton_21.setEnabled(True)
        #except Exception:
        #    QMessageBox.information(self,'خطأ',' قم بإدخال البيانات كاملة',QMessageBox.Ok)
        #    return  
    ##########################
    ### دوال الازرار
    #######################

    def open_daily_movment_tap (self):
        self.tabWidget.setCurrentIndex(1)

    def open_quran_input (self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)

    def open_report (self):
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_3.setCurrentIndex(0)

    def open_settings (self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_4.setCurrentIndex(0)

def main():                                           #كود مكرر حفظ
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    App.exec_()
if __name__== '__main__':
    main()

