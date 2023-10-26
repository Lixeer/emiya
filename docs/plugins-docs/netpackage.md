<a name="GroupMessage">`GroupMessage`群聊消息</a>
```python
class GroupMessage(MessagePackage):  # 群消息
    message_type: str
    sub_type: str
    user_id: int
    message_id: int
    message: str
    raw_message: str
    font: int

    group_id: int
    anonymous: None = None  # 匿名消息字段，未测试，如果没有就是None
    sender: GroupSender
    message_seq: int

```
- <a href="#GroupSender">GroupSender</a>
___

<a name="PrivateMessage">`PrivateMessage`私聊消息</a>
```python
class PrivateMessage(MessagePackage):  # 私聊消息
    message_type: str
    sub_type: str
    user_id: int
    message_id: int
    message: str
    raw_message: str
    font: int

    target_id: int
    sender: PrivateSender
    temp_source: int = None
```
- <a href="#PrivateSender">PrivateSender</a>
