# 开发时间：2023/9/15  21:41
# The road is nothing，the end is all    --Demon

from pydantic import BaseModel

class PostPackageFactory:
    modelList = []

    @classmethod
    def sort(self):
        pass

    def creat(self, request: dict):
        # 解包逻辑写在这里

        # 伪代码如下
        r = None
        for e in self.modelList:
            try:
                r = e[0](**request)
            except:
                pass
                # print(f'=================================={e[0]}数据模型类出错')
        return r

def registerModel(rate: int=1):
    def rg(cls):
        PostPackageFactory.modelList.append((cls, rate))
        return cls
    return rg

class PrivateSender(BaseModel):  # PrivateMessage类中的sender字段的类
    age: int
    nickname: str
    sex: str
    user_id: int

class GroupSender(BaseModel):  # GroupMessage类的sender字段的类
    age: int
    area: str
    card: str
    level: str
    nickname: str
    role: str
    sex: str
    title: str
    user_id: int

class Stat(BaseModel):  # Status类中的stat字段的类
    packet_received: int
    packet_sent: int
    packet_lost: int
    message_received: int
    message_sent: int
    disconnect_times: int
    lost_times: int
    last_message_time: int

class Status(BaseModel):  # MetaPostPackage类中的status字段的类
    app_enabled: bool
    app_good: bool
    app_initialized: bool
    good: bool
    online: bool
    plugins_good: None
    stat: Stat

class UploadFile(BaseModel):  # GroupFileUpload类的file字段的类
    id: str
    name: str
    size: int
    busid: int
    url: str

class ReceiveFiles(BaseModel):  #  ReceivingOfflineFiles类的file字段的类
    name: str
    size: int
    url: str

class Client(BaseModel):  # OtherEndStatusChanges类的client字段的类
    app_id: int
    device_kind: str
    device_name: str


class AbsPostPackage(BaseModel):  # 所有报文字段的公共字段类
    # 公共字段写这里
    time: int
    self_id: int
    post_type: str
    # pass

class MessagePackage(AbsPostPackage):  # 消息报文的公共字段的类
    message_type: str
    sub_type: str
    user_id: int
    message_id: int
    message: str
    raw_message: str
    font: int



class NoticePackage(AbsPostPackage):  # 通知报文的公共字段的类
    notice_type: str



@registerModel(1)  # 仅用装饰器注册到模型容器中
class MetaPostPackage(AbsPostPackage):  # 心跳数据模型类
    meta_event_type: str
    status: Status
    interval: int
    # 根据gocqhttp文档封装

@registerModel(1)
class PrivateMessage(MessagePackage):  # 私有消息
    target_id: int
    sender: PrivateSender
    temp_source: int = None

@registerModel(1)
class GroupMessage(MessagePackage):  # 群消息
    group_id: int
    anonymous: None = None  # 匿名消息字段，未测试，如果没有就是None
    sender: GroupSender
    message_seq: int

@registerModel(1)
class PrivateRevoke(NoticePackage):  # 私聊消息撤回
    user_id: int
    message_id: int

@registerModel(1)
class GroupRevoke(NoticePackage):  # 群消息撤回
    group_id: int
    user_id: int
    operator_id: int
    message_id: int

# @registerModel(1)
# class GroupMemberIncrease(NoticePackage):  # 群成员增加
#     sub_type: str
#     group_id: int
#     operator_id: int
#     user_id: int

@registerModel(1)
class GroupMemberChanges(NoticePackage):  # 群成员变动
    sub_type: str
    group_id: int
    operator_id: int
    user_id: int

# @registerModel(1)
class GroupAdministratorChanges(NoticePackage):  # 群管理员变动
    sub_type: str
    group_id: int
    user_id: int

@registerModel(1)
class GroupFileUpload(NoticePackage):  # 群文件上传
    group_id: int
    user_id: int
    file: UploadFile

@registerModel(1)
class GroupTaboo(NoticePackage):  # 群禁言
    sub_type: str
    group_id: int
    operator_id: int
    user_id: int
    duration: int

# @registerModel(1)
class AddFriends(NoticePackage):  # 好友添加
    user_id: int


@registerModel(1)
class PrivateStamp(NoticePackage):  # 好友戳一戳，未测试
    sub_type: str
    sender_id: int
    user_id: int
    target_id: int

@registerModel(1)
class GroupStamp(NoticePackage):  # 群内戳一戳，未测试
    sub_type: str
    group_id: int
    user_id: int
    target_id: int

@registerModel(1)
class GroupMemberTitleChange(NoticePackage):  # 群成员头衔变更，未测试
    sub_type: str
    group_id: int
    user_id: int
    title: str

@registerModel(1)
class ReceivingOfflineFiles(NoticePackage):  # 接收到离线文件，未测试
    user_id: int
    file: ReceiveFiles

@registerModel(1)
class OtherEndStatusChanges(NoticePackage):  # 其他客户端在线状态变更
    client: Client
    online: bool

@registerModel(1)
class EssenceMessageChange(NoticePackage):  # 精华消息变更，未测试
    sub_type: str
    group_id: int
    sender_id: int
    operator_id: int
    message_id: int
#
# @registerModel(1)
# class MessageSent(AbsPostPackage):
#     pass







