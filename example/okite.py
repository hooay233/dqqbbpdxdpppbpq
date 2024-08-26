from function import *
from datetime import datetime, timedelta

# 假设的固定时间字符串，例如 "06:00:00"
_t = "06:00:00"
# 设为 1 为明天
_tomorrow = 0

# 解析时间字符串
_time = datetime.strptime(_t, "%H:%M:%S").time()
# 记录当前日期和时间
_current_datetime = datetime.now()
# 计算日期
_day = _current_datetime.date() + timedelta(days=_tomorrow)
_day_time = datetime.combine(_day, _time)

_okite_need = True
_okite_number = 0

def when_start():
    send("dqqbbpdxdpppbpq 已启动")
    send("该示例将在相应时间启动叫醒服务")

def when_update():
    global _okite_need, _okite_number
    # 获取当前时间
    current_time = datetime.now()
    # 判断当前时间是否超过
    if current_time > _day_time and _okite_need:
        send("起きて！")
        if _okite_number < 2:
            _okite_number += 1
    elif current_time < _day_time and not _okite_need:
        _okite_need = True



def when_get_message(inner):
    global _okite_need, _okite_number, _tomorrow
    print(_okite_need, _okite_number)
    if _okite_need and _okite_number >= 2:
        send("おはよ！")
        _tomorrow += 1
        _okite_need = False
        _okite_number = 0

def when_stop():
    send("dqqbbpdxdpppbpq 已关闭")
