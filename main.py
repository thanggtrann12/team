from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UI(QtWidgets.QMainWindow):
    """Run the main window"""
    def __init__(self, ):
        super(UI, self).__init__()
        uic.loadUi("ui/mainWindow.ui", self)
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec_()
