from mqtt.client.client import publish
from settings.container.log import success_log, failed_log
payload = {
    "Name": "",
    "Size": "",
    "Pin": ""
}


def delete_team(self):
    """This function is used to delete a team information"""
    code = self.txt_code.text()
    if self.infor_container.currentRow() == -1:
        failed_log(self, "delete", "", "empty field")
        pass
    else:
        self.infor_container.takeItem(self.infor_container.currentRow())
        payload["Name"] = code
        payload["Size"] = ""
        payload["Pin"] = ""
        if publish(code, str(payload)):
            success_log(self, "Delete Team", code)
        else:
            failed_log(self, "Delete", code, "mqtt failed")
