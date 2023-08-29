#coding:gbk
from flask import  Flask,request

import requests
BASEURL="http://127.0.0.1:5700"
r=requests.get(url="http://127.0.0.1:5700/get_login_info")
print(r.json())

def sendGroupMsg(gid:int,text:str):
	print("进入2")
	d={"message":text,
	   "group_id":gid}
	print(requests.post(f"{BASEURL}/send_group_msg",data=d))
	
	
def getMsg(id:int):
	d={"message_id":id}
	return requests.post(f"{BASEURL}/get_msg",data=d)

app=Flask(__name__)         

@app.route('/',methods=['POST'])
def handle():
	#print(request.json)
	if request.json["post_type"]=="meta_event":
		return "a"
	msgid=request.json["message_id"]
	print("msgid=",msgid)
	
	msg=getMsg(msgid).json()
	msgtext=msg["data"]["message"]
	
	print("msg=",msg)
	if msgtext=="原神":
		print("进入")
		gid=msg["data"]["group_id"]
		sendGroupMsg(gid=gid,text="启动尼玛b")
		
	return "ts"
	
if __name__=="__main__":
    app.run(port=5701,host="0.0.0.0",debug=True)
