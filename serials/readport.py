from multiprocessing.sharedctypes import Value
import serial
from event.event import dataResend
from settings.container.team import team_list
lastData = ""


def read_serial(self):
    global lastData
    
    if len(dataResend) > 5 and dataResend[len(dataResend)-1] != "n'":
      code = dataResend[len(dataResend)-1]
      if code != "":
        print("readinggg: " + code)
        self.txt_code.setText(code)
        self.team_name.setText(team_list[code])
      # for key, value in team_list.items():
      #   if key == code:
      #     self.txt_code.setText(value)
      #     print(code)
      #     lastData = dataResend
