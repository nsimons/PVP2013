import sys
from PySide import QtCore, QtGui
from MySQLScript import * # <--- REPLACE WITH YOUR MYSQL CLASS
from decimal import Decimal
from lol import Example
import os.path

import PySide


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.customerWindow = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 680)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
#buttons
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 330, 65, 65))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 400, 65, 65))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 330, 65, 65))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 540, 65, 65))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 540, 135, 65))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(490, 470, 65, 135))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(490, 400, 65, 65))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 330, 65, 65))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(420, 470, 65, 65))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(350, 470, 65, 65))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(280, 470, 65, 65))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(280, 400, 65, 65))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(280, 330, 65, 65))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(350, 400, 65, 65))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(350, 330, 65, 65))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(420, 400, 65, 65))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(560, 470, 65, 135))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(280, 260, 65, 65))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(350, 260, 65, 65))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(420, 260, 65, 65))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(490, 260, 65, 65))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(560, 260, 65, 65))
        self.pushButton_22.setObjectName("pushButton_22")
#toggle buttons        
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setAutoExclusive(True)
        self.pushButton_18.toggle()
        self.pushButton_18.clicked.connect(self.lineFocus)
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setAutoExclusive(True)
        self.pushButton_19.clicked.connect(self.lineFocus)
              
        
#tableWidget       
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
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
       
        self.declarativeView = QtDeclarative.QDeclarativeView(self.centralwidget)
        self.declarativeView.setGeometry(QtCore.QRect(300, 20, 300, 200))
        self.declarativeView.setObjectName("declarativeView")

        self.dbROW = ""
        self.rowCount = 0
        self.tot = 0
#total sum label       
        self.totLabel = QtGui.QLabel(self.centralwidget)
        self.totLabel.setGeometry(QtCore.QRect(10, 550, 341, 100))
        self.totLabel.setObjectName("totLabel")
        self.font = QtGui.QFont()
        self.font.setPointSize(15)
        self.totLabel.setFont(self.font)
#input field        
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(282, 230, 341, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFocus()
        self.lineEdit.returnPressed.connect(self.returnPressedHandler)
#button signals        
        self.pushButton_2.clicked.connect(self.traverseDown)
        self.pushButton_3.clicked.connect(self.traverseUp)
        self.pushButton_6.clicked.connect(self.lineEdit.returnPressed)
        self.pushButton_11.clicked.connect(self.buttonPress)
        self.pushButton_17.clicked.connect(self.lineReset)
        self.pushButton_17.clicked.connect(self.lineFocus)
        self.pushButton_20.clicked.connect(self.deleteRow)         
        self.pushButton_21.clicked.connect(self.recieptWindow)
        
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.pushButton_7.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_14.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_15.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_17.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_18.setText(QtGui.QApplication.translate("MainWindow", "Barcode", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_19.setText(QtGui.QApplication.translate("MainWindow", "Cash", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_20.setText(QtGui.QApplication.translate("MainWindow", "Delete\nItem", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_21.setText(QtGui.QApplication.translate("MainWindow", "RECIEPT", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_22.setText(QtGui.QApplication.translate("MainWindow", "btn", None, QtGui.QApplication.UnicodeUTF8))
        
    def getSelectedRow(self):
        try:
            self.seli = self.tableWidget.selectedIndexes()
            self.row = self.seli[0].row()
        except:
            self.row = -1
        return self.row
        
    #TODO: update tot when deleting row
    def deleteRow(self):
        try:
            self.r = self.getSelectedRow()            
            if (self.r > -1):
                self.tableWidget.removeRow(self.r)
                self.r -= 1
                self.rowCount -= 1
        except:
            print "Nothing selected"

    #TODO: cyclic traverse?
    def traverseDown(self):
        self.r = self.getSelectedRow()
        if (self.r != self.rowCount-1):
            self.r += 1
            self.tableWidget.selectRow(self.r)
        
    def traverseUp(self):
        self.r = self.getSelectedRow()
        if (self.r > 0):
            self.r -= 1
            self.tableWidget.selectRow(self.r)
        
    def returnPressedHandler(self):
        if (self.pushButton_18.isChecked()):
            self.DB()
        if (self.pushButton_19.isChecked()):
            self.payCash()
        self.lineReset()
        self.updateLabels()

    # TODO: rounding ?
    def payCash(self):
        try:
            self.cash = Decimal(self.lineEdit.text())
            self.tot = Decimal(self.tot)-self.cash
        except:
            print "invalid input"

    def updateLabels(self):
        if (self.tot > 0):
            self.totLabel.setText("Total Price:\n" + str(self.tot) + " euro")
        if (self.tot <= 0):
            if (self.tot == 0):
                self.tot *= -1
            self.totLabel.setText("Change back: " + str(self.tot*-1))
            self.dbROW = "Change back: " + str(self.tot*-1)
        self.label.setText(self.dbROW)
      
    #TODO: reload db when adding stuff in adminPOS(now you have to restart clientPOS)  
    def DB(self):
        self.tableWidget.setRowCount(self.rowCount+1)
        line = self.lineEdit.text()
        try: #test if input is int
            line = int(line)
            
            line = str(line)
            
            Decimal(self.tot)
            
            if (line): #test if line exists
                if MySQLc.cur.execute("select BARCODE,PRODUCT,PRICE from itemTable where BARCODE = " + line + ";"):
                    #test if mysql returns any rows at all
                    for row in MySQLc.cur.fetchall():
                        self.tableWidget.setItem(self.rowCount,0,QtGui.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(self.rowCount,1,QtGui.QTableWidgetItem(str(row[1])))
                        self.tableWidget.setItem(self.rowCount,2,QtGui.QTableWidgetItem(str(row[2])))
                        self.rowCount += 1
                        self.tot += Decimal(row[2])
                        self.dbROW = row[1] + ": " + str(row[2]) + " euro\nTotal Price: " + str(self.tot) + " euro"
                else: #no rows returned
                    self.tableWidget.setRowCount(self.rowCount)
                    print "no rows returned"
            else: #empty line
                self.tableWidget.setRowCount(self.rowCount)
                print "empty line"
        except: #non-int
            self.tableWidget.setRowCount(self.rowCount)
            print "NaN"
            
    def window(self):
            if self.customerWindow is None:
                self.window = QtGui.QMainWindow()
                self.window.setGeometry(50, 50, 500, 100)
                self.window.setWindowTitle('Customer Window')
                self.window.setAttribute(QtCore.Qt.WA_ShowWithoutActivating)
                self.customerWindow = self.window
            self.window = self.customerWindow
            self.windowCentralWidget = QtGui.QWidget(self.window)
            self.window.setCentralWidget(self.windowCentralWidget)
            self.label = QtGui.QLabel(self.windowCentralWidget)
            self.label.setGeometry(QtCore.QRect(10, 0, 500, 100))
            self.label.setFont(self.font)
            self.label.setText(self.dbROW)

            self.window.show()
        
        
            print self.tableWidget.geometry()
        
            print self.tableWidget.width()
#THIS HERE IS THE INTERESTING PART, THE FOR-LOOP SUCCESSFULLY PRINtS OUT EACH ELEMENT OF THE TABLEWIDGET
#THE exp.main() CALLS the main() in the lol.py program which the outputs the message "Hej alla barn" 
# trying to change the initUI function to take 2 argument i.e. initUI(self, ASS) seems to be impossible 
#cause when calling this funtion with exp.initUI(tex) error "initUI takes two arguments pops-up" ??? this is not
# good and i therefore will imidiately move to peru where i intend to live my life as a Llama....
    def recieptWindow(self):
        
        tex = " "
        #loops through our table and prints out each element with containging info
        for x in range (0, self.rowCount):
                      
            for y in range (0, 3):
                tex += self.tableWidget.item(x,y).tex()+" "
            tex += "\n"
        print tex  
        exp = Example()
        exp.main()
                        
    def barcodeWindow(self):
            self.barcodeWindow = QtGui.QMainWindow()
            self.barcodeWindow.setGeometry(700, 50, 500, 60)
            self.barcodeWindow.setWindowTitle('Barcode')
            self.bcCentralWidget = QtGui.QWidget(self.barcodeWindow)
            self.barcodeWindow.setCentralWidget(self.bcCentralWidget)
            self.bcLineEdit = QtGui.QLineEdit(self.bcCentralWidget)
            self.bcLineEdit.setGeometry(QtCore.QRect(10, 10, 340, 40))
            self.rx = QtCore.QRegExp("[1-9]\\d{0,19}") #accept first number 1-9, then any numbers (string length = 20)
            self.validator = QtGui.QRegExpValidator(self.rx)
            self.bcLineEdit.setValidator(self.validator)
            self.bcLineEdit.setText("")
            self.bcButton = QtGui.QPushButton(self.bcCentralWidget)
            self.bcButton.setText("Scan!")
            self.bcButton.setGeometry(QtCore.QRect(350, 10, 140, 40))
            
            self.bcButton.clicked.connect(self.barcodeMethod)
            self.bcLineEdit.returnPressed.connect(self.barcodeMethod)
            
            self.barcodeWindow.show()
            
    def barcodeMethod(self):
        self.lineEdit.setText(self.bcLineEdit.text())
        self.DB()
        self.updateLabels()
        self.lineReset()
        self.bcLineEdit.setFocus()
        
    def lineReset(self):
        self.lineEdit.setText("")
        self.bcLineEdit.setText("")
        
    def lineFocus(self):
        self.lineEdit.setFocus()
            
    def buttonPress(self): #button 1 press test
        self.lineEdit.setText(self.lineEdit.text() + "1")

from PySide import QtDeclarative

class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.window()
        self.ui.barcodeWindow()
  
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
