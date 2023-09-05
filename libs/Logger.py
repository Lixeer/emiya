
import threading
from datetime import datetime

from libs.singleton import Singleton


class Log(Singleton):
    # 可以是非单例 但是要有全局访问节点 代表状态的属性可以放静态变量里面
    def logInfo(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\033[32m[{now}] [INFO] {message}\033[0m")

    def logWarning(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\033[33m[{now}] [WARNING] {message}\033[0m")

    def logError(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\033[31m[{now}] [ERROR] {message}\033[0m")

    def logDebug(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\033[34m[{now}] [DEBUG] {message}\033[0m")


# 单例Log惰性实现
privatelog = Log()
logInfo = privatelog.logInfo
logWarning = privatelog.logWarning
logError = privatelog.logWarning
logDebug = privatelog.logDebug

