from uuid import uuid4 as uid
from sortedcontainers import SortedDict as SortedDict
from sortedcontainers import SortedList as SortedList
import datetime
def idgen():
        memid = uid().int
        return memid

def year():
    now = datetime.datetime.now()

    return int(now.year)

class Member:
    def __init__(self,name,yob,phone,email,memid=None):
        self.name = name
        self.yob = yob
        self.phone = phone
        self.email = email
        self.groups = set()
        if memid != None:
            self.id = int(memid)
        else:
            self.id = idgen()

    def __str__(self):
        return "Name: "+ str(self.name)+" Date of birth: "+ str(self.yob) + " Contact Information: "+ str(self.phone) +" "+ str(self.email)

    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, other):
        if other == None:
            return False

        return self.id == other.id

    def __gt__(self, other):
        return self.id > other.id

    def age(self):
        return year() - int(self.yob)

    def addMemberToGroup(self, group):
        self.groups.add(group.groupid)
        return True

class MemberList:
    def __init__(self):
        self.membersByID = dict() #mainmap
        
        self.membersByName =  SortedDict()
        
        self.membersByYob =  SortedDict()
        self.membersByPhone = dict()
        self.membersByEmail = dict()
        

    def addmember(self,name,yob,phone,email,memid = None):
        newmember = Member(name,yob,phone,email, memid)

        self.membersByID[newmember.id] = newmember
        
        if self.membersByName.__contains__(newmember.name) == False:
            self.membersByName[newmember.name] = SortedList()
        self.membersByName[newmember.name].add(newmember)
        
        self.membersByYob[newmember.yob] = newmember.id
        self.membersByPhone[newmember.phone] = newmember.id
        self.membersByEmail[newmember.email] = newmember.id
        return newmember

    def removeMember(self,selectmember):       
        self.membersByID.pop(selectmember.id)

        membersWithName = self.membersByName[selectmember.name]
        membersWithName.remove(selectmember)
        return True

    def getmembersByID(self,ID):
        return self.membersByID[ID]

    def getMembersByName(self, name):
        if self.membersByName.__contains__(name):
            return self.membersByName[name]
        else:
            return None
    
    def getmembersByYob(self,yob):
        yobID = self.membersByYob[yob]
        return self.membersByID[yobID]

    def getmembersByPhone(self,phone):
        phoneID = self.membersByPhone[phone]
        return self.membersByID[phoneID]

    def getmembersByEmail(self, email):

        if self.membersByEmail.__contains__(email):
            emailID = self.membersByEmail[email]
            return self.membersByID[emailID]
            
        else:
            return None



    # def getmembersByEmail(self,email):
    #     emailID = self.membersByEmail[email]
    #     return self.membersByID[emailID]

    def getAllMembers(self):
        memberlist = list()
        for member in self.membersByID.values():
            memberlist.append(member)
        return memberlist    
  
class UndoLists:
    def __init__(self):
        self.removedobjects = dict()
        self.removedobjects[Member] = list()
        self.removedobjects[Sports] = list()
        self.removedobjects[Sports.Groups] = list()


    def addToRemoveDict(self,passedobject):

        self.removedobjects[type(passedobject)].append(passedobject)
        
        return 

    def getRemovedObjects(self):
        objectlist = list()
        for key,value in self.removedobjects:
            objectlist.append((key,value))
        return(objectlist)






class Sports:
    class Groups:
        def __init__(self,sport,groupname,agefrom,ageto,maxmembers = 0):
            self.sport = sport
            self.groupname = groupname
            self.agefrom = agefrom
            self.ageto = ageto
            self.groupid = idgen()
            self.maxmembers = maxmembers
            self.membercount = 0
            self.memberlist = set()
            self.waitinglist = set()

        def __str__(self):
            return self.groupname

        def addMember(self, member):
            if self.membercount < self.maxmembers:
                self.memberlist.add(member.id)
                self.membercount += 1
                return Sports.AddMemberToSportResult(True, False, self)
            else:
                self.waitinglist.add(member.id)
                return Sports.AddMemberToSportResult(True, True, self)

    class AddMemberToSportResult:
        def __init__(self, success, waitinglist, group):
            self.success = success
            self.waitinglist = waitinglist
            self.group = group

    #Hvert sport á lista af hópum eftir aldri
    def __init__(self,sportname,sportid = None):
        self.sportname = sportname
        if sportid == None:
            self.sportID = idgen()
        else:
            self.sportID = int(sportid)
        self.groupsList = list()
        self.littleleague = self.Groups(sportname,str(sportname)+" "+ "littleleague",6,11,50)
        self.middleleague = self.Groups(sportname,str(sportname)+" "+ "middleleague",12,18,50)
        self.primaryleauge = self.Groups(sportname,str(sportname)+" "+ "primaryleauge",19,28,50)
        self.oldboys = self.Groups(sportname,str(sportname)+" "+ "oldboys",29,100,50)
        self.groupsList.append((self.sportID,self.littleleague))
        self.groupsList.append((self.sportID,self.middleleague))
        self.groupsList.append((self.sportID,self.primaryleauge))
        self.groupsList.append((self.sportID,self.oldboys))
        
    def addMemberToSport(self,member):
        memberage = member.age()

        if memberage >= 6 and memberage <= 11:
            result = self.littleleague.addMember(member)
        if memberage >= 12 and memberage <= 18:
            result = self.middleleague.addMember(member)    
        if memberage >= 19 and memberage <= 28:
            result = self.primaryleauge.addMember(member)
        if memberage >= 29 and memberage <= 100:
            result = self.oldboys.addMember(member)

        return result

    def __str__(self):
        return self.sportname
    
    # def __lt__(self, other):
    #     return self.sportID < other.sportID

    # def __eq__(self, other):
    #     return self.sportID == other.sportID

    # def __gt__(self, other):
    #     return self.sportID > other.sportID
              
    def addGroup(self, groupname, agefrom, ageto, maxmembers = 0):
        newgroup = self.Groups(self, groupname, agefrom, ageto, maxmembers)
        self.groupsList.append((self.sportID,newgroup))

    def addMembertoGroup(self,sportname,membername):
        member = MemberList.getMemberbyName[membername]
        sportname = SportsList ## BÆTA MEMBER í SPORT
              
class SportsList:
    def __init__(self):
        self.sportsdict = SortedDict()
        self.namesportsdict = SortedDict()

    def addSport(self,sport,sportid=None):
        newsport = Sports(sport, sportid)
        self.sportsdict[newsport.sportID] = newsport  ##krassaði sem int newsport.sportID t[str(newsport.sportID)] = newsport
        self.namesportsdict[sport] = newsport.sportID
        return newsport
    
    def getAllSports(self):
        sportlist = list()
        for sport in self.sportsdict.values():
            sportlist.append(sport)
        return sportlist

    
        

       


        
        


if __name__ == "__main__":
    m = MemberList()
    #m.addmember()
    # m.addmember("gunnar","1983","7775726","gunnarig@visir.is")
    # m.addmember("gunnar","1983","7775726","gunnarig@visir.is")
    # m.addmember("gunnar","1983","7775726","gunnarig@visir.is")
    # m.addmember("gunnar","1983","7775726","gunnarig@visir.is")
    # testmember = m.addmember("gunnar","1983","7775726","gunnarig@visir.is")
    # m.addmember("gunnar","1983","7775726","gunnarig@visir.is")
    # m.addmember("gunnar","1983","7775726","gunnarig@visir.is")
    # print(m.getMembersByName("gunnar"))
    # print(len(m.getMembersByName("gunnar")))
    # m.removeMember(testmember)
    # print(m.getMembersByName("gunnar"))
    # print(len(m.getMembersByName("gunnar")))
    #print(str(m.getmembersByPhone("7775726")))
    #print(m.getmembersByYob("1983"))
    #print(m.getmembersByEmail("gunnarig@visir.is"))

    s = SportsList()
    s.addSport("Kung fu")
    s.addSport("Chess")
    s.addSport("fishing")
    
    print(s)
    # member = m.getMemberbyName("gunnar")

    #sportsList = s.getAllSports()
    #s.addMemberToSport(member)

 

    # for sport in sportsList:
    #     print(sport)
    

    #print(s)