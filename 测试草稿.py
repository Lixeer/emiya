# 开发时间：2023/10/6  21:23
# The road is nothing，the end is all    --Demon


# class Foo:
#     leishux: str = None
#     def __init__(self):
#         print("Foo对象实例化成功")
# class Bar:
#     def __init__(self):
#         print("Bar对象实例化成功")
# class Baz:
#     def __init__(self):
#         print("Baz对象实例化成功")
# # 定义字典，值是字符串与相关的类名对应
# class_dict = {
#     "Foo": "foo",
#     "Bar": "bar",
#     "Baz": "baz"
# }
# value = "foo" # 假设需要实例化 Foo 类的对象
# # 根据字典中的值来实例化对象
# if value in class_dict.values():
#     # 根据值获取对应的类名
#     class_name = [k for k, v in class_dict.items() if v == value][0]
#     # 根据类名动态获取类对象
#     class_obj = globals()[class_name]
#     print(globals())
#     print(class_obj)
#     # 实例化对象
#     instance = class_obj()
# else:
#     print("无法实例化对象，未找到对应的类名")


class A:
    aaa = 000

    def __init__(self, x):
        self.x = x
        print(self.x)




smallFish = {'小黄鱼': 21, '小红鱼': 27, '小蓝鱼': 32, '稀有的小黑鱼': 100}
s = set(smallFish.keys())
print(s)



