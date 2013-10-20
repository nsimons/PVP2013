# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pad.ui'
#
# Created: Fri Oct 18 13:11:04 2013
# by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui
from MySQLScript import * # <--- REPLACE MED DIN MYSQL CLASS

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.customerWindow = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 680)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 270, 65, 65))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 340, 65, 65))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 270, 65, 65))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 480, 65, 65))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 480, 135, 65))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(490, 410, 65, 135))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(490, 340, 65, 65))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 270, 65, 65))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(420, 410, 65, 65))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(350, 410, 65, 65))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(280, 410, 65, 65))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(280, 340, 65, 65))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(280, 270, 65, 65))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(350, 340, 65, 65))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(350, 270, 65, 65))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(420, 340, 65, 65))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(560, 410, 65, 135))
        self.pushButton_17.setObjectName("pushButton_17")
        
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("ID"))
        self.tableWidget.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("Item"))
        self.tableWidget.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("Price"))
        self.tableWidget.setColumnWidth(0, 25)
        self.tableWidget.setColumnWidth(1, 107)
        self.tableWidget.setColumnWidth(2, 70)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 256, 521))
        self.tableWidget.setObjectName("tableWidget")
        
        self.declarativeView = QtDeclarative.QDeclarativeView(self.centralwidget)
        self.declarativeView.setGeometry(QtCore.QRect(300, 20, 300, 200))
        self.declarativeView.setObjectName("declarativeView")
        
        #potential fix in the future, setters/getters istället för globals?
        global rowCount
        global tot
        global dbROW
        rowCount = 0
        tot = 0
        dbROW = ""
        
        self.totLabel = QtGui.QLabel(self.centralwidget)
        self.totLabel.setGeometry(QtCore.QRect(10, 550, 341, 25))
        self.totLabel.setObjectName("totLabel")
        self.font = QtGui.QFont()
        self.font.setPointSize(20)
        self.totLabel.setFont(self.font)
        
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(282, 230, 341, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFocus()
        self.lineEdit.returnPressed.connect(self.DB)
        self.lineEdit.returnPressed.connect(self.window)
        self.lineEdit.returnPressed.connect(self.lineReset)
        
        self.pushButton_6.clicked.connect(self.lineEdit.returnPressed)
        self.pushButton_11.clicked.connect(self.buttonPress)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "down", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "up", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "Enter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_14.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_15.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_17.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        
    def DB(self):
        global dbROW
        global rowCount
        global tot
        self.tableWidget.setRowCount(rowCount+1)
        line = self.lineEdit.text()
        try: #testar om input är av typ "Int"
            line = int(line)
            line = str(line)
            if (line): #testar om line existerar
                if MySQLc.cur.execute("select id,item,price from itemTable where ID = " + line + ";"):
                    #testar om MySQLc returnerar några rows överhuvudtaget
                    for row in MySQLc.cur.fetchall():
                        self.tableWidget.setItem(rowCount,0,QtGui.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(rowCount,1,QtGui.QTableWidgetItem(str(row[1])))
                        self.tableWidget.setItem(rowCount,2,QtGui.QTableWidgetItem(str(row[2])))
                        rowCount += 1
                        tot += row[2]
                        dbROW = row[1] + " - " + str(row[2]) + " euro<br>Total Price: " + str(tot) + " euro"
                        self.totLabel.setText("Total Price: " + str(tot) + " euro")
                else: #no rows returned
                    self.tableWidget.setRowCount(rowCount)
            else: #empty line
                self.tableWidget.setRowCount(rowCount)
        except: #non-int
            self.tableWidget.setRowCount(rowCount)
        
    def window(self):
            if self.customerWindow is None:
                self.window = QtGui.QMainWindow()
                self.customerWindow = self.window
                self.window.setGeometry(50, 50, 500, 100)
                self.window.setWindowTitle('Customer Window')
                self.window.setAttribute(QtCore.Qt.WA_ShowWithoutActivating)
            self.window = self.customerWindow
            self.layout = QtGui.QVBoxLayout()
            
            self.label = QtGui.QLabel(dbROW)
            self.label.setFont(self.font)
            self.layout.addWidget(self.label)
            
            self.window.setLayout(self.layout)
            self.window.setCentralWidget(self.label)
            self.window.show()
        
    def lineReset(self):
        self.lineEdit.setText("")
            
    def buttonPress(self): #don't mind me, just testing :D
        self.lineEdit.setText("1")
            
from PySide import QtDeclarative


class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.window()
   
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
