from mqtt.client.client import publish
from ui.component.msgAlert import msgPopUp
from settings.container.log import success_log, failed_log
payload = {
    "Name": "",
    "Size": "",
    "Pin": ""
}


def add_team(self):
    """This function is used to add a team information"""
    name = self.team_name.text()
    code = self.txt_code.text()
    size = self.team_height.text() + " cm " + self.team_weight.text() + \
        " cm " + self.team_long.text() + " cm "
    pin = self.team_pin.text()
    if name == "" or size == "" or pin == "" or code == "":
        failed_log(self, "add", name, "empty field")
        msgPopUp("Please fill in all the fields", "Error")
    else:
        self.infor_container.addItem(
            "Team Name: "+name + "  Team Size: "+size+"  Team Pin: "+pin+" V")
        success_log(self, "Add Team", name)
        payload["Name"] = name
        payload["Size"] = size
        payload["Pin"] = pin
        if (publish(code, str(payload))):
            msgPopUp("Team added successfully", "Success")
            self.team_name.setText(" ")
            self.team_pin.setText(" ")
            self.team_height.setText(" ")
            self.team_weight.setText(" ")
            self.team_long.setText(" ")
        else:
            failed_log(self, "add", name, "mqtt failed")
