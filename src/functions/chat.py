import requests
import urllib.parse
import random


def chat_1(msg):
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + msg
    result = requests.get(url).json()
    if result["result"] == 0:
        return result['content'].replace('{br}', '\n')
    else:
        return "出错了"


def chat_2(msg):
    url = 'https://api.ownthink.com/bot?spoken={}'.format(urllib.parse.quote(msg))
    result = requests.get(url).json()
    if result["message"] == "success":
        return result["data"]['info']['text']
    else:
        return "出错了"


def chat_3(msg):
    key = '35034e960e824195a51f6a9ee0b67996'
    url = 'https://www.tuling123.com/openapi/api?key={}&text={}'.format(key, urllib.parse.quote(msg))
    result = requests.get(url).json()
    if result["code"] == 40002:
        return result["text"]
    else:
        return "出错了"


def chat(message):
    mode = random.randint(1, 3)
    match mode:
        case 1:
            return chat_1(message)
        case 2:
            return chat_2(message)
        case 3:
            return chat_3(message)
        case _:
            return "出错了"
