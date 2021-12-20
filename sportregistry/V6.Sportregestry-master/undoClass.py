from sortedcontainers import SortedDict as SortedDict
from sortedcontainers import SortedList as SortedList
from memberClass import *
from sportsClass import *

class UndoLists:
    def __init__(self):
        self.removedobjects = dict()
        self.removedobjects[Member] = list()
        self.removedobjects[Sports] = list()


    def addToRemoveDict(self,passedobject):

        self.removedobjects[type(passedobject)].append(passedobject)
        
        return passedobject

    def getRemovedOMemberObjects(self):
        objectlist = list()
        for value in self.removedobjects[Member]:
            objectlist.append(value)
        return(objectlist)

    def getRemovedSportsObjects(self):
        objectlist = list()
        for key,value in self.removedobjects[Sports]:
            objectlist.append((key,value))
        return(objectlist)
