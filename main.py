import threading
import os
from plyer import notification
import keyboard
import pystray
from PIL import Image
from pystray import MenuItem

from db import init_db, save_key_event


def click_menu(icon, item):
    print("点击了", item)


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


def notify(title, message):
    notification.notify(
        title=title, message=message, app_name='KeyOverWatch', timeout=10,
        app_icon='./resource/kow.ico'
    )


def on_key_pressed(event):
    print(f"按下的键：{event.name}")
    save_key_event(event.name)


if __name__ == '__main__':
    # 初始化数据库
    init_db()

    # 创建托盘线程
    tray_thread = threading.Thread(target=create_menu, daemon=True)
    tray_thread.start()

    print("托盘创建完成，开始监听键盘输入...")
    keyboard.on_press(on_key_pressed)

    # 主线程等待按下 ESC 键
    keyboard.wait()