# dqqbbpdxdpppbpq
 有些 bug 和回答问题时有点问题的基于 xdotool 程序和屏幕画面以及粘贴的残废 QQ 机器人（Disabled QQ Bot Base on Picture of Display & XDotool Program & Paste Plus some Bugs and Problem of Question answering）

> 这个项目的思路清奇，直接通过屏幕内容检测，和 xdotool 模拟鼠标按键操作，来实现 QQ 机器人，因此有一些问题（比如有时会莫名奇妙发两次），请把它当作乐子看待

顾名思义 dqqbbpdxdpppbpq 是一个 QQ 自动回复的框架，
它基于屏幕画面检测和 xdotool 程序，发送消息会调用剪贴板（因为 QQ 输入过快有些字会输入不了，而粘贴却没问题）  

它只在 GNU/Linux 的基于 X11 的桌面环境上测试过，其他操作系统和桌面环境兼容性未知

## 运行
### 🥚准备
先确保你的系统安装有 python3 和 xdotool，如果没有请使用你的系统的包管理器进行安装；
还需要安装 `pillow` 请通过 `pip install pillow` 或 `pip3 install pillow`
以及如果你在启动后要关闭此项目请使用远程控制（如 ssh 一类的软件）在其他设备上向运行该项目的设备的 `./term` 文件中写入任意内容。

### 🐣克隆仓库
现在把这个仓库克隆到本地

### 🐤更改配置
编辑 `./config.py` 文件，将 `x1` 设为检测区域（对方发送新消息出现的位置）的左上角横轴坐标；`y1` 设为检测区域的左上角纵轴坐标；
`x2` 设为检测区域右下角的横轴坐标；`y2` 设为检测区域右下角的纵轴坐标；  
`inputX` 设为输入框位置的横轴坐标；`inputY` 设为输入框位置的纵轴坐标；  
`messageX` 设为对方发出的新消息的位置的横轴坐标；`massageY` 设为对方发出的新消息的位置的纵轴坐标；  
`copyX` 设为右键“对方发出的新消息的位置”出现的复制按钮的位置的横轴坐标；`copyY` 设为右键“对方发出的新消息的位置”出现的复制按钮的位置的纵轴坐标；  
你可以使用 `xdotool getmouselocation` 获得当前鼠标位置。

### 🐔编写功能及启动
编辑 `./action.py` 文件，调用 `send` 函数可以发送内容。`when_start` 函数将会在该项目启动后运行；`when_update` 函数将会在检测屏幕检测区域是否更改前运行；`when_get_message` 函数将在检测区域发生更改时运行，`inner` 参数是对方发送的内容；`when_stop` 函数将在项目关闭后执行。  
默认它启动后会启动一个复读机（如果不修改的话）。  
在运行前先确保 QQ 是启动状态，且检测区域没有被遮挡（建议先用小号测试）  
运行 `./main.py`，然后你将有 10 秒的时间准备，请在这段时间内将焦点移动到 QQ。

