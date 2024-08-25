from PIL import Image
import pyperclip as clip
import os
from config import *

def send(*thing):
    os.system(f"xdotool mousemove {inputX} {inputY} click 1")
    for i in thing:
        clip.copy(i)
        os.system("xdotool key Ctrl+v")
    os.system("xdotool key Return")

def img(path):
    return Image.open(path).tobytes()
