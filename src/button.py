import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class SimpleButton(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 50
        self.top = 50
        self.width = 320
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.buttonA = QPushButton('PyQt5 button', self)
        self.buttonA.setToolTip('This is an example button')
        self.buttonA.move(100,70)
        self.buttonA.clicked.connect(self.on_click)

        self.labelA = QLabel(self)
        self.labelA.setText('Label Example')
        
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        self.labelA.setText('Changed')
        print('PyQt5 button click')

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleButton()
    sys.exit(app.exec_())