from registry import *


def cleanScreen():
    print("\n"*100)

def fancyLine():
    print("-"*30)


def selectMember():
    running = True
    selectedmember = None

    while running == True:
        memberName = str(input("please enter a membername: "))
    
        selectedmembers = registry.getMembersByName(memberName)
        if memberName != "r":
            if selectedmembers != None:
                goat = len(selectedmembers)
                if len(selectedmembers) > 1: ### krassar ef allt er fjarlægt.. len virðist ekki virka.
                    while selectedmember == None:
                        cleanScreen()
                        fancyLine()
                        for x, selections in enumerate(selectedmembers):
                            print(str(x + 1) + ". " + str(selections))
                        fancyLine()
                        print("it is apparent that there are multiple members named {}".format(memberName))
                        fancyLine()
                        particularmember = input("Please select the desired member by the number index: ")
                        cleanScreen()
                        
                        if particularmember.isnumeric() and int(particularmember)-1 < len(selectedmembers):
                            selectedmember = selectedmembers[int(particularmember) - 1]
                            running = False
                else:
                    if len(selectedmembers) == 0:
                        print("The world is dust, you removed every member with that name")
                        input("Press any key to continue....")
                        running = False
                    else:    
                        selectedmember = selectedmembers[0]
                        running = False
            else:
                print("Im afraid {} is imaginary\nWould you like to try again? \n".format(memberName))
                again = str(input("y to try again: ")).lower()
                if again != "y":
                    running = False  
        else:
            running = False
    return selectedmember 

def selectSport(selectedmember=None):
    running = True
    selectedsport = None

    while running == True:
        sportslist = registry.getAllSports()

        if len(sportslist) > 0:
            for x, sports in enumerate(sportslist):
                print(str(x + 1) + ". " + str(sports))
            fancyLine()
            if selectedmember == None:

                sportnumber = str(input("Select a sport "))
            else:
                sportnumber = str(input("please enter sport number to select for {} ".format(selectedmember.name)))

            if sportnumber.isnumeric() and int(sportnumber)-1 < len(sportslist):
                selectedsport = sportslist[int(sportnumber) - 1]
                running = False
        else:
            running = False

    return selectedsport


global registry
registry = Registry()