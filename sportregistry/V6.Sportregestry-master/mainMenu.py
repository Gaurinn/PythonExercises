#from memberregSorted import *
from helpFunctions import *


######MENUS#######
from addNewMenu import *
from signUpMenu import *
from removeMenu import *
from searchMenu import *
from saveAndExit import *
##################



def mainMenu():
    registry.readFromFiles()
    running = True  
    while running:
        cleanScreen()
        choice = printMain()
        if choice == "1":
            addNewMenu()

        elif choice == "2":
            signUpMenu() ### vantar order by

        elif choice == "3":
            removeMenu()
            
        elif choice == "4":
            searchMenu()
            
        elif choice == "5":
            saveData()

        elif choice == "x":
           running = exitFunction()
             
def printMain():
     #cleanScreen()
    running = True
    while running:
        print(" "*11 + "MAINMENU")
        fancyLine()
        print("1. Registry")
        print("2. Sign Up")
        print("3. Remove")
        print("4. Search")
        print("5. Save data")
        fancyLine()
        print("x. Exit")
        fancyLine()
        choice = str(input("please input your choice to continue :")).lower()
        cleanScreen()
        running = False
    return choice






mainMenu()

