# coding:gbk

import requests
from fastapi import Request, FastAPI

from libs.Logger import Log
from libs.message import MessageInput

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
    return "data"


if __name__ == '__main__':
    log.log_info("emiya正在启动")
    import uvicorn

    uvicorn.run(app, port=5701, host='0.0.0.0', log_level="warning")
