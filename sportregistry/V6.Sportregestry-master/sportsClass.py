from sortedcontainers import SortedDict as SortedDict
from sortedcontainers import SortedList as SortedList
import datetime
from uuid import uuid4 as uid

def idgen():
    memid = str(uid().int)
    return memid

def year():
    now = datetime.datetime.now()
    return int(now.year)



class Sports:
    class AddMemberToSportResult:
        def __init__(self, success, waitinglist):
            self.success = success
            self.waitinglist = waitinglist

    def __init__(self,sportname,maxmembers = 0,sportid = None):
        self.sportname = sportname
        if sportid == None:
            self.sportID = idgen()
        else:
            self.sportID = sportid
        self.maxmembers = int(maxmembers)
        self.membercount = 0
        self.memberlist = set()
        self.waitinglist = set()
        
    def addMemberToSport(self,member):
        if self.maxmembers > 0 and self.membercount == self.maxmembers:
            self.waitinglist.add(member.id)
            return Sports.AddMemberToSportResult(True, True)
        else:                
            self.memberlist.add(member.id)
            self.membercount += 1
            return Sports.AddMemberToSportResult(True, False)

    def __str__(self):
        return self.sportname
    
    # def __lt__(self, other):
    #     return self.sportID < other.sportID

    # def __eq__(self, other):
    #     return self.sportID == other.sportID

    # def __gt__(self, other):
    #     return self.sportID > other.sportID
              
              
class SportsList:
    def __init__(self):
        self.sportsdict = SortedDict()
        self.namesportsdict = SortedDict()

    def addSport(self,sportname,maxmembers,sportid=None):
        newsport = Sports(sportname, maxmembers, sportid)
        self.sportsdict[newsport.sportID] = newsport  ##krassaði sem int newsport.sportID t[str(newsport.sportID)] = newsport
        self.namesportsdict[sportname] = newsport.sportID
        return newsport
    
    def getAllSports(self):
        sportlist = list()
        for sport in self.sportsdict.values():
            sportlist.append(sport)
        return sportlist

    def getSportById(self, sportid):
        if self.sportsdict.__contains__(sportid):
            return self.sportsdict[sportid]
        else:
            return None

    def removeSport(self,sport):
    
        selected = self.namesportsdict
        remID = sport.sportID
        selected.__delitem__(sport.sportname)
        otherselection = self.sportsdict
        otherselection.__delitem__(remID)
        #self.sportsdict.pop[sport.sportname]
        return None

