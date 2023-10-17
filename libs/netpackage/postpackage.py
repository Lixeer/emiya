# 开发时间：2023/9/15  21:41
# The road is nothing，the end is all    --Demon




from pydantic import BaseModel

from abc import ABCMeta, abstractmethod

from libs.action import Action
class PostPackageFactory:
    modelList = []

    @classmethod
    def sort(self):  # 冒泡排序
        for i in range(0, len(self.modelList) - 1):
            for j in range(0, len(self.modelList) - 1 - i):
                if self.modelList[j][1] < self.modelList[j+1][1]:
                    self.modelList[j], self.modelList[j+1] = self.modelList[j+1], self.modelList[j]

    def creat(self, request: dict , actioner:Action):
        # 解包逻辑写在这里
        self.sort()
        r = None
        for e in self.modelList:
            try:
                r = e[0](**request,actioner=actioner)
                return r
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


class AbsPostPackage(BaseModel,metaclass=ABCMeta):  # 所有报文字段的公共字段类
    # 抽象报文 子类再实现
    time: int
    self_id: int
    post_type: str
    actioner:Action



    
    





    

class MessagePackage(AbsPostPackage):  # 消息报文的公共字段的类
    message_type: str
    sub_type: str
    user_id: int
    message_id: int
    message: str
    raw_message: str
    font: int


    arg:str=None

    @abstractmethod
    def getID(self)->int:
        #获取上报 id 如果来自群聊就是群号 来自私聊就是发送者q号
        pass

    
    def getMessage(self)->str:
        return self.message

    
    def getMessageID(self)->str:
        return self.message_id

    @abstractmethod
    def getSender(self):
        pass
    



class NoticePackage(AbsPostPackage):  # 通知报文的公共字段的类
    notice_type: str



@registerModel(16)  # 仅用装饰器注册到模型容器中
class MetaPostPackage(AbsPostPackage):  # 心跳数据模型类
    meta_event_type: str
    status: Status
    interval: int
    def __str__(self):
        return f"{self.meta_event_type} | {self.time}"
    # 根据gocqhttp文档封装

@registerModel(9)
class PrivateMessage(MessagePackage):  # 私聊消息
    target_id: int
    sender: PrivateSender
    temp_source: int = None

    def getID(self)->int:
        return self.sender.user_id
        
    def getSender(self)->PrivateSender:
        return self.sender
    
    def __str__(self):
        return f"{self.message_type}({self.getID()}) | {self.sender.nickname}({self.sender.user_id}) : {self.message}"


@registerModel(10)
class GroupMessage(MessagePackage):  # 群消息
    group_id: int
    anonymous: None = None  # 匿名消息字段，未测试，如果没有就是None
    sender: GroupSender
    message_seq: int

    def getID(self)->int:
        return self.group_id
        
    def getSender(self)->GroupSender:
        return self.sender

    def __str__(self):
        return f"{self.message_type}({self.group_id}) | {self.sender.nickname}({self.sender.user_id}) : {self.message}"

@registerModel(11)
class PrivateRevoke(NoticePackage):  # 私聊消息撤回
    user_id: int
    message_id: int

@registerModel(12)
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

@registerModel(14)
class GroupMemberChanges(NoticePackage):  # 群成员变动
    sub_type: str
    group_id: int
    operator_id: int
    user_id: int

@registerModel(13)
class GroupAdministratorChanges(NoticePackage):  # 群管理员变动
    sub_type: str
    group_id: int
    user_id: int

@registerModel(8)
class GroupFileUpload(NoticePackage):  # 群文件上传
    group_id: int
    user_id: int
    file: UploadFile

@registerModel(15)
class GroupTaboo(NoticePackage):  # 群禁言
    sub_type: str
    group_id: int
    operator_id: int
    user_id: int
    duration: int

@registerModel(1)
class AddFriends(NoticePackage):  # 好友添加
    user_id: int

@registerModel(4)
class PrivateStamp(NoticePackage):  # 好友戳一戳，未测试
    sub_type: str
    sender_id: int
    user_id: int
    target_id: int

@registerModel(5)
class GroupStamp(NoticePackage):  # 群内戳一戳，未测试
    sub_type: str
    group_id: int
    user_id: int
    target_id: int

@registerModel(3)
class GroupMemberTitleChange(NoticePackage):  # 群成员头衔变更，未测试
    sub_type: str
    group_id: int
    user_id: int
    title: str

@registerModel(2)
class ReceivingOfflineFiles(NoticePackage):  # 接收到离线文件，未测试
    user_id: int
    file: ReceiveFiles

@registerModel(7)
class OtherEndStatusChanges(NoticePackage):  # 其他客户端在线状态变更
    client: Client
    online: bool

@registerModel(6)
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







