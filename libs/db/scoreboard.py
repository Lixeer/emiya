import ZODB.FileStorage as Fs
from ZODB import DB
import transaction


"""
    usage: python scoreboard.py
    通过 create(path: str) 方法可以在不开启的情况下创建库文件
    通过 open(path: str) 方法打开库文件
    通过 close() 方法关闭库对象
    通过 del 关键字删除键值对，和删除字典中的键值对一样， db.root 是字典根节点
      例: del db.root[‘name']   # 该语句删除db对象根节点上的键为 name 的对象
    
    p.s. 调用过 open 或者 create 或者赋给 db 对象地址的方法之后
      可以通过 with 语句块快速访问
        
"""

class DataStorage():
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

    def __enter__(self):
        self.storage = Fs.FileStorage(self.path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

    def __exit__(self, exc_type, exc_val, exc_tb):
        transaction.commit()
        self.connection.close()
        self.db.close()
        self.storage.close()

    def close(self):
        transaction.commit()
        self.connection.close()
        self.db.close()
        self.storage.close()

    def open(self, path: str):
        self.path = path
        self.storage = Fs.FileStorage(self.path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

    def write(self, data: dict):
        for item in data.keys():
            self.root[item] = data[item]

    def find(self, pred: str):
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

    def change(self, key: str, value):
        self.root[key] = value


if __name__ == '__main__':
    """scoreboard使用例"""

    # 初始化
    msg = {
        "name": "小明",
        "score": [86, 97, 88]
    }
    db = DataStorage()  # 注册实例对象
    # db.create('./data/beta.db')  # 创建
    print(db.path)

    db.open("./data/beta.db")  # 开启
    db.write(msg)  # 写入数据
    db.close()  # 关闭
    #
    # 使用R
    db.open("./data/beta.db")
    res = db.find("name")  # 查找
    print("[search result]:", res)
    # del db.root['name']       # 删除
    db.show(flag=True)  # 查看数据项
    db.change("name", "韩梅梅")
    db.close()
    #
    # 使用 with 语句访问
    with db:
        res = db.find("name")  # 查找
        print("[search result]:", res)
        # del res['name']       # 删除
        db.show(flag=True)  # 查看数据项

    dc = DataStorage()
    dc.open('./data/alpha.db')
    dc.find('name')
    dc.close()

    # 打开过一次就可以通过下面这种形式访问了
    with dc:
        dc.write({'name': 'Hatsune Miku'})
        dc.write({'age': 17})
        dc.write({'email': 'miku@sega.com'})
        dc.show(1)

    with dc:
        dc.show(flag=True)  # 查看全部
