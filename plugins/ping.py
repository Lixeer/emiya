# coding:utf-8

from libs.event.qqevent import onkeyword,oncommand
from libs.netpackage.postnetpackage import MessagePackage





    



@onkeyword(keywordList=["ping"])
async def handle(netpackage:MessagePackage):
    id=netpackage.getID()
    rp=await netpackage.actioner.callAPI(url="send_group_message",group_id=id,message="pong")
  
    
    

    

    






