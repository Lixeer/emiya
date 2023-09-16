import sys
from typing import Any

sys.path.insert(0, sys.path[0] + "/../")
from libs.Request import Message
from libs.Logger import Log

msg = Message()

normal = " (going well)"


def msgResponseTest(f: Message, log: Log, received: Any) -> None:
    if received["post_type"] == "message":
        userId = received["user_id"]
        if received["message_type"] == "private":
            message = "[Report]: message received."
            res = f.sendPrivateMsg(userId, message=message)
            if res.status_code == 200:
                log.logDebug("[Response]: success")
            else:
                log.logError("[Response]: failed")
        if received["message_type"] == "group":
            if received['message'] == "[CQ:at,qq=3064618662] 小亮，给大家整个活":
                f.send_group_msg(746490988, "草，走，忽略！ጿ ኈ ቼ ዽ ጿ​")


if __name__ == "__main__":
    a = {"name": "小明"}
    b = {"score": [86, 97, 88]}
    for item in b.keys():
        print(b[item])
