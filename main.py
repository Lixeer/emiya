# coding:gbk
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

flag: str = "default"  # default  mix-console  debug
parser = argparse.ArgumentParser(description="主程序脚本，当前为测试阶段测试所用")
parser.add_argument('--debug', help="调试模式", action='store_true')
args = parser.parse_args()

if args.debug:
    flag = "debug"

async def setBody(request):
    receive_ = await request._receive()

    async def receive():
        return receive_

    request._receive = receive


"""
@app.middleware("http")
async def addProcessTimeHeader(request: Request, call_next):
    #日志和适配器请写在中间件
    await setBody(request)
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time


    data = await request.json()
    p=npakage.creat(data)
    log.logInfo(p)

    response.headers["X-Process-Time"] = str(process_time)

    return response
"""

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


@app.get("/hello")
async def test():
    return "test"









if __name__ == "__main__":

    print("emiya正在启动")

    #print(aPluginsLoader.pls)
    import uvicorn

    # asyncio.run(getFixedMsg())  # 大概是要用creat_grather() 23.9.11
    match flag:
        case 'default':
            cqinit.init()
        case 'mix-console':
            pass
        case 'debug':
            cqinit.DebugMode.debug()
        case _:
            print("Unknown args")

    uvicorn.run("main:app", port=5701, host="0.0.0.0", log_level="warning", workers=2 , reload=True)
