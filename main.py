# coding:utf-8

import requests
import subprocess
import asyncio
from fastapi import Request, FastAPI

from libs.Logger import Log
from libs.message import MessageInput
from libs.Request import Message

BASEURL = "http://127.0.0.1:5700"


def sendGroupMsg(gid: int, text: str):
    d = {"message": text, "group_id": gid}
    print(requests.post(f"{BASEURL}/send_group_msg", data=d))


def getMsg(id: int):
    d = {"message_id": id}
    return requests.post(f"{BASEURL}/get_msg", data=d)


app = FastAPI()
log = Log()
msg = MessageInput()


@app.post("/")
async def handle(request: Request):
    data = await request.json()
    msg.cheak(data)

    f = Message()

    # 回复测试 23.9.8
    if data["post_type"] == "message":
        if data["message_type"] == "private":
            user_id = data["user_id"]
            message = "[Reprot]: meaasge received."
            res = f.send_private_msg(user_id, message=message)
            if res.status_code == 200:
                log.logDebug(f"[Response]: success")
            else:
                log.logError("[Response]: faild")

    # log.logInfo(f.send_private_msg(2322978154, "ok").text)

    return "data"


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
                process = subprocess.Popen(
                    "go-cqhttp_windows_amd64.exe", stdout=subprocess.DEVNULL
                )
                break
            else:
                print(line)
    except asyncio.CancelledError:
        print("Coroutine cancelled")
        await asyncio.shield(asyncio.sleep(0))
    return -1


async def getFixdMsg():
    print("processing start")
    cq = asyncio.create_task(fixOutput())
    result = await cq
    if result == -1:
        pass
    print("processing end, loding...")


if __name__ == "__main__":
    log.logInfo("emiya正在启动")
    import uvicorn

    asyncio.run(getFixdMsg())

    uvicorn.run(app, port=5701, host="0.0.0.0", log_level="warning")
