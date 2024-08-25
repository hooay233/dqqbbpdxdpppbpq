from function import *
from datetime import datetime

# HH:MM:SS 24小时制时间
_t = "06:00:00"  # 示例时间，可以根据实际情况修改

# 将字符串时间转换为datetime对象
_target_time = datetime.strptime(_t, "%H:%M:%S")

_okite = True


def when_start():
    send("dqqbbpdxdpppbpq 已启动")
    send("该示例将在相应时间启动俊达萌闹钟")

def when_update():
    global _okite
    # 获取当前时间
    current_time = datetime.now()
    current_hour, current_minute, current_second = current_time.hour, current_time.minute, current_time.second
    current_time_only = datetime.now().replace(year=1900, month=1, day=1, hour=current_hour, minute=current_minute, second=current_second)
    # 判断当前时间是否超过
    if current_time_only > _target_time and _okite:
        send("起きて！")
    elif current_time_only < _target_time and not _okite:
        _okite = True


def when_get_message(inner):
    global _okite
    if _okite:
        send("おはよう！")
        _okite = False

def when_stop():
    send("dqqbbpdxdpppbpq 已关闭")
