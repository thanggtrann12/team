from PyQt5 import QtWidgets


def components(self):
    self.refresh_port = self.findChild(
        QtWidgets.QPushButton, "btn_refresh")
    self.btn_connect_port = self.findChild(
        QtWidgets.QPushButton, "btn_port")
    self.btn_edit_team = self.findChild(QtWidgets.QPushButton, "btn_edit")
    self.btn_add_team = self.findChild(QtWidgets.QPushButton, "btn_add")
    self.btn_delete_team = self.findChild(QtWidgets.QPushButton, "btn_delete")
    self.team_name = self.findChild(QtWidgets.QLineEdit, "txtName")
    self.team_height = self.findChild(QtWidgets.QLineEdit, "txtHeight")
    self.team_weight = self.findChild(QtWidgets.QLineEdit, "txtWeight")
    self.team_long = self.findChild(QtWidgets.QLineEdit, "txtLong")
    self.team_pin = self.findChild(QtWidgets.QLineEdit, "txtPin")
    self.infor_container = self.findChild(
        QtWidgets.QListWidget, "team_info_container")
    self.log_container = self.findChild(QtWidgets.QListWidget, "log_container")
    self.txt_code = self.findChild(QtWidgets.QLabel, "txtCode")
    self.portList = self.findChild(QtWidgets.QComboBox, "port_container")
    self.portStatusLabel = self.findChild(QtWidgets.QLabel, "lblPortStatus")
