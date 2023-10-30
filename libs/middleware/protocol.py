#coding:utf-8

from libs.netpackage.postpackage import AbsPostPackage
from libs.singleton import Singleton

class MiddleWareControl():
	class _DefaultMiddleWare:
		def verify(self,netpackage):
			return True
	pluginsMiddleWareMap=dict()
	globaMiddleWare = AbsPostPackage



class _MiddleWare:
  def verify(self,netpackage : AbsPostPackage):
		raise NotApproachmentException()

class GlobalMiddleWare(_MiddleWare,Singleton):
	pass

class PluginMiddleWare(_MiddleWare):
	pass

def globalmiddleware():
	def rg(func):
		
	
