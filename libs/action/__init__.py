#coding:utf-8

from fastapi import WebSocket

class Action:
  def __init__(self,websocket:WebSocket):
    self.websocket=websocket
    self._sendText=websocket.send_text
  async def callApi(url,parmams):
    d={"action":url,
       "params":params
      }
    response = await self.sendText(d)
    return response
   

