from observer.observer import Observer
import serial

dataResend = []


class readCard(Observer):

    def __init__(self):
        Observer.__init__(self)

    def handler(self, agrs):
        global dataResend, read_flag
        ser = serial.Serial(agrs, 9600, timeout=0.5)
        while (1):
            data = str(ser.read(13))
            if data != str(b''):
                dataResend.append(data)
