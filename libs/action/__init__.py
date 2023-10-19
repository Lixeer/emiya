#coding:utf-8


class Action:
  def __init__(self,websocket):
    self.websocket=websocket
    self._sendText=websocket.send_text
  async def callAPI(self,url,**kwargs):
    d={"action":url,
       "params":kwargs
      }
    response = await self.sendText(d)
    return response
   

