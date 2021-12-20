from helpFunctions import *



def addNewMenu():
    running = True
    while running:
        print(12*" " + "REGISTRY")
        fancyLine()
        print("m. To view members")
        print("a. To register a new member")
        print("i. To view all sports")
        print("n. To register a new sport")
        print("r. To return to main menu")
        fancyLine()
        choice = str(input("Please input your choice: "))
        if choice == "m":
            running = viewMembersMenu()
        elif choice == "a":
            running = newMemberMenu()
        elif choice == "i":
            running = viewSportMenu()             
        elif choice == "n":
            running = newSportMenu()
        elif choice == "r":
            return
        cleanScreen()


def newMemberMenu():
    continueMenu = True   
    running = True

    while running:
        name = input("enter a name: ")
        yob = input("enter a year of birth: ")
        phone = input("enter phone number: ")
        email = input("enter a email adress: ")
        
        newmember = registry.addmember(name,yob,phone,email)
        cleanScreen()
        fancyLine()
        if newmember == newmember:
            print("A new member was registered")
            fancyLine() 
            print(" Name: {} Birthyear: {} Phonenumber: {} Email: {}".format(name+"\n",yob+"\n",phone+"\n",email+"n"))
            fancyLine()
            moremembers = str(input("If you would like to register more items push y"+ 
                                        "\nOtherwise gently caress any other key: ")).lower()

            if moremembers != "y":
                continueMenu = False   
                running = False
            else:
                return continueMenu


def newSportMenu():
    continueMenu = True   
    running = True

    while running:
        name = input("Please enter a sport name: ")
        maxmembers = str(input("please input a maximum member count (0 for no maximum) "))
        if maxmembers.isnumeric() == False:
            maxmembers = 0

        newsport = registry.addNewSport(name,maxmembers)
        cleanScreen()
        fancyLine()
        if newsport != None:
            print("A new sport was registered")
            fancyLine() 
            print("Name: " + str(newsport) + "\nMax members: " + str(newsport.maxmembers) + "\n")
            fancyLine()
            moreitems = str(input("If you would like to register more items push y"+ 
                                        "\nOtherwise gently caress any other key: ")).lower()

            if moreitems != "y":
                continueMenu = False   
                running = False
            else:
                return continueMenu



def viewMembersMenu():
    memberlist = registry.getAllMembers()
    memberstoshow = None
    running = True
    continueMenu = True
    
    while running:
        cleanScreen()
        print(" "*9+"SORTING MENU")
        fancyLine()
        print("n. To Order by name")
        print("a. To Order by age")
        print("s. To Order by sport")
        fancyLine()
        print("r. To return to main menu")
        fancyLine()
        choice = str(input("Please make a selection to continue ")).lower()
        if choice == "n":
            memberlist.sort(key=lambda x: x.name)
            memberstoshow = memberlist
        elif choice == "a":
            memberlist.sort(key=lambda x: x.yob)
            memberstoshow = memberlist
        elif choice == "s":
            selectedsport = selectSport()
            memberstoshow = registry.getMembersForSport(selectedsport)
        elif choice == "r":
            running = False
        if memberstoshow != None and len(memberstoshow) > 0:
            print("Members:")
            for member in memberstoshow:
                print(str(member) + "\n")
        else:
            print("No members were found")
        again = str(input("Hit v to view again, any other key to return to main menu ")).lower()
        if again != "v":
            continueMenu = False
            running = False


    return running

def viewSportMenu():
    sportlist = registry.getAllSports()
    running = True
    continueMenu = True
    
    while running:
        cleanScreen()
        print(" "*7 + "SPORT VIEW MENU")
        fancyLine()
        if sportlist != None and len(sportlist) > 0:
            for x, sport in enumerate(sportlist):
                print(str(x + 1) + ". " + str(sport) + ", Max members: " + str(sport.maxmembers) + ", Member count: " + str(sport.membercount) + "\n")
            sportnumber = input("Enter a number of sport to view detailed information, r to return: ").lower()
            if sportnumber != "r":
                if sportnumber.isnumeric():
                    cleanScreen()
                    selectedsport = sportlist[int(sportnumber) - 1]
                    print(str(selectedsport))
                    fancyLine()
                    if len(selectedsport.memberlist) > 0:
                        print("Registered members:")
                        for memberid in selectedsport.memberlist:
                            member = registry.getMemberByID(memberid)
                            print(member)
                    else:
                        print("No registered members")
                    fancyLine()
                    if len(selectedsport.waitinglist) > 0:
                        print("Members in waiting list:")
                        for memberid in selectedsport.waitinglist:
                            member = registry.getMemberByID(memberid)
                            print(member)
                    else:
                        print("No members in waiting list")
                    fancyLine()
            else:
                continueMenu = True
                running = False
        else:
            print("No sports were found")
        again = str(input("Hit v to view again, any other key to return to main menu ")).lower()
        if again != "v":
            continueMenu = False
            running = False


    return running             