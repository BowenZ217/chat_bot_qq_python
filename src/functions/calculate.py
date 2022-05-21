import requests
import urllib.parse


def calculate(equation):
    temp = urllib.parse.quote(equation)
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=计算" + temp
    r = requests.get(url)
    result = r.json()['content'].replace('{br}', '\n')
    return result
