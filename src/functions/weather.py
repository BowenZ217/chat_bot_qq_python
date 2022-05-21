import requests


def weather(place):
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=天气" + place.strip()
    r = requests.get(url)
    result = r.json()['content'].replace('{br}', '\n')
    return result
