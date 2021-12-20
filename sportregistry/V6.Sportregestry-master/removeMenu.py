from helpFunctions import *


def removeMenu():
    running = True

    while running:
        cleanScreen()
        print(" "*13 + "REMOVE")
        fancyLine()
        print("ms. to remove a member from a sport")
        print("sp. to remove a sport from registry")
        print("me. to remove a member from registry")
        fancyLine()
        print("r. To return to main menu")
        fancyLine()
        choice = str(input("please enter your choice: "))
        if choice == "r":
            running = False
        elif choice == "ms":
            cleanScreen()
            print("you chose to remove a member from a sport")
            ## Útfæra
        elif choice == "sp":
            cleanScreen()
            fancyLine()
            print("you chose to remove a sport from registry")
            running = removeSport()
        elif choice == "me":
            running = removeMember()
       
 
        
 


def removeMember():
    continueMenu = True
    running = True
    while running:
        cleanScreen()
        print("to REMOVE a member from registry")
        memberToRemove = selectMember()
        if memberToRemove != None:
            print(memberToRemove)
            print("is selected for removal from system: ")
            fancyLine()
            yes = input("hit y to remove, any other key to break: ").lower()
            cleanScreen()
            if yes == "y":

                registry.addToUndoLists(memberToRemove)
                registry.removeMemberfromregistry(memberToRemove)
                cleanScreen()
                fancyLine()
                print(memberToRemove)
                print("Has been removed, If you would like to undo go to savemenu ")
                moar = input("Hit y to remove more, any other key to return to main menu ")
                if moar == "y":
                    return continueMenu
        
                else:
                    running = False
            else:
                running = False
                return running
        else:
            running = False
            return running
        

def removeSport():
    continueMenu = True
    running = True
    while running:
        cleanScreen()
        print("select sport to REMOVE a sport from registry")
        sportToRemove = selectSport()
        if sportToRemove != None:
            print(sportToRemove)
            print("is selected for removal from system: ")
            fancyLine()
            yes = input("hit y to remove, any other key to break: ").lower()
            cleanScreen()
            if yes == "y":
                registry.addToUndoLists(sportToRemove)
                registry.removeSportfromregistry(sportToRemove)
                print("Sport has been removed, If you would like to undo go to savemenu ")
                moar = input("Hit y to remove more, any other key to return to main menu ")
                if moar == "y":
                    return continueMenu
                else:
                    running = False
            else:
                running = False
                return running
        else:
            cleanScreen()
            input("No sports registered, press any key to return to main menu ")
            running = False
            return running
    
        