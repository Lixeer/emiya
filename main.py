# coding:gbk

import requests
from fastapi import Request, FastAPI

from libs.Logger import Log
from libs.message import MessageInput
from libs.Request import Message

BASEURL = 'http://127.0.0.1:5700'


def sendGroupMsg(gid: int, text: str):
    d = {'message': text,
         'group_id': gid}
    print(requests.post(f'{BASEURL}/send_group_msg', data=d))


def getMsg(id: int):
    d = {'message_id': id}
    return requests.post(f'{BASEURL}/get_msg', data=d)


app = FastAPI()
log = Log()
msg = MessageInput()


@app.post('/')
async def handle(request: Request):
    msg.cheak(await request.json())
    f = Message()
    log.logInfo(f.send_private_msg(2322978154, "ok").text)
    return "data"

@app.get('/hello')
async def test():
    return "test"

if __name__ == '__main__':
    log.logInfo("emiya正在启动")
    import uvicorn

    uvicorn.run(app, port=5701, host='0.0.0.0', log_level="warning")
