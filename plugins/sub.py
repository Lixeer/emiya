# 开发时间：2023/10/21  21:44
# The road is nothing，the end is all    --Demon

import requests
import re

from libs.event.qqevent import onkeyword,oncommand

# pic_uri = f'https://opengraph.githubassets.com/0/{one}/{two}'


# 项目主页
@onkeyword(keywordList=['github.com','github.com/Lixeer/emiya/issues/','github.com/Lixeer/emiya/commit/'])
async def handle(n):
    new_msg = n.netpackage.message.replace('github.com', 'opengraph.githubassets.com/0')
    CQ_code = f'[CQ:image,file={new_msg}]'
    rp = await n.callAPI(url="send_group_msg",group_id=n.netpackage.getID(),message=CQ_code)




