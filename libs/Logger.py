
import threading
from datetime import datetime

from libs.singleton import Singleton

import os
import sys

os.system("")
# 本程序依靠此bug运行，勿删[/doge]

def getCall():
  try:
    fileName = sys._getframe(2).f_code.co_filename
  except:
    return "?"
  callName = ""
  fileNameList = fileName.replace(os.getcwd(), "").replace("\\", "/").lstrip("/").split("/")
  if fileNameList[-1][-3:] == ".py":
    fileNameList[-1] = fileNameList[-1][0:-3]
  for i in fileNameList:
    callName = callName + "." + i
  if callName[-8:] == "__init__":
    callName = callName[0:-9]
  callName = callName[1:]
  return callName

class Log(Singleton):
    # 可以是非单例 但是要有全局访问节点 代表状态的属性可以放静态变量里面
    def logInfo(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        call = getCall()
        print(f"[\033[40;36m{now}\033[0m] [\033[40;32mINFO\033[0m] \033[40;36;4m{call}\033[0m \033[40;32m{message}\033[0m")

    def logWarning(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        call = getCall()
        print(f"[\033[40;36m{now}\033[0m] [\033[40;33mWARNING\033[0m] \033[40;36;4m{call}\033[0m \033[40;33m{message}\033[0m")

    def logError(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        call = getCall()
        print(f"[\033[40;36m{now}\033[0m] [\033[40;31mERROR\033[0m] \033[40;36;4m{call}\033[0m \033[40;31m{message}\033[0m")

    def logDebug(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        call = getCall()
        print(f"[\033[40;36m{now}\033[0m] [\033[40;37mDEBUG\033[0m] \033[40;36;4m{call}\033[0m  \033[40;37m{message}\033[0m")


# 单例Log惰性实现
privatelog = Log()
logInfo = privatelog.logInfo
logWarning = privatelog.logWarning
logError = privatelog.logWarning
logDebug = privatelog.logDebug

