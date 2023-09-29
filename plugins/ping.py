# coding:utf-8

from libs.event.qqevent import onkeyword
import requests

BASEURL = "http://127.0.0.1:5700"
def sendGroupMsg(gid: int, text: str):
    d = {"message": text, "group_id": gid}
    print(requests.post(f"{BASEURL}/send_group_msg", data=d))





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


