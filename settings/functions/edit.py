from settings.container.log import failed_log, success_log


payload = {
    "Name": "",
    "Pin": "",
    "Size": ""
}

size = {
    "long": "",
    "height": "",
    "weight": ""
}


def split_data(data):
    """This function is used to split the data"""
    listData = []
    temp = ""
    for i in range(0, len(data)):
        if data[i] != " ":
            temp += data[i]
        else:
            listData.append(temp)
            temp = ""
    payload["Name"] = listData[2]
    size["height"] = listData[6]
    size["weight"] = listData[8]
    size["long"] = listData[10]
    for i in range(6, 12):
        if i % 2 != 0:
            payload["Size"] += listData[i]
            payload["Size"] += " "
        else:
            payload["Size"] += listData[i]
    payload["Pin"] = listData[len(listData) - 1]
    return payload, size


def edit_team(self):
    """This function is used to edit a team information"""
    if self.infor_container.currentRow() == -1:
        failed_log(self, "edit", "", "no team selected")
        pass
    else:
        data = self.infor_container.currentItem().text()

        self.infor_container.takeItem(self.infor_container.currentRow())
        dataPure, sizePure = split_data(data)
        self.team_name.setText(str(dataPure["Name"]))
        self.team_pin.setText(dataPure["Pin"])
        self.team_height.setText(sizePure["height"])
        self.team_weight.setText(sizePure["weight"])
        self.team_long.setText(sizePure["long"])
        success_log(self, "Edit Team", dataPure["Name"])
