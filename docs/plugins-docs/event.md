## 事件-回调🌸
⚽emiya采用观察者模式轮询订阅列表实现回调<br>


流程如下

```
接收数据->轮询事件订阅列表->判断是否符合订阅的事件->执行回调函数(是)
```
而plugins开发者需要做的就是定义回调函数，并加入到订阅列表<s>(看起来很麻烦)</s>

_✨作为一个优雅pythoner✨_

### ☘️一个示例
```python
#coding:utf-8
"""
path
plugins/demo.py
or
plugins/demo/__init__.py
"""
from libs.event.qqevent import onkeyword

@onkeyword(KeywordList=["ping"])
def handle(n):

    message=n.netpackage.getMessage()
    print(message)

```

### ☘️已实现的事件
---
这里有个表格(占位)
