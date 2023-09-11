# coding:utf-8
import os
from abc import ABC,abstractmethod





class InitWay:
	registeredWay=[]
	def __init__(self):
		pass
	@abstractmethod
	def run()->None:
		pass
		
		
		
	@classmethod	
	def start():
		for e in self.registeredWay:
			e.run()



def register(clas):
	obj=clas()
	InitWay.registeredWay.append(obj)
	return clas

@register
class BatWay(InitWay):
	def run():
		os.system("./go-cqhttp.bat")
	
class BatWay(InitWay):
	#补全管道启动方式(策略)
	pass

init=InitWay.start
