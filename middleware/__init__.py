#coding:utf-8
from libs.middleware import globalMiddleWare
from libs.middleware.protocol import GlobalMiddleWare
from libs.netpackage.postpackage import AbsPostPackage
@globalMiddleWare ()
class MyMiddleWare(GlobalMiddleWare):
    async def verify(self,netpackage:AbsPostPackage,wrap)->bool:
        try:
            id=netpackage.getSender().user_id
            if id == 123456:
                print("ok")
                return True
            else:
                return False
        except:
            return True

