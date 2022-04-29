from multiprocessing.sharedctypes import Value
import serial
from event.event import dataResend
from settings.container.team import team_list
lastData = ""


def read_serial(self):
     
    if len(dataResend) > 0 and lastData != dataResend:
        code = dataResend[len(dataResend)-1][3:14]
        for key, value in team_list.items():
          if key == code:
            self.txt_code.setText(value)
            lastData = dataResend
    else:
        self.txt_code.setText("ccc")
        pass
