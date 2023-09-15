# coding:utf-8

import time
import requests
import argparse
import subprocess
import asyncio
from fastapi import Request, FastAPI

from libs.Logger import Log
from libs.message import MessageInput
from libs.Request import Message
from libs import cqinit
import plugins.myplugin as plug

BASEURL = "http://127.0.0.1:5700"


def sendGroupMsg(gid: int, text: str):
    d = {"message": text, "group_id": gid}
    print(requests.post(f"{BASEURL}/send_group_msg", data=d))


def getMsg(id: int):
    d = {"message_id": id}
    return requests.post(f"{BASEURL}/get_msg", data=d)


app = FastAPI()
# 使用域内创建

log = Log()
msg = MessageInput()

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

@app.middleware("http")
async def addProcessTimeHeader(request: Request, call_next):
    #日志和适配器请写在中间件
    await setBody(request)
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    data = await request.json()
    if 'message_type' in data:  # 排除心跳包data的干扰
        log.logInfo(f'{data["message_type"]} | {data["sender"]["nickname"]} : {data["message"]}')

    response.headers["X-Process-Time"] = str(process_time)

    return response


@app.post("/")
async def handle(request: Request):
    data = await request.json()
    return "data"  # 去掉这行用cq输出 别用main输出cq信息 23.9.11


@app.get("/hello")
async def test():
    return "test"


async def fixOutput():
    try:
        process = subprocess.Popen(
            "go-cqhttp_windows_amd64.exe", stdout=subprocess.PIPE
        )
        while True:
            line = process.stdout.readline().decode("utf-8").strip()
            if "诊断完成" in line:
                print(line)
                process.kill()
                subprocess.Popen(
                    "go-cqhttp_windows_amd64.exe", stdout=subprocess.DEVNULL
                )
                break
            else:
                print(line)
    except asyncio.CancelledError:
        print("Coroutine cancelled")
        await asyncio.shield(asyncio.sleep(0))
    return -1

async def getFixedMsg():
    print("processing start")
    cq = asyncio.create_task(fixOutput())
    result = await cq
    if result == -1:
        pass
    print("processing end, loading...")


if __name__ == "__main__":
    log.logInfo("emiya正在启动")
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

    uvicorn.run("main:app", port=5701, host="0.0.0.0", log_level="warning", workers=2)
