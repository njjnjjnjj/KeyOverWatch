import os
import threading

import pystray
from PIL import Image
from pystray import MenuItem


def init_ui():
    # 创建托盘线程
    tray_thread = threading.Thread(target=create_menu, daemon=True)
    tray_thread.start()


def on_exit(icon, item):
    print("退出程序")
    icon.stop()  # 停止托盘图标
    os._exit(0)  # 结束整个程序


# 创建菜单
def create_menu():
    # 定义托盘菜单
    menu = (MenuItem(text='退出', action=on_exit),)
    # 加载图标
    image = Image.open("./resource/kow.ico")
    # 创建托盘图标
    icon = pystray.Icon("name", image, "KeyOverWatch\n守护你的健康", menu)
    icon.run()  # 阻塞运行托盘
