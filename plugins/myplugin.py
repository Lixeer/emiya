import sys

sys.path.insert(0, sys.path[0] + "/../")
from libs.Request import Message

msg = Message()

normal = " (going well)"

if __name__ == "__main__":
    # msg.send_private_msg(2364082093, "send_private_msg"+normal)
    # msg.send_group_msg(746490988, "send_group_msg"+normal)
    res = msg.get_friend_list(True)
    data = res['data']
    for dic in data:
        print(dic)
