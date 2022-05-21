from chat_bot import ChatBot


def main():
    qq = "123456"
    qq_list = [123456]  # 输入要定时发送消息的QQ号
    qq_group_list = [123456, 654321]  # 输入要定时发送消息的QQ群号

    qq_robot = ChatBot(qq, qq_list, qq_group_list)
    while True:
        qq_robot.check()


if __name__ == "__main__":
    main()
