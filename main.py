from plyer import notification
import keyboard
import pystray
from PIL import Image
from pystray import MenuItem

from db import init_db, save_key_event


def click_menu(icon, item):
    print("点击了", item)


def on_exit(icon, item):
    icon.stop()


# 创建菜单
def create_menu():
    menu = (MenuItem(text='退出', action=on_exit))
    image = Image.open("./resource/kow.ico")
    icon = pystray.Icon("name", image, "KeyOverWatch\n守护你的健康", [menu])
    icon.run()


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
    # TODO: 这里创建托盘并开始做 UI
    # print("开始创建托盘...")
    # create_menu()
    print("开始监听键盘输入...")
    keyboard.on_press(on_key_pressed)
    keyboard.wait('esc')  # 等待按下 ESC 键来退出程序