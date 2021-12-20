from sortedcontainers import SortedDict as SortedDict
from sortedcontainers import SortedList as SortedList
import datetime
from uuid import uuid4 as uid

def idgen():
    memid = uid().int
    return memid

def year():
    now = datetime.datetime.now()
    return int(now.year)



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

    def removeSport(self,sport):
    
        selected = self.namesportsdict
        remID = sport.sportID
        selected.__delitem__(sport.sportname)
        otherselection = self.sportsdict
        otherselection.__delitem__(remID)
        #self.sportsdict.pop[sport.sportname]
        return None

