import datetime
import time
import random

from functions.receive import rev_msg
from functions.base_functions import *

from functions.get_pictures_url import *
from functions.daily_message import get_daily_message
from functions.get_help import get_menu
from functions.chat import chat
from functions.translate import translate
from functions.weather import weather
from functions.calculate import calculate
from functions.idioms import find_idioms_cn

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 ' \
             'Safari/537.36 '


# qq机器人
class ChatBot:
    # init
    def __init__(self, qq, qq_list, qq_group_list):
        # qq机器人初始化
        self.qq_robot = eval(qq)
        self.state = False
        self.qq_list = qq_list
        self.qq_group_list = qq_group_list
        self.headers = {
            'user-agent': user_agent,
        }

        # 拉取屏蔽词
        file = open("blocked_words.txt", "r", encoding='utf-8')
        data = file.read()
        self.blocked_words = data.split("\n")
        file.close()

        # 储存：{违规成员: 次数}
        self.ban_list = {0: 0}

        # 记录是否有人刷屏
        self.last_message_id = 0
        self.last_qq = 0
        self.last_qq_count = 0

        # 部分图片初始化
        print("图片初始化中...")
        self.img_list1 = get_img_list_1('女')
        print("图片 —— 1 完成")
        self.img_list2 = None
        self.img_list3 = get_img_list_1('壁纸')
        print("图片 —— 3 完成")
        self.img_list4 = get_img_list_1('男生头像')
        print("图片 —— 4 完成")

        print("初始化完成")

    def check(self):
        # 定时消息
        now = datetime.datetime.now()
        if now.hour == 7 and now.minute == 0:
            daily_message = get_daily_message()
            for qq in self.qq_group_list:
                send_msg({'msg_type': 'group', 'number': qq, 'msg': '各位早安！'})
                send_msg({'msg_type': 'group', 'number': qq, 'msg': daily_message})
            for qq in self.qq_list:
                send_msg({'msg_type': 'private', 'number': qq, 'msg': '早安！'})
            time.sleep(60)
            return
        if now.hour == 22 and now.minute == 0:
            for qq in self.qq_group_list:
                send_msg({'msg_type': 'group', 'number': qq, 'msg': '各位晚安~'})
            for qq in self.qq_list:
                send_msg({'msg_type': 'private', 'number': qq, 'msg': '晚安~'})
            time.sleep(60)
            return

        # 尝试接收消息
        rev = rev_msg()
        print(rev)
        if rev is None:
            return

        # 消息
        if rev["post_type"] == "message":
            # 私聊
            if rev["message_type"] == "private":
                message = rev['raw_message']
                qq = rev['sender']['user_id']

                if 'face' in message:
                    img = rev['raw_message']
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': img})
                elif 'image' in message:
                    img = rev['raw_message']
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': img})
                else:
                    result = chat(message)
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': result})
                    return

            # 群聊
            elif rev["message_type"] == "group":
                message = rev['raw_message']
                group = rev['group_id']
                user_id = rev['sender']['user_id']
                # 检测刷屏
                if user_id == self.last_qq and self.last_message_id != rev['message_id']:
                    self.last_message_id = rev['message_id']
                    self.last_qq_count += 1
                else:
                    self.last_qq_count = 0

                if self.last_qq_count == 10:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '请勿刷屏'})
                    return
                elif self.last_qq_count >= 30:
                    delete_msg(rev['message_id'])
                    return
                elif self.last_qq_count >= 60:
                    ban(rev['group_id'], rev['user_id'], 60)
                    return
                self.last_qq = user_id

                # check if it contains blocked word
                for word in self.blocked_words:
                    if word in rev['raw_message']:
                        # do something
                        message_id = rev['message_id']
                        delete_msg(message_id)

                        not_added = True
                        for key, value in self.ban_list.items():
                            if user_id == key:
                                self.ban_list[key] += 1
                                not_added = False
                                break
                        if not_added:
                            self.ban_list[user_id] = 1
                        # send_msg({'msg_type': 'group', 'number': group, 'msg': '警告第' + str(ban_list[user_id]) + '次~'})
                        if self.ban_list[user_id] > 5:
                            ban(group, user_id, 15 * self.ban_list[user_id])
                        continue

                # functions
                # 检测是否返回使用手册
                if message[:4] == "help":
                    send_msg({'msg_type': 'group', 'number': group, 'msg': get_menu(message[4:])})
                    return
                elif message[:2] == "翻译":
                    result = translate(message[3:])
                    send_msg({'msg_type': 'group', 'number': group, 'msg': result})
                    return
                elif message[:2] == "天气":
                    result = weather(message[3:])
                    send_msg({'msg_type': 'group', 'number': group, 'msg': result})
                    return
                elif message[:2] == "计算":
                    result = calculate(message[3:])
                    send_msg({'msg_type': 'group', 'number': group, 'msg': result})
                    return
                elif message[:2] == "成语":
                    result = find_idioms_cn(message[3:])
                    send_msg({'msg_type': 'group', 'number': group, 'msg': result})
                    return

                # 群聊艾特
                if "[CQ:at,qq={}]".format(self.qq_robot) in rev["raw_message"]:
                    # 提取文本信息
                    temp = rev['raw_message'].split(' ')
                    temp.remove(temp[0])
                    message = " ".join(temp)

                    # do something
                    if '爆照' in temp[0]:
                        url = self.img_list1[random.randint(0, len(self.img_list1))]
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                        return
                    elif '美女' in temp[0]:
                        url = self.img_list1[random.randint(0, len(self.img_list1))]
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                        return
                    elif '照片' in temp[0]:
                        url = self.img_list1[random.randint(0, len(self.img_list1))]
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                        return
                    elif '帅哥' in temp[0]:
                        url = self.img_list4[random.randint(0, len(self.img_list4))]
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                        return
                    elif message == '壁纸':
                        url = self.img_list3[random.randint(0, len(self.img_list3))]
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                        return
                    else:
                        result = chat(message)
                        send_msg({'msg_type': 'group', 'number': group, 'msg': result})
                        return

            # message里结束
            else:
                return

        # 戳一戳
        if rev["post_type"] == "notice":
            if rev['sub_type'] == 'poke' and rev['target_id'] == self.qq_robot and rev['group_id'] is not None:
                group = rev['group_id']
                send_msg({'msg_type': 'group', 'number': group, 'msg': '戳我干嘛！'})
                return
        return

    def run(self):
        self.state = True
        while self.state:
            self.check()
