import sys

from PySide import QtGui, QtCore


#lol.py which is needed for pad2.py <3

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
     
    #here u could insert a new argument => u'll get fucktons of errors :(    
    def initUI(self):   
        self.text = "Hej alla barn"
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Reciept')
        self.show()

    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()
        
    def drawText(self, event, qp):
      
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)        
                
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()
    
    
    
    
