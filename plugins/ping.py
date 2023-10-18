# coding:utf-8

from libs.event.qqevent import onkeyword,oncommand
from libs.netpackage.postnetpackage import MessagePackage





             ###############         ################
             # 快快写action!#         # 我有抑郁症.jpg #
             ###############         ################




@onkeyword(keywordList=["ping"])
async def handle(netpackage:MessagePackage):
    id=netpackage.getID()
    rp=await netpackage.actioner.callApi(url="send_group_message",group_id=id,message="pong")
  
    
    

    

    






