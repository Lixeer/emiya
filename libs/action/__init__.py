#coding:utf-8

import fastapi.WebSocket

class Action:
  def __init__(self,websocket:fastapi.WebSocket):
    self.websocket=websocket
    self._sendText=websocket.send_text
  async def callAPI(self,url,**kwargs):
    d={"action":url,
       "params":kwargs
      }
    response = await self.sendText(d)
    return response
   

