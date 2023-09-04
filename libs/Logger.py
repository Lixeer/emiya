import threading
from datetime import datetime

from libs.singleton import Singleton


class Log(Singleton):
    def log_info(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\033[32m[{now}] [INFO] {message}\033[0m")

    def log_warning(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\033[33m[{now}] [WARNING] {message}\033[0m")

    def log_error(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\033[31m[{now}] [ERROR] {message}\033[0m")

    def log_debug(self, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\033[34m[{now}] [DEBUG] {message}\033[0m")
