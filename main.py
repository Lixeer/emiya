# coding:utf-8
import os
import importlib
class PluginLoader():

    def __init__(self):
        self.pls=[]
    def load(self):
        dir = os.listdir("plugins")
        pluginls = [os.path.splitext(filename) for filename in dir if filename != "__pycache__"]
        pluginls = [i[0] for i in pluginls]
        for pl in pluginls:
            m = importlib.import_module(f'plugins.{pl}')
            #print(m)
            self.pls.append(m)
aPluginsLoader=PluginLoader()
aPluginsLoader.load()
#先加载插件

import time
import requests
import argparse
import asyncio

from fastapi import Request, FastAPI,WebSocket

from uvicorn import run

from libs.Logger import Log
from libs.netpackage.postpackage import PostPackageFactory
from libs.event.qqevent import EventControl,aEventControl
from libs.action import Action
from libs import cqinit



app = FastAPI()


log = Log()

npackage = PostPackageFactory()

"""
@app.post("/")
def handle(request:Request)
     data = await request.json()

     p=npakage.creat(data)

     log.logInfo(p)
     #print(aEventControl.eventList)
     for each in aEventControl.eventList:


         if each[0].isPass(p):

             each[1](p)


     return "data"  # 去掉这行用cq输出 别用main输出cq信息 23.9.11
"""
class Wraper:
    def __init__(self,actioner,netpackage):
        self.actioner=actioner
        self.callAPI=actioner.callAPI

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    #print('=================================')
    await websocket.accept()
    while True:
        
        data = await websocket.receive_text()
        log.logDebug(data)
        
        actioner=Action(websocket)
        np=npackage.creat(data)
        
        log.logInfo(np)
        for each in aEventControl.eventList:
            
            if each[0].isPass(np):
                wraper=Wraper(actioner=actioner,netpackage=np)
                await each[1](wraper)
            


        



        
        




@app.post("/hook")
async def handle():
    pass
    

@app.get("/hello")
async def test():
    return "test"









if __name__ == "__main__":

    log.logInfo("emiya正在启动")

    
    import uvicorn

    uvicorn.run("main:app", port=5701, host="0.0.0.0", log_level="warning", workers=2 , reload=True)
