# coding:utf-8

from libs.event.qqevent import onkeyword,oncommand
import requests

BASEURL = "http://127.0.0.1:5700"
def sendGroupMsg(gid: int, text: str):
    d = {"message": text, "group_id": gid}
    requests.post(f"{BASEURL}/send_group_msg", data=d)





             ###############         ################
             # 快快写action!#         # 我有抑郁症.jpg #
             ###############         ################




@onkeyword(keywordList=["ping"])
def handle(netpackage):

    try:
        sendGroupMsg(gid=netpackage.group_id,text="pong")
    except:
        pass

    print("hello emiya")




@oncommand( promat = [".","/"] , cmd = ["ts"])
def handle(netpackage):
    print("command触发")

    try:
        sendGroupMsg(gid=netpackage.group_id,text=f"参数为{netpackage.arg}")
    except:
        pass



