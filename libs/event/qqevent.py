# coding:utf-8

class EventControl:
    eventList=[]



class AbsEvent:
    
    def isPass(self,netpackage)->bool:
        pass

class KeyWordEvent(AbsEvent):
    def __init(self,keywordList,rate):
        
        self.keywordList=keywordList
        
    def isPass(self,netpackage):
        try:
            for i in self.keywordList:
                if i in netpackage.message:
                    return True
            
        except:
            pass
        
        return False
        
def onkeyword(keywordList,rate=1):
    def rg(callback):
        EventControl.eventList.append(( KeywordEvent(rate=rate,keywordList=keywordList) , callback))
        
