# coding:utf-8

from libs.evvent,qqevent import onkeyword

@onkeyword(keywordList=["ping"]):
def handle(netpackage):
    print("hello emiya")
