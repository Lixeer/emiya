# coding:utf-8
import os
import importlib
import inspect
from libs.Logger import logInfo, logError


class PluginLoader():

    def __init__(self):
        self.pls = []

    def load(self):
        dir = os.listdir("plugins")
        pluginls = [os.path.splitext(filename) for filename in dir if filename != "__pycache__"]
        pluginls = [i[0] for i in pluginls]
        for pl in pluginls:
            try:
                m = importlib.import_module(f'plugins.{pl}') #会输出三次 uvicorn的锅 todo:塞main里
                logInfo(f"{pl}|The plugin has been loaded")
                self.pls.append(m)
            except Exception as e:
                logError(f"{pl} can not be loaded")
                logError(e)

if __name__ == "__main__":

    aPluginsLoader = PluginLoader()
    aPluginsLoader.load()

# 先加载插件


import time
import requests
import argparse
import asyncio
import json

from fastapi import Request, FastAPI, WebSocket
import uvicorn

from libs.Logger import Log
from libs.netpackage.postpackage import PostPackageFactory
from libs.event.qqevent import EventControl, aEventControl
from libs.action import Action
from libs.middleware import MiddleWareControl
import middleware

from  libs.action import Action
app = FastAPI()

log = Log()
aMiddleWare=MiddleWareControl()
npackage = PostPackageFactory()



class Wraper:
    def __init__(self, actioner, netpackage):
        self.actioner = actioner
        self.callAPI = actioner.callAPI
        self.netpackage = netpackage


@app.websocket("/emiya/onebot11/")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()
    log.logInfo("connected")
    while True:

        data = await websocket.receive_text()
        data = json.loads(data)
        log.logDebug(data)
        for each in aEventControl.eventList:
            if each[0].isPass(data=data):
                sig = inspect.signature(each[1])
                params_list = [params[0] for params in sig.parameters.items() if params[0] != "websocket"]
                d = dict()
                for k in params_list:
                    try:
                        d[k] = data[k]
                    except Exception as e:
                        logError(f"{k} can not be found",e)


                await each[1](websocket, **d)



        '''
        for each in aEventControl.eventList:
            print(each)
            await each[1](websocket,data)'''


@app.post("/hook")
async def handle():
    pass


@app.get("/hello")
async def test():
    return "test"


if __name__ == "__main__":
    log.logInfo("emiya正在启动")




    uvicorn.run("main:app", port=5703, host="0.0.0.0", log_level="warning")
