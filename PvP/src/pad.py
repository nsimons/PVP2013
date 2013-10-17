# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pad.ui'
#
# Created: Thu Oct 17 11:52:07 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 64, 64))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 10, 64, 64))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 10, 64, 64))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 80, 64, 64))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 80, 64, 64))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtGui.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 80, 64, 64))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtGui.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 150, 64, 64))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtGui.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 150, 64, 64))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtGui.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 150, 64, 64))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtGui.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(220, 10, 64, 64))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtGui.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(220, 80, 64, 64))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtGui.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(150, 220, 64, 64))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtGui.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(220, 150, 64, 135))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtGui.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(10, 220, 130, 64))
        self.pushButton_14.setObjectName("pushButton_14")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Dialog", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Dialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Dialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Dialog", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("Dialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("Dialog", "up", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("Dialog", "down", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("Dialog", "Enter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_14.setText(QtGui.QApplication.translate("Dialog", "?", None, QtGui.QApplication.UnicodeUTF8))


class ControlMainWindow(QtGui.QMainWindow):
  def __init__(self, parent=None):
    super(ControlMainWindow, self).__init__(parent)
    self.ui =  Ui_Dialog()
    self.ui.setupUi(self)
   
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())