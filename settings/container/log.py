import datetime


def success_log(self, acction, teamname):
    """This function is used to add a success log"""
    self.log_container.addItem(
        "Success " + acction+" with team "+teamname+" at "+str(datetime.datetime.now()))


def failed_log(self, acction, teamname, case):
    """This function is used to add a failed log"""
    self.log_container.addItem(
        "Failed " + acction + " with team "+teamname + " at " + str(datetime.datetime.now()) + " because " + case)
