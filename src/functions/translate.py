import requests

trans_lan_choice = ["zh", "de", "en", "es", "fr", "it", "ja", "nl", "pl", "ru"]


def translate(message):
    target_lang = message[:2]
    api = "1234567890"
    if target_lang in trans_lan_choice:
        message = message[2:]
    else:
        target_lang = "zh"

    url = "https://api.deepl.com/v1/translate?auth_key=" + api + "&text=" + message + "&target_lang=" + target_lang
    r = requests.get(url)
    result = "初始语言：" + r.json()['translations'][0]['detected_source_language'] + \
             "\n结果(" + target_lang + ")：\n" + r.json()['translations'][0]['text']
    return result
