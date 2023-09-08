# coding:utf-8

import requests
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


if __name__ == "__main__":
    log.logInfo("emiya正在启动")
    import uvicorn

    uvicorn.run(app, port=5701, host="0.0.0.0", log_level="warning")
