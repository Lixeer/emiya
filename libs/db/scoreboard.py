import ZODB.FileStorage as Fs
from ZODB import DB
import transaction


class DataStorage(object):
    def __init__(self, path):
        self.storage = Fs.FileStorage(path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

    def close(self):
        transaction.commit()
        self.connection.close()
        self.db.close()
        self.storage.close()

    def write(self, data: dict):
        for item in data.keys():
            self.root[item] = data[item]

    def find(self, pred):
        for k in self.root.keys():
            if k == pred:
                return self.root[k]
        print("[ERROR] can't find:", pred)

    def show(self, num: int = None):
        count = 1
        if num > self.root.__len__():
            print("[ERROR] out of range")
        else:
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
    a = {"name": "小明", "score": [86, 97, 88]}
    db = DataStorage('./data/beta.db')  # 创建数据存储
    db.write(a)  # 写入数据
    db.close()  # 关闭

    # 使用
    db = DataStorage('./data/beta.db')
    res = db.find("name")  # 查找
    print("[search result]:", res)
    # del res['name']       # 删除
    db.show(3)  # 查看数据项
    db.close()
