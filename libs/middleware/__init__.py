# coding:utf-8
from libs.singleton import Singleton


class MiddleWareControl(Singleton):
    class _DefaultMiddleWare:
        async def verify(self, netpackage,wrap):
            print("default")
            return True

    pluginsMiddleWareMap = dict()
    globalMiddleWare = _DefaultMiddleWare()

def globalMiddleWare():
    def rg(mw):
        MiddleWareControl().globalMiddleWare = mw()

    return rg
