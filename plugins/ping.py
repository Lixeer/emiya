# coding:utf-8


from libs.event.qqevent import onmessage
from libs.action import Action
from libs.Logger import logDebug,logInfo

import serial

    



@onmessage()
async def handle(websocket,raw_message,group_id):
    if "ping" in raw_message:
        logDebug(raw_message)
        logDebug(group_id)
        a=Action(websocket)
        rp=await a.callAPI(url="send_group_msg",group_id=group_id,message="pong")


ser = serial.Serial(port="COM7",
                    baudrate=9600,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=1
                    )  # 打开COM17，将波特率配置为115200，其余参数使用默认值
if ser.is_open:  # 判断串口是否成功打开
    logInfo("打开串口成功。")
    logInfo(ser.name)  # 输出串口号
else:
    logInfo("打开串口失败。")
@onmessage()
async def handle(websocket,raw_message,group_id):
    logInfo(raw_message)
    if  raw_message == "/delight":
        ser.write('R1'.encode('utf-8'))
        a=Action(websocket)
        rp=await a.callAPI(url="send_group_msg",group_id=group_id,message="熄灭成功")
    elif raw_message == "/light":
        ser.write('R0'.encode('utf-8'))
        a = Action(websocket)
        rp = await a.callAPI(url="send_group_msg", group_id=group_id, message="点亮成功")
    
    

    

    






