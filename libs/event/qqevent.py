# coding:utf-8
import libs.singleton


class EventControl(libs.singleton.Singleton):
    #[(AbsEvent,callable)]
    def __init__(self):
        self.eventList=[]



class AbsEvent:
    
    def isPass(self,netpackage)->bool:
        pass

class KeyWordEvent(AbsEvent):
    def __init__(self,keywordList,rate):
        
        self.keywordList=keywordList
        
    def isPass(self,netpackage)->bool:
        try:
            for i in self.keywordList:
                if i in netpackage.message:
                    return True
            
        except:
            pass
        
        return False
        
def onkeyword(keywordList,rate=1):

    def rg(callback):

        EventControl().eventList.append((KeyWordEvent(rate=rate,keywordList=keywordList) , callback))
        #print("38",EventControl().eventList)
    return rg
        
aEventControl=EventControl()