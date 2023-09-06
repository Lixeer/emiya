from libs.Request import Message as msg


if __name__ == '__main__':
    res = msg.get_group_msg_history(1,746490988)
    print(res)