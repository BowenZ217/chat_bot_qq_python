import requests


def find_idioms_cn(word):
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=成语" + word
    r = requests.get(url)
    result = r.json()['content'].replace('{br}', '\n')
    return result
