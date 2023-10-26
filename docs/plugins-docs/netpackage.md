<a name="GroupMessage">`GroupMessage`</a>
---
```python
class GroupMessage(MessagePackage):  # 群消息
    group_id: int
    anonymous: None = None  # 匿名消息字段，未测试，如果没有就是None
    sender: GroupSender
    message_seq: int

```
