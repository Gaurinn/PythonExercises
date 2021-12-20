from helpFunctions import *

def signUpMenu():
    running = True
    while running:
        cleanScreen()
        print(12*" " + "SIGN UP")
        fancyLine()
        print("r. To return to main menu")
        fancyLine()
        selectedmember = selectMember()

        if selectedmember != None:
            cleanScreen()
            print("You have selected the following member")
            fancyLine()
            print(selectedmember)
            fancyLine()
            selectedsport = selectSport(selectedmember)

            result = registry.addmembertosport(selectedmember, selectedsport)

            if result.success == True:
                if result.waitinglist == False:
                    print("Member {} added to sport {}".format(selectedmember.name, selectedsport))
                else:
                    print("Member {} added to waiting list to sport {}".format(selectedmember.name, selectedsport))
            else:
                print("Could not add member {} to sport {}".format(selectedmember.name, selectedsport))

            input("Press any key to continue ...")
        else:
            running = False
                        
 


def selectSport(selectedmember=None):
    running = True
    selectedsport = None

    while running == True:
        sportslist = registry.getAllSports()
        for x, sports in enumerate(sportslist):
            print(str(x + 1) + ". " + str(sports))
        fancyLine()
        sportnumber = str(input("please enter sport number to select for {} ".format(selectedmember.name)))
        
        if sportnumber.isnumeric() and int(sportnumber)-1 < len(sportslist):
            selectedsport = sportslist[int(sportnumber) - 1]
            running = False

    return selectedsport

        #selectedmember = registry.getMembersByName(memberName)
        #registry.addmembertosport(selectedmember)