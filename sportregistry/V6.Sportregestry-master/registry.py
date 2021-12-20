import csv

#####Classes######
from memberClass import *
from undoClass import *
from sportsClass import *
##################



class Registry:
    def __init__(self):
        self.membertally  = MemberList()
        self.sportstally = SportsList()
        self.undolists = UndoLists()

    def addmember(self,name,yob,phone,email):
        return self.membertally.addmember(name, yob, phone, email)

    def getMemberByID(self, memberid):
        return self.membertally.getmembersByID(memberid)

    def getMembersByPhone(self, phone):
        return self.membertally.getmembersByPhone(phone)

    def getMembersByName(self, name):
        return self.membertally.getMembersByName(name)

    def getMembersByEmail(self,email):
        return self.membertally.getmembersByEmail(email)

    def getMembersByYob(self,yob):
        return self.membertally.getmembersByYob(yob)
    
    def addNewSport(self,name, maxmembers):
        return self.sportstally.addSport(name, maxmembers)

    def getAllMembers(self):
        return self.membertally.getAllMembers()

    def addmembertosport(self,selectmember,selectedsport):
        result = selectedsport.addMemberToSport(selectmember)

        if result.success == True:
            result.success = selectmember.addMemberToSport(selectedsport)

        return result

    def getMembersForSport(self, sport):
        members = list()

        for memberid in sport.memberlist:
            member = self.membertally.getmembersByID(memberid)
            members.append(member)

        return members

    def getSportById(self, sportid):
        return self.sportstally.getSportById(sportid)

    def removeMemberfromregistry(self,selectmember):
        return self.membertally.removeMember(selectmember)

    def removeSportfromregistry(self,sport):
        return self.sportstally.removeSport(sport)
    
    
    def addToUndoLists(self,passedobject):
        return self.undolists.addToRemoveDict(passedobject)

    def getAllSports(self):
        return self.sportstally.getAllSports()
    
    def getAllRemoved(self):
       return self.undolists.getRemovedObjects()

    def readFromFiles(self):
        self.readMembersFromFile()
        self.readSportsFromFile()
        self.addToUndoLists

        members = self.membertally.getAllMembers()

        for member in members:
            for sportid in member.sports:
                if sportid.isnumeric():
                    sport = self.getSportById(sportid)
                    sport.addMemberToSport(member)

    def writeToFiles(self):
        self.writeMembersToFile()
        self.writeSportsToFile()
        self.writeMembersToUndolist()


    def readMembersFromFile(self):
        with open('members.csv', newline='') as memberfile:
            reader = csv.reader(memberfile, delimiter=';', quotechar='|')
            for row in reader:
                memid = row[0]
                name = row[1]
                yob = row[2]
                phone = row[3]
                email = row[4]
                sports = row[5]
                member = self.membertally.addmember(name, yob, phone, email, memid)

                member.sports = set(sports.split(","))

    def readMembersFromUndoFile(self):
        if len(self.undolists.removedobjects[Member]) > 0:
            with open('undomembers.csv', newline='') as memberfile:
                reader = csv.reader(memberfile, delimiter=';', quotechar='|')
                for row in reader:
                    memid = row[0]
                    name = row[1]
                    yob = row[2]
                    phone = row[3]
                    email = row[4]
                    sports = row[5]
                    member = self.undolists.getRemovedObjects(name, yob, phone, email, memid)

                    member.sports = set(sports.split(","))
        else:
            pass


    def writeMembersToFile(self):
        with open('members.csv', 'w', newline='') as memberfile:
            writer = csv.writer(memberfile, delimiter=';', quotechar='|')
            for currentmember in self.membertally.getAllMembers():
                sports = ",".join(currentmember.sports)
                writer.writerow([currentmember.id, currentmember.name, 
                    currentmember.yob, currentmember.phone, currentmember.email, sports])

    def writeMembersToUndolist(self):
        if len(self.undolists.removedobjects[Member]) > 0:
            objectlist = self.undolists.getRemovedOMemberObjects()
            with open('undomembers.csv', 'w', newline='') as undofile:
                writer = csv.writer(undofile, delimiter=';', quotechar='|')
                for i in range(0,len(objectlist)):
                    sports = ",".join(objectlist[i].sports)
                    writer.writerow([objectlist[i].id, objectlist[i].name, 
                            objectlist[i].yob, objectlist[i].phone, objectlist[i].email, sports])
                   
        else:
            pass



    def readSportsFromFile(self):
        with open('sports.csv', newline='') as sportsfile:
            reader = csv.reader(sportsfile, delimiter=';', quotechar='|')
            for row in reader:
                sportid = row[0]
                name = row[1]
                maxmembers = row[2]
                self.sportstally.addSport(name, maxmembers, sportid)

    def writeSportsToFile(self):
        with open('sports.csv', 'w', newline='') as sportsfile:
            writer = csv.writer(sportsfile, delimiter=';', quotechar='|')
            for currentsport in self.sportstally.getAllSports():
                writer.writerow([currentsport.sportID, currentsport.sportname, currentsport.maxmembers])          


