# coding:utf-8
import libs.singleton


class EventControl(libs.singleton.Singleton):
    # [(AbsEvent,callable)]
    def __init__(self):
        self.eventList = []


class AbsEvent:

    def isPass(self, netpackage) -> bool:
        pass

class TestEvent(AbsEvent):
    def __init__(self, number):
        self.number=number

    def isPass(self, netpackage) -> bool:
        if netpackage.message != "":
            return True


class KeyWordEvent(AbsEvent):
    def __init__(self, keywordList, rate):

        self.keywordList = keywordList

    def isPass(self, netpackage) -> bool:
        try:
            for i in self.keywordList:
                if i in netpackage.message:
                    return True

        except:
            pass

        return False


class CommandEvent(AbsEvent):
    def __init__(self, cmd: list[str], prompt: list[str] = None):
        """


        :param cmd:命令
        :param prompt:命令提示符
        """
        if prompt == None:
            self.promat = [""]
        else:
            self.promat = prompt

        self.cmd = cmd

    def isPass(self, netpackage) -> bool:
        try:
            s = netpackage.message

            for i in self.promat:
                for k in self.cmd:

                    if s.startswith(i + k):
                        netpackage.arg = s.replace(i + k, "", 1)

                        return True


        except Exception as e:
            # print(e)
            pass

        return False


class AtEvent(AbsEvent):
    """
    :atee :被at者
    """
    def __init__(self, atee):
        self.atee = atee
        pass

    def isPass(self, netpackage) -> bool:
        try:
            for i in self.atee:
                if i in netpackage.message:
                    """
                    TODO?
                    """
                    return True
        except:
            pass
        return False

class MessageEvent(AbsEvent):
    def __init__(self):
        pass
    def isPass(self,netpackage) -> bool:
        try:
            if self.netpackage.post_type == "message":
                return True
        except:
            return False



def onkeyword(keywordList, rate=1):
    def rg(callback):
        EventControl().eventList.append((KeyWordEvent(rate=rate, keywordList=keywordList), callback))
        # print("38",EventControl().eventList)
    return rg


def oncommand(*, promat: list[str], cmd: list[str], rate=1):
    def rg(callback):
        EventControl().eventList.append((CommandEvent(cmd=cmd, prompt=promat), callback))
        # print("38",EventControl().eventList)
    return rg


def onmessage(rate=1):
    def rg(callback):
        EventControl().eventList.append((MessageEvent(),callback))
    
    return rg


def ontest(number, rate=1):
    def rg(callback):
        EventControl().eventList.append((TestEvent(number=number),callback))

    return rg

aEventControl = EventControl()
