from function import *

def when_start():
    send("dqqbbpdxdpppbpq 已启动")
    send("该示例将重复对方说过的话")

def when_update():
    ...

def when_get_message(inner):
    send(inner) # 当对方发来消息就会自动将对方发的内容重新发一遍

def when_stop():
    send("dqqbbpdxdpppbpq 已关闭")
