class SingletonMeta(type):
    """
    实现单例模式的元类，可以被继承
    """
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]


class Singleton(metaclass=SingletonMeta):
    """
    单例的基类，继承该类的子类都具有单例模式的特性
    """
    pass

'''
class A(Singleton):
    def __init__(self):
        self.ls=[]

a=A()
a.ls.append(2)

b=A()
print(b.ls)
'''