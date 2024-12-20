import keyboard

from app.db import init_db, save_key_event
from app.ui import init_ui


def click_menu(icon, item):
    print("点击了", item)


def on_key_pressed(event):
    print(f"按下的键：{event.name}")
    save_key_event(event.name)


if __name__ == '__main__':
    # 初始化数据库
    init_db()

    # 初始化 ui
    init_ui()

    print("托盘创建完成，开始监听键盘输入...")
    keyboard.on_press(on_key_pressed)

    # 主线程等待按下 ESC 键

    try:
        keyboard.wait()
    except KeyboardInterrupt:
        pass
