import serial
from PyQt5 import QtWidgets
import threading
from event.event import readCard
card = readCard()
card.observe('event1', card.handler)


def find_port(self):
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    for port, desc, _ in sorted(ports):
        portDetail = "{}: {}".format(port, desc)
        self.portList.addItem(portDetail)


def connect_port(self):
    ser = serial.Serial(self.portList.currentText(), 115200, timeout=1)
    if ser.is_open:
        self.portStatusLabel.setStyleSheet(
            "background-color: green; color :green;")
        self.portStatusLabel.setText("C")
        ser.close()
        read_card = threading.Thread(
            target=card.handler, args=(self.portList.currentText(),))
        read_card.start()

        return True
    else:
        self.portStatusLabel.setStyleSheet(
            "background-color: red; color :green;")
        self.portStatusLabel.setText("D")
        return False
