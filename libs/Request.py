import abc
import json
import requests
from libs.Logger import Log

log = Log()


class RequestsMessage:
    BASEURL = "http://127.0.0.1:5700/"

    @abc.abstractmethod
    def sendata(self, route: str, data: dict):
        pass
        # url = f'{self.BASEURL+route}'
        # requests.post(url=url, data=data)

    @abc.abstractmethod
    def send(self, route: str):
        pass
        # url = f'{self.BASEURL+route}'
        # requests.post(url=url)

    @abc.abstractmethod
    def get(self, route: str):
        pass
        # url = f'{self.BASEURL+route}'
        # requests.get(url=url)


class Message(RequestsMessage):
    def sendata(self, route: str, data: dict):
        url = f"{self.BASEURL + route}"
        return requests.post(url=url, json=data)

    def send(self, route: str):
        url = f"{self.BASEURL + route}"
        return requests.post(url=url)

    def get(self, route: str):
        url = f"{self.BASEURL + route}"
        return requests.get(url=url)

    def get_friend_list(self):
        """
        响应数据
        user_id	int64	QQ 号
        nickname	string	昵称
        source	string	来源
        """
        return self.send("get_friend_list")

    def getFriendList(self, flag: bool):
        """
        参数
        字段名	数据类型	默认值	说明
        user_id	int64	-	好友 QQ 号
        无响应数据
        """
        res = self.get("get_friend_list")
        data = json.loads(res.text)
        return data

    def delete_friend(self, user_id: int):
        """
        参数
        字段名	数据类型	默认值	说明
        user_id	int64	-	好友 QQ 号
        无响应数据
        """
        data = {"user_id": user_id}
        self.sendata("delete_friend", data=data)

    def get_login_info(self):
        """
        响应数据
        字段名	数据类型	说明
        user_id	int64	QQ 号
        nickname	string	QQ 昵称
        :return: data: dict
        """
        return self.send("get_login_info")

    def send_private_msg(self, user_id: int, group_id: int, message: str):
        """
        参数
        字段名	    数据类型	    默认值	    说明
        user_id	    int64	    -	    对方 QQ 号
        group_id	int64	    -	    主动发起临时会话时的来源群号(可选, 机器人本身必须是管理员/群主)
        message	    message	    -	    要发送的内容
        auto_escape	boolean	    false	消息内容是否作为纯文本发送 ( 即不解析 CQ 码 ) , 只在 message 字段是字符串时有效
        :return:
        字段名	数据类型	说明
        message_id	int32	消息 ID
        """
        data = {
            "user_id": user_id,
            "group_id": group_id,
            "message": message,
            "auto_escape": False,
        }
        return self.sendata("send_private_msg", data)

    def sendPrivateMsg(self, user_id: int, message: str):
        """
        参数
        字段名	    数据类型	    默认值	    说明
        user_id	    int64	    -	    对方 QQ 号
        message	    message	    -	    要发送的内容
        auto_escape	boolean	    false	消息内容是否作为纯文本发送 ( 即不解析 CQ 码 ) , 只在 message 字段是字符串时有效
        :return:
        字段名	数据类型	说明
        message_id	int32	消息 ID
        """
        data = {"user_id": user_id, "message": message, "auto_escape": False}
        return self.sendata("send_private_msg", data)

    def send_group_msg(self, group_id: int, message: str):
        """
        字段名	        数据类型	    默认值	说明
        group_id	    int64	    -	    群号
        message	        message	    -	    要发送的内容
        auto_escape	    boolean	    false	消息内容是否作为纯文本发送 ( 即不解析 CQ 码 ) , 只在 message 字段是字符串时有效
        :param group_id:int
        :param message: str
        :return:
        字段名	    数据类型	   说明
        message_id	int32	消息 ID
        """
        data = {
            "group_id": group_id,
            "message": message,
            "auto_escape": False,
        }
        return self.sendata("send_msg", data)

    def send_msg(self, group_id: int, message: str, message_type="group"):
        """
        字段名	        数据类型	默认值	说明
        message_type	string	-	消息类型, 支持 private、group , 分别对应私聊、群组, 如不传入, 则根据传入的 *_id 参数判断
        # user_id	        int64	-	对方 QQ 号 ( 消息类型为 private 时需要 )
        group_id	    int64	-	群号 ( 消息类型为 group 时需要 )
        message	        message	-	要发送的内容
        auto_escape	    boolean	false	消息内容是否作为纯文本发送 ( 即不解析 CQ 码 ) , 只在 message 字段是字符串时有效
        :return:
        字段名	    数据类型	   说明
        message_id	int32	消息 ID
        """
        data = {
            "message_type": message_type,
            "group_id": group_id,
            "message": message,
            "auto_escape": False,
        }
        return self.sendata("send_msg", data)

    def sendMsg(self, user_id: int, message: str, message_type="private"):
        """
        字段名	        数据类型	默认值	说明
        message_type	string	-	消息类型, 支持 private、group , 分别对应私聊、群组, 如不传入, 则根据传入的 *_id 参数判断
        user_id	        int64	-	对方 QQ 号 ( 消息类型为 private 时需要 )
        # group_id	    int64	-	群号 ( 消息类型为 group 时需要 )
        message	        message	-	要发送的内容
        auto_escape	    boolean	false	消息内容是否作为纯文本发送 ( 即不解析 CQ 码 ) , 只在 message 字段是字符串时有效
        :return:
        字段名	    数据类型	   说明
        message_id	int32	消息 ID
        """
        data = {
            "message_type": message_type,
            "group_id": user_id,
            "message": message,
            "auto_escape": False,
        }
        return self.sendata("send_msg", data)

    def get_msg(self, message_id: int):
        """
        参数
        字段	        类型	    说明
        message_id	int32	消息id
        :param message_id:
        :return:
        响应数据
        字段	            类型	说明
        group	        bool	是否是群消息
        group_id	    int64	是群消息时的群号(否则不存在此字段)
        message_id	    int32	消息id
        real_id	        int32	消息真实id
        message_type	string	群消息时为group, 私聊消息为private
        sender	        object	发送者
        time	        int32	发送时间
        message	        message	消息内容
        raw_message	    message	原始消息内容
        ------------------------------
        其中sender字段包含两个字段:
        字段	        类型	    说明
        nickname	string	发送者昵称
        user_id	    int64	发送者 QQ 号
        """

        data = {"message_id": message_id}
        return self.sendata("get_msg", data)

    def delete_msg(self, message_id: int):
        """
        参数
        字段	        类型	    说明
        message_id	int32	消息id

        :param message_id:
        :return: 无返回值
        """
        data = {"message_id": message_id}
        return self.sendata("delete_msg", data)

    def mark_msg_as_read(self, message_id: int):
        """
        参数
        字段	        类型	    说明
        message_id	int32	消息id

        :param message_id:
        :return: 无返回值
        """
        data = {"message_id": message_id}
        return self.sendata("mark_msg_as_read", data)

    def get_forward_msg(self, message_id: int):
        """
        参数
        字段	        类型	    说明
        message_id	int32	消息id
        :param message_id: string
        :return:
        响应数据
        字段	        类型	                说明
        messages	forward message[]	消息列表
        """
        data = {"message_id": message_id}
        return self.sendata("get_forward_msg", data)

    def send_group_forward_msg(self, group_id: int, messages: dict):
        """
        :param group_id: int
        :param messages: get_forward_msg方法返回的[]
        :return:
        响应数据
        字段名	    数据类型	说明
        message_id	int64	消息 ID
        forward_id	string	转发消息 ID
        """
        data = {"group_id": group_id, "messages": messages}
        return self.sendata("send_group_forward_msg", data)

    def send_private_forward_msg(self, user_id: int, messages: dict):
        """
        :param user_id: int
        :param messages: get_forward_msg方法返回的[]
        :return:
        响应数据
        字段名	    数据类型	说明
        message_id	int64	消息 ID
        forward_id	string	转发消息 ID
        """
        data = {"group_id": user_id, "messages": messages}
        return self.sendata("send_private_forward_msg", data)

    def get_group_msg_history(self, message_seq: int, group_id: int):
        """
        :param message_seq: 起始消息序号, 可通过 get_msg 获得
        :param group_id: 群号
        :return:
        字段	        类型	        说明
        messages	Message[]	从起始序号开始的前19条消息
        """
        data = {"message_seq": message_seq, "group_id": group_id}
        return self.sendata("get_group_msg_history", data)
