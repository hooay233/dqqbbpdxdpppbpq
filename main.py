from PIL import ImageGrab
import time
from action import *

print("dqqbbpdxdpppbpq 即将在10秒后启动")
time.sleep(10)

def capture_screen(x1, y1, x2, y2):
    """捕获指定区域的屏幕"""
    return ImageGrab.grab(bbox=(x1, y1, x2, y2))

def has_changed(image1, image2):
    """比较两个图像是否相同"""
    if image1.size != image2.size:
        return True
    for i in range(image1.width):
        for j in range(image1.height):
            if image1.getpixel((i, j)) != image2.getpixel((i, j)):
                return True
    return False


# 第一次捕获屏幕区域
previous_screen = capture_screen(x1, y1, x2, y2)

print("dqqbbpdxdpppbpq 已启动，关闭可使用远程控制电脑向“./term”文件中写入任意内容")
when_start()

f = open("term", "w+")


try:
    while True:
        # 等待一段时间后再次捕获屏幕区域
        when_update()
        time.sleep(0.5)
        current_screen = capture_screen(x1, y1, x2, y2)

        # 检查屏幕区域是否发生变更
        if has_changed(previous_screen, current_screen):
            print("屏幕区域已变更。")
            os.system(f"xdotool mousemove {messageX} {messageY} click 3 sleep 0.05 mousemove {copyX} {copyY} click 1 mousemove {inputX} {inputY}") #copy
            when_get_message(clip.paste())

            time.sleep(0.1)
            previous_screen = capture_screen(x1, y1, x2, y2)
        if f.read():
            break
except KeyboardInterrupt:
    print("关闭")
    when_stop()

print("关闭")
when_stop()

f.write("")
f.close()


