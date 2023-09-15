# 开发时间：2023/9/15  21:41
# The road is nothing，the end is all    --Demon

from pydantic import BaseModel

class PostPackageFactory:
    modelList = []

    @classmethod
    def sort(self):
        pass

    def creat(self, request: dict):
        # 解包逻辑写有右边
        # 伪代码如下
        r = None
        for e in self.modelList:
            try:
                r = e[0](request)
            except:
                pass
        return r

def registerModel(rate: int=1):
    def rg(cls):
        PostPackageFactory.modelList.append((cls,rate))
        return cls
    return rg

class AbsPostPackage(BaseModel):
    # 公共字段写这里
    pass

@registerModel(1)  # 仅用装饰器注册到模型容器中
class MetaPostPackage(AbsPostPackage):
    pass
    # 根据gocqhttp文档封装

@registerModel(1)
class Message(AbsPostPackage):
    pass
    # 根据gocqhttp文档封装



