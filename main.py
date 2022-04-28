from PyQt5 import QtWidgets, uic
import sys
from serials.connectport import find_port, connect_port
from settings.functions.network import check_ping
from serials.readport import read_serial
from PyQt5.QtCore import *
from threading import *
from ui.component.ui import components
from settings.functions.add import add_team
from settings.functions.delete import delete_team
from settings.functions.edit import edit_team


class UI(QtWidgets.QMainWindow):
    """Run the main window"""

    def __init__(self, ):
        super(UI, self).__init__()
        uic.loadUi("ui/mainWindow.ui", self)
        components(self)
        if check_ping(self):
            find_port(self)
            self.refresh_port.clicked.connect(lambda: find_port(self))
            self.btn_connect_port.clicked.connect(lambda: connect_port(self))
            self.btn_add_team.clicked.connect(lambda: add_team(self))
            self.btn_delete_team.clicked.connect(lambda: delete_team(self))
            self.btn_edit_team.clicked.connect(lambda: edit_team(self))
            timer = QTimer(self)
            timer.timeout.connect(lambda: read_serial(self))
            timer.start(1000)
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec_()
