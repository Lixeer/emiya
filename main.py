# coding:utf-8
import os
import importlib
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


aPluginsLoader = PluginLoader()
aPluginsLoader.load()
print("emiya")
# 先加载插件


import time
import requests
import argparse
import asyncio
import json

from fastapi import Request, FastAPI, WebSocket


from libs.Logger import Log
from libs.netpackage.postpackage import PostPackageFactory
from libs.event.qqevent import EventControl, aEventControl
from libs.action import Action
from libs.middleware import MiddleWareControl
import middleware

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
    while True:

        data = await websocket.receive_text()
        data = json.loads(data)
        #log.logDebug(data)

        actioner = Action(websocket)
        np = npackage.creat(data)
        try:
            if np.post_type != "meta_event":
                log.logInfo(np)
        except:
            pass


        for each in aEventControl.eventList:

            if each[0].isPass(np):
                wraper = Wraper(actioner=actioner, netpackage=np)
                if not await aMiddleWare.globalMiddleWare.verify(netpackage=np,wrap=wraper):
                    continue

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

    uvicorn.run("main:app", port=5703, host="0.0.0.0", log_level="warning", reload=True)
