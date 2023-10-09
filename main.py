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

from fastapi import Request, FastAPI

from libs.Logger import Log

from libs.netpackage.postpackage import PostPackageFactory
from libs.event.qqevent import EventControl,aEventControl
from libs import cqinit







'''
BASEURL = "http://127.0.0.1:5700"


def sendGroupMsg(gid: int, text: str):
    d = {"message": text, "group_id": gid}
    print(requests.post(f"{BASEURL}/send_group_msg", data=d))


def getMsg(id: int):
    d = {"message_id": id}
    return requests.post(f"{BASEURL}/get_msg", data=d)
'''

app = FastAPI()
# 使用域内创建

log = Log()

npakage = PostPackageFactory()



@app.post("/")
async def handle(request: Request):
    data = await request.json()

    p=npakage.creat(data)
    
    log.logInfo(p)
    #print(aEventControl.eventList)
    for each in aEventControl.eventList:


        if each[0].isPass(p):

            each[1](p)


    return "data"  # 去掉这行用cq输出 别用main输出cq信息 23.9.11


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
