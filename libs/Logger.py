
import threading
from datetime import datetime

from libs.singleton import Singleton


class Log(Singleton):
    # 可以是非单例 但是要有全局访问节点 代表状态的属性可以放静态变量里面
    def logInfo(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] [INFO] {message}")

    def logWarning(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] [WARNING] {message}")

    def logError(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] [ERROR] {message}")

    def logDebug(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] [DEBUG] {message}")


# 单例Log惰性实现
privatelog = Log()
logInfo = privatelog.logInfo
logWarning = privatelog.logWarning
logError = privatelog.logWarning
logDebug = privatelog.logDebug

