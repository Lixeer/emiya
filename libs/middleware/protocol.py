#coding:utf-8

from libs.netpackage.postpackage import AbsPostPackage
from libs.singleton import Singleton




class _MiddleWare:
  	async def verify(self,netpackage : AbsPostPackage,wrap)->bool:
	  	pass

class GlobalMiddleWare(_MiddleWare,Singleton):
	pass

class PluginMiddleWare(_MiddleWare):
	pass


		
	
