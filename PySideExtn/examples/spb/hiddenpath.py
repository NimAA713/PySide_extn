import sys
from PySide6 import QtCore, QtWidgets, QtGui

from PySideExtn import spiralProgressBar #IMPORT THE EXTENSION LIBRARY

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.hello = 'Spiral Progress Bar'
        
        self.spbN = spiralProgressBar()    #SPIRAL PROGRESSBAR OBJECT

        self.spbN.spb_lineWidth(15)

        self.spbN.spb_setPathHidden(True)

        self.spbN.spb_setValue((55, 15, 69))

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.spbN)
        self.setLayout(self.layout)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())