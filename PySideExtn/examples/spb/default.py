import sys
from PySide6 import QtCore, QtWidgets, QtGui

from PySideExtn import spiralProgressBar #IMPORT THE EXTENSION LIBRARY

x = 0
p = 1

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.hello = 'Spiral Progress Bar'
        self.button = QtWidgets.QPushButton("Click me to change Value")
        self.text = QtWidgets.QLabel("Spiral Progress Bar")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        
        self.spb = spiralProgressBar()    #CREATING THE SPIRAL PROGRESS BAR OBJECT
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        
        self.layout.addWidget(self.spb) # ADDING THE SPIRAL PROGRESS BAR OBJECT TO THE LAYOUT

        self.setLayout(self.layout)
        self.button.clicked.connect(self.magic) #BUTTON PRESSED EVENT
        
    def magic(self):
        global x, p
        x = x + 10*p
        if x==100:
            p = -1
        elif x==0:
            p = 1
        self.spb.spb_setValue((x, x*2, x*3))        #CHANGING THE VALUE OF THE 3 DEFAULT PROGRESS BAR
        out_text = 'Spiral Progress Bar: ' + str(x) + '%, ' + str(2*x) + '%, ' + str(3*x) + '%'
        self.text.setText(out_text)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())