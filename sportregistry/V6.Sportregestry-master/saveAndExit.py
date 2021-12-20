from helpFunctions import *

def saveData():
    registry.writeToFiles()
    input("Data saved to files ... press any key to continue")


def exitFunction():
    exitchoice = str(input("Are you sure you want to quit? \nhit x to quit without saving \n"+ 
                            "hit y to save changes to quit \nhit any key to return to main menu")).lower()
    if exitchoice == "x":
        exit()
    elif exitchoice == "y":
        saveData()
        exit()
    else:
        return True