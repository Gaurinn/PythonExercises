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


class Member:
    def __init__(self,name,yob,phone,email,memid=None):
        self.name = name
        self.yob = yob
        self.phone = phone
        self.email = email
        self.sports = set()
        if memid != None:
            self.id = memid
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

    def addMemberToSport(self, sport):
        self.sports.add(sport.sportID)
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
        
        if self.membersByYob.__contains__(newmember.yob) == False:
            self.membersByYob[newmember.yob] = SortedList()
        self.membersByYob[newmember.yob].add(newmember)        
        
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
        if self.membersByYob.__contains__(yob):
            return self.membersByYob[yob]
        else:
            return None

    def getmembersByPhone(self,phone):
        if self.membersByPhone.__contains__(phone):
            phoneID = self.membersByPhone[phone]
            return self.membersByID[phoneID]
        else:
            return None

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