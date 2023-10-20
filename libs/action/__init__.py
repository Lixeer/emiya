#coding:utf-8



class Action:
  def __init__(self,websocket):
    self.websocket=websocket
    self._sendText=websocket.send_json
  async def callAPI(self,url,**kwargs):
    d={"action":url,
       "params":kwargs
      }
    
    print(d)
    response = await self._sendText(d)
    return response
   

