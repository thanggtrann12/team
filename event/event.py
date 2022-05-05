from observer.observer import Observer
import serial

dataResend = []


class readCard(Observer):

    def __init__(self):
        Observer.__init__(self)

    def handler(self, agrs):
        global dataResend, read_flag
        ser = serial.Serial(agrs, 9600  , timeout=0.5)
        while (1):
            print("Sendinggg")
            data = str(ser.read(13))
            dataResend.append(data[3:14])
