import requests
import urllib.parse
import random


def chat_1(msg):
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + msg
    r = requests.get(url)
    result = r.json()['content'].replace('{br}', '\n')
    return result


def chat_2(msg):
    url = 'https://api.ownthink.com/bot?spoken={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["data"]['info']['text']


def chat(message):
    mode = random.randint(1, 2)
    match mode:
        case 1:
            return chat_1(message)
        case 2:
            return chat_2(message)
        case _:
            return "出错了"
