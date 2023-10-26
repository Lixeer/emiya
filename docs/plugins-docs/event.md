## 事件-回调🌸
⚽emiya采用观察者模式轮询订阅列表实现回调<br>


流程如下
```
接收数据->轮询事件订阅列表->判断是否符合订阅的事件->执行回调函数(是)
```
而plugins开发者需要做的就是定义回调函数，并加入到订阅列表<s>(看起来很麻烦)</s>

_✨作为一个优雅pythoner✨_
___
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
#导入事件订阅装饰器

@onkeyword(KeywordList=["ping","pong"])
async def handle(aWraper):
    #如果收到的消息包含ping 或 pong 就会触发该回调函数

    message=aWraper.netpackage.getMessage()
    print(message)

```
`aWraper`是一个`包装器(Wraper)`对象<br>
为了不引起歧义，下面将隆重介绍一下介绍一下<br>
首先看看Wraper类的<s>伪</s>代码
```python
class Wraper:
    def __init__(self,actioner,netpackage):
        self.actioner=actioner
        self.callAPI=actioner.callAPI
        self.netpackage=netpackage
```
很清晰的，`Wraper`就是一个集成`action(主动操作)`和`netpackage(上报数据)`的类




### ☘️已实现的事件
---
这里有个表格(占位)
<table border="2" width="400px">
 <tr>
  <th>事件名称</th>
  <th>装饰器</th>
 </tr>
 <tr>
  <td>命令事件</td>
  <td>
   <a href="#oncmmand">
    @oncommand
   </a>
  </td>
 </tr>
 <tr>
  <td>关键词事件</td>
  <td>
   <a href="#onkeyword">
    @onkeyword
   </a>
  </td>
 </tr>
  <tr>
  <td>心跳事件</td>
  <td>
   <a href="#onheartbeat">
    @onheartbeat
   </a>
  </td>
 </tr>
</table>
  
### ☘️开始
___
<a name="onkeyword">`@onkeyword`</a>

```python
def onkeyword(keywordList:Iterable,rate:int=1):
    """
    param:
    keywordList Iterable : 关键词列表
    rate int : 优先级

    return :
    None : 不可做函数调用    
    """
    
```
使用示例(下面的其他装饰将省略使用示例)
```python
from libs.event.qqevent import onkeyword

@onkeyword(keywordList=["ping"])
def handle(n): #函数名和形参可瞎写
    id = n.netpackage.getID()
    n.callAPI(url = "send_msg",
              group_id = id,
              message = "pong"
             )
```
`n.netpackage`下面简称`netpackage`

`netpackage`可能的值为
- <a href="./netpackage.md#GroupMessage">GroupMessage</a>
- <a href="./netpackage.md#PrivateMessage">PrivateMessage</a>
