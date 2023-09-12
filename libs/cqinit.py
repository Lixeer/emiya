# coding:utf-8
import os
import subprocess
from abc import ABC, abstractmethod


class InitWay:
    registeredWay = []

    def __init__(self):
        pass

    @abstractmethod
    def run(self) -> None:
        pass

    @classmethod
    def start(self):
        for e in self.registeredWay:
            e.run()


def register(clas):
    obj = clas()
    InitWay.registeredWay.append(obj)
    return clas


@register
class BatWay(InitWay):
    def run(self):
        # os.system(".\go-cqhttp.bat")
        subprocess.Popen(["cmd","/K","go-cqhttp_windows_amd64.exe -D"],creationflags=subprocess.CREATE_NEW_CONSOLE)


class PWay(InitWay):
    # 补全管道启动方式(策略)
    pass


init = InitWay.start
# print('kkk')
