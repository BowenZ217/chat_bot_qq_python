import socket


# 发送消息
def send_msg(resp_dict):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = '127.0.0.1'
    client.connect((ip, 5700))

    msg_type = resp_dict['msg_type']  # 回复类型（群聊/私聊）
    number = resp_dict['number']  # 回复账号（群号/好友号）
    msg = resp_dict['msg']  # 要回复的消息

    # 将字符中的特殊字符进行url编码
    msg = msg.replace(" ", "%20")
    msg = msg.replace("\n", "%0a")

    payload = ""
    if msg_type == 'group':
        payload = "GET /send_group_msg?group_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    elif msg_type == 'private':
        payload = "GET /send_private_msg?user_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    print("发送" + payload)

    client.send(payload.encode("utf-8"))
    client.close()
    return 0


# 关小黑屋
def ban(group_id, user_id, time):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = '127.0.0.1'
    client.connect((ip, 5700))

    payload = "GET /set_group_ban?group_id=" + str(
        group_id) + "&user_id=" + str(user_id) + "&duration=" + str(
        time) + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"

    print("发送" + payload)
    client.send(payload.encode("utf-8"))
    client.close()
    return 0


# 撤回消息
def delete_msg(message_id):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = '127.0.0.1'
    client.connect((ip, 5700))

    payload = "GET /delete_msg?message_id=" + str(
        message_id) + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"

    print("发送" + payload)
    client.send(payload.encode("utf-8"))
    client.close()
    return 0
