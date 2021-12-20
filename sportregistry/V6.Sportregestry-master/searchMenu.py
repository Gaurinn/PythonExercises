from helpFunctions import *

def searchMenu():
    running = True

    while running:
        cleanScreen()
        print(" "*12+"SEARCH")
        fancyLine()
        print("f. Find a member by phone ")
        print("n. Find a member by name  ")
        print("e. Find a member by email ")
        print("b. Find a member by birth year ")
        fancyLine()
        print("r. To return to main menu")
        fancyLine()
        memberselection = str(input("Please enter your choice: ")).lower()
        if memberselection == "f":
            running = searchFindMemberByPhone()
        elif memberselection == "n":
            running = searchFindMemberByName()
        elif memberselection == "e":
            running = searchFindMemberByEmail()
        elif memberselection == "b":
            running = searchFindMemberByYob()


        elif memberselection == "r":
            running = False


def searchFindMemberByPhone():
    continueMenu = True    
    running = True

    while running:
        cleanScreen()
        print(" "*8 + "SEARCH BY PHONE")
        fancyLine()
        phone = str(input("please enter a valid 7 digit phone number "))
        cleanScreen()
        if len(phone) == 7 and phone.isnumeric():
            selectedmember = registry.getMembersByPhone(phone)
            print("You entered the following phonenumber: {}\n".format(phone))
            print("You found the following member\n"+"-"*30)
            print(selectedmember)
            phonequesiton = str(input("hit s to search again, any other key to return to main menu ")).lower()
            if phonequesiton != "s":
                continueMenu = False
                running = False
        else:
            idiotinput = str(input("it seems you entered a incorrect phone number or it does not exist \n\n" +
                                    "hit y to try again or any key to return to main menu ")).lower()
            if idiotinput != "y":
                continueMenu = False
                running = False

    return continueMenu

def searchFindMemberByName():
    continueMenu = True    
    running = True

    while running:
        cleanScreen()
        print(" "*8 + "SEARCH BY NAME")
        fancyLine()
        name = str(input("Please enter a member name: "))
        cleanScreen()
        if len(name) > 0:
            selectedmembers = registry.getMembersByName(name)

            if (selectedmembers != None):
                print("You found the following members:\n"+"-"*30)
                for member in selectedmembers:
                    print(str(member) + "\n")
            else:
                print("No members found with the name " + name + "\n")
            again = str(input("Hit s to search again, any other key to return to main menu ")).lower()
            if again != "s":
                continueMenu = False
                running = False
        else:
            idiotinput = str(input("It seems you entered a incorrect member name or it does not exist \n\n" +
                                    "hit y to try again or any key to return to main menu ")).lower()
            if idiotinput != "y":
                continueMenu = False
                running = False

    return continueMenu



def searchFindMemberByEmail():
    continueMenu = True    
    running = True

    while running:
        print(" "*8 + "SEARCH BY EMAIL")
        fancyLine()
        email = str(input("Please enter a email address "))
        cleanScreen()
        if len(email) > 0:
            selectedmember = registry.getMembersByEmail(email)

            if (selectedmember != None):
                print(selectedmember)
            else:
                fancyLine()
                print("Im not sorry, No members found with the email: " + email + "\n")
            fancyLine()
            again = str(input("Hit s to search again, any other key to return to main menu ")).lower()
            fancyLine()
            cleanScreen()
            if again != "s":
                continueMenu = False
                running = False
        else:
            idiotinput = str(input("it seems you entered a incorrect email or it does not exist \n\n" +
                                    "hit y to try again or any key to return to main menu ")).lower()
            if idiotinput != "y":
                continueMenu = False
                running = False

    return continueMenu

def searchFindMemberByYob():
    continueMenu = True    
    running = True

    while running:
        print(" "*3 + "SEARCH BY YEAR OF BIRTH")
        fancyLine()
        yob = str(input("Please enter a birth year "))
        cleanScreen()
        if len(yob) > 0:
            selectedmembers = registry.getMembersByYob(yob)
            if (selectedmembers != None):
                print("You found the following members:\n"+"-"*30)
                for member in selectedmembers:
                    print(str(member) + "\n")
            else:
                print("No members found with the birth year " + yob + "\n")
            again = str(input("Hit s to search again, any other key to return to main menu ")).lower()
            if again != "s":
                continueMenu = False
                running = False
        else:
            idiotinput = str(input("it seems you entered a incorrect birth year or it does not exist \n\n" +
                                    "hit y to try again or any key to return to main menu ")).lower()
            if idiotinput != "y":
                continueMenu = False
                running = False

    return continueMenu


