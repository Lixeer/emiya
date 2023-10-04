# 开发时间：2023/10/1  15:11
# The road is nothing，the end is all    --Demon

import sys
sys.path.insert(0, sys.path[0]+"/../")

from libs.event.qqevent import onkeyword, oncommand
from libs.db import scoreboard


import requests


BASEURL = "http://127.0.0.1:5700"
def sendGroupMsg(gid: int, text: str):
    d = {"message": text, "group_id": gid}
    requests.post(f"{BASEURL}/send_group_msg", data=d)

@oncommand( promat = [".","/"] , cmd = ["fish"])
def handle(netpackage):

    print('前')
    db = scoreboard.DataStorage()  # 注册实例对象
    db.create('../db/data/beta.db')  # 创建

    print('后')

    # 初始化数据格式
    gameData = {'send_id': None, 'group_id': None,
                'personal_center': {'fishing_level': None, 'wallet_coins': None,
                                    'bank_deposit': None},
                'go_bank': {'wallet_coins': None, ' bank_deposit': None, 'interest': None,
                            'yesterday_earnings': None, 'transfer_limit': None},
                'go_fishing': {'fish': None, 'coins': None, 'experience': None,
                               'fishing_rod': None},
                'exploration_sea': {'this_time_coins': None, 'wallet_coins': None},
                'pirate_raid': {'raidResult': None}
                }

    # if netpackage.user_id in db.find('send_id'):





    # 使用R
    db.open('../db/data/beta.db')
    res = db.find("name")  # 查找
    print("[search result]:", res)
    # del res['name']       # 删除
    db.show(flag=True)  # 查看数据项
    db.change("name", "韩梅梅")
    db.close()

    # 使用 with 语句访问
    with db as d:
        res = db.find("name")  # 查找
        print("[search result]:", res)
        # del res['name']       # 删除
        db.show(flag=True)  # 查看数据项


    # 判断游戏者是否为第一次游戏
    # if netpackage.user_id


    print('该钓鱼了')
    try:
        sendGroupMsg(gid=netpackage.group_id, text="恭喜您获得普通钓竿\n命令：0 钓个鱼")
    except:
        pass

    print("hello emiya")

@oncommand( promat = [".","/"] , cmd = ["ts"])
def handle(netpackage):
    print("command触发")

    try:
        sendGroupMsg(gid=netpackage.group_id,text=f"参数为{netpackage.arg}")
    except:
        pass

# 个人中心类
class PersonalCenter:
    fishingLevel: str = 1  # 钓鱼等级
    walletCoins: int = 0  # 当前钱包余额
    bankDeposit: int = 0  # 银行存款

    def __init__(self):
        pass

    def personalCenter(self):  # 个人中心
        pass

    def goBank(self):  # 去银行
        pass

    def pirateRaid(self):  # 海盗突袭
        pass

    def goFishing(self):  # 去钓鱼
        pass

    def explorationAtSea(self):  # 出海探险
        pass


# 银行类
class GoBank:
    walletCoins: int = 0  # 钱包余额
    bankDeposit: int = 0  # 存款余额
    interest: str = '1%'  # 利息
    yesterdayEarnings: str = '1鱼币（每日利息收入自动发放到钱包余额）'  # 昨天的收益
    transferLimit: str = '50000鱼币/次'  # 转账限额

    def __init__(self):
        pass

    def goBank(self):  # 银行
        pass

    def deposit(self):  # 存款
        pass

    def withdrawalDeposits(self):  # 取存款
        pass

    def transferAccounts(self):  # 转账
        pass

    def goFishing(self):  # 钓鱼
        pass

    def personalCenter(self):  # 个人中心
        pass

    def explorationSea(self):  # 出海探险
        pass

    def pirateRaid(self):  # 海盗突袭
        pass


# 钓鱼类
class GoFishing:
    fish: str = None  # 鱼类
    coins: str = '+0'  # 鱼币
    experience: str = '+8'  # 经验
    fishingRod: str = '普通钓竿'  # 钓竿

    def __init__(self):
        pass

    def goFishing(self):  # 钓鱼
        pass

    def goBank(self):  # 银行
        pass

    def personalCenter(self):  # 个人中心
        pass

    def explorationSea(self):  # 出海探险
        pass

    def pirateRaid(self):  # 海盗突袭
        pass


# 出海探险类
class ExplorationSea:
    thisTimeCoins: str = '+0'  # 本次鱼币变化
    walletCoins: int = 0  # 当前钱包余额

    def __init__(self):
        pass


    def explorationSea(self):  # 出海探险
        pass

    def goFishing(self):  # 钓鱼
        pass

    def goBank(self):  # 银行
        pass

    def personalCenter(self):  # 个人中心
        pass

    def pirateRaid(self):  # 海盗突袭
        pass


# 海盗突袭类
class PirateRaid:
    raidResult: str = None  # 突袭结果

    def __init__(self):
        pass

    def pirateRaid(self):  # 海盗突袭
        pass

    def explorationSea(self):  # 出海探险
        pass

    def goFishing(self):  # 钓鱼
        pass

    def goBank(self):  # 银行
        pass

    def personalCenter(self):  # 个人中心
        pass


# 角色类
class Role(PersonalCenter, GoBank, GoFishing, ExplorationSea, PirateRaid):

    def __init__(self):
        print('创建了一个角色。。')
        super().__init__()

# 通过账号判断游戏者是否第一次游戏






if __name__ == '__main__':
    pass








