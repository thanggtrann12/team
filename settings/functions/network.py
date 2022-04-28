import os
from PyQt5 import QtWidgets


def check_ping(self):
    self.lbl_ping = self.findChild(QtWidgets.QLabel, "lblStatus")
    hostname = "google.com"
    response = os.system("ping  " + hostname)
    if response == 0:
        self.lbl_ping.setText("Online")
        self.lbl_ping.setStyleSheet("background-color: green")
        return True
    else:
        self.lbl_ping.setText("Offline")
        self.lbl_ping.setStyleSheet("background-color: red")
        return False
