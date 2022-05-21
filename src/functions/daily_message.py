import datetime

now = datetime.datetime.now()
date = now.strftime("%x").replace("/", "-")


def get_daily_message():
    message = "今天是：{}".format(date)
    return message
