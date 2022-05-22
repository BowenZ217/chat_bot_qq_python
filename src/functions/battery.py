import psutil


def report_battery():
    # 获取笔记本当前电池参数
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    if plugged:
        return "正在充电，当前电量：{}%".format(percent)
