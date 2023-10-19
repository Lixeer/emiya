# coding:utf-8

from libs.event.qqevent import onkeyword,oncommand






    



@onkeyword(keywordList=["ping"])
async def handle(n):
    id=n.netpackage.getID()
    rp=await n.callAPI(url="send_group_message",group_id=id,message="pong")
  
    
    

    

    






