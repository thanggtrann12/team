import serial
from event.event import dataResend
lastData = ""


def read_serial(self):
    if len(dataResend) > 0 and lastData != dataResend:
        self.txt_code.setText(dataResend[len(dataResend)-1][3:14])
        lastData = dataResend
    else:
        self.txt_code.setText("ccc")
        pass
