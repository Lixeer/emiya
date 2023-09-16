import ZODB
import ZODB.FileStorage as fs
from ZODB import DB
import transaction


class DataStorage(object):
    def __init__(self, path):
        self.storage = fs.FileStorage(path)
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
        for key in self.root.keys():
            if key == pred:
                return self.root[key]
        print("can't find:", pred)


if __name__ == '__main__':
    # a = {"name": "小明", "score": [86, 97, 88]}
    # db = DataStorage('./data/beta.db')
    # db.write(a)
    # db.close()

    db = DataStorage('./data/beta.db')
    res = db.find("name")
    print("[search result]:", res)
    root = db.root
    for key in root.keys():
        print(key + ':', root[key])
    db.close()
