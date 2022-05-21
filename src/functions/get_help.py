# 等待完善！

# 目录
main_menu = """目录：

翻译
示例：翻译 zh hello, everyone

天气
示例：天气 重庆

计算
示例：计算 2333-1234

成语查询
示例：成语 望子成龙

"""

trans_menu = """格式：翻译 [目标语言的缩写] [句子]

支持语言：
中文(zh)
德语(de)
英语(en)
西班牙语(es)
法语(fr)
意大利语(it)
日语(ja)
荷兰语(nl)
波兰语(pl)
俄语(ru)
"""


def get_menu(keyword):
    if "翻译" in keyword:
        return trans_menu
    else:
        return main_menu
