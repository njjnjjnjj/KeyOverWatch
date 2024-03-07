from plyer import notification


def notify(title, message):
    notification.notify(
        title=title, message=message, app_name='KeyOverWatch', timeout=10,
        app_icon='./resource/kow.ico'
    )


notify('休息提醒', '已敲击xxx次键盘，休息一下！')
