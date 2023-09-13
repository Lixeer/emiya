# coding:utf-8
import subprocess
from abc import abstractmethod


class InitWay:
    registeredWay = []

    def __init__(self):
        pass

    @abstractmethod
    def run(self) -> None:
        pass

    @classmethod
    def start(cls):
        for e in cls.registeredWay:
            e.run()


def register(clas):
    """Decorated method, decorate methods in script cq-init"""
    obj = clas()
    InitWay.registeredWay.append(obj)
    return clas


@register
class BatWay(InitWay):
    def run(self):
        # os.system(".\go-cqhttp.bat")
        subprocess.Popen(["cmd", "/K", "go-cqhttp_windows_amd64.exe -D"], creationflags=subprocess.CREATE_NEW_CONSOLE)


class PipeWay(InitWay):
    def run(self) -> None:
        pass

    # 补全管道启动方式(策略)


class DebugMode(InitWay):
    """For main script to debug, you should excuse the cq service
    manually by using this method.

    Attributes: none
    """

    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        pass

    @staticmethod
    def debug():
        print("IN DEBUG MODE")


init = InitWay.start
# print('kkk')
