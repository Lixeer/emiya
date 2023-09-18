import ZODB.FileStorage as Fs
from ZODB import DB
import transaction
import sys

sys.path.insert(0, sys.path[0] + "/../../")
from libs.singleton import Singleton


class DataStorage(Singleton):
    def __init__(self):
        self.root = None
        self.connection = None
        self.db = None
        self.storage = None
        self.path = ""

    def create(self, path: str):
        self.path = path
        self.storage = Fs.FileStorage(path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()
        self.close()

    def close(self):
        transaction.commit()
        self.connection.close()
        self.db.close()
        self.storage.close()

    def open(self):
        self.storage = Fs.FileStorage(self.path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

    def write(self, data: dict):
        for item in data.keys():
            self.root[item] = data[item]

    def find(self, pred):
        for k in self.root.keys():
            if k == pred:
                return self.root[k]
        print("[ERROR] can't find:", pred)

    def show(self, num: int = 0, flag: bool = False):
        count = 1
        if num > self.root.__len__():
            print("[ERROR] out of range")
        else:
            if flag:
                num = self.root.__len__()
            for k in self.root.keys():
                if count > num:
                    break
                else:
                    count += 1
                print(k + ':', self.root[k])

    def change(self):
        pass


if __name__ == '__main__':
    """scoreboard使用例"""

    # 初始化
    msg = {"name": "小明", "score": [86, 97, 88]}
    db = DataStorage()  # 注册实例对象
    db.create('./data/beta.db')  # 创建
    db.open()  # 开启
    db.write(msg)  # 写入数据
    db.close()  # 关闭

    # 使用
    db.open()
    res = db.find("name")  # 查找
    print("[search result]:", res)
    # del res['name']       # 删除
    db.show(flag=True)  # 查看数据项
    db.close()
