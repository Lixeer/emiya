
from libs.Logger import Log
from libs.singleton import Singleton


#要改 后面的输出也要改成小写驼峰而不是大驼峰 改完删掉这行主食
log = Log()

"""
定义消息类(上报输出)
"""


class MessageInput(Singleton):
    def info(self, data: dict):  # debug时使用，输出全部data
        if data['post_type'] != 'meta_event':
            log.logInfo(data)

    def infoGroup(self, data: dict):  # group
        log.logInfo(f'{data["message_type"]} | {data["sender"]["nickname"]}:{data["message"]}')

    def infoPrivate(self, data: dict):  # private
        log.logInfo(f'{data["message_type"]} | {data["sender"]["nickname"]}:{data["message"]}')

    def choose(self, data: dict):  # 进行消息分流
        try:
            if data['meta_event_type'] == 'heartbeat':
                pass
        except:
            if data['message_type'] == 'private':
                self.infoPrivate(data)
            elif data['message_type'] == 'group':
                self.infoGroup(data)

    def cheak(self, data: dict):  # data数据传入这个会自动分流
        self.choose(data)
