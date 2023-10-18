#coding:utf-8

import Fastapi.WebSocket

class Action:
  def __init__(self,websocket:Fastapi.WebSocket):
    self.websocket=websocket
    self._sendText=websocket.send_text
  async def callApi(self,url,**kwargs):
    d={"action":url,
       "params":kwargs
      }
    response = await self.sendText(d)
    return response
   

