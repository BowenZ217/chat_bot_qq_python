首先从 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp/releases) 下载自己 (系统 / 处理器) 对应版本

## Windows:
1. 将 "go-cqhttp_windows_xxx.exe"拖入src文件夹
2. 双击运行一次，通讯方式选择：  
   0: HTTP通信
3. 生成配置文件: "config.yml"
4. 使用txt修改配置文件：
   1. uin 修改为自己QQ号
   2. 密码（password）可选填，不填则为扫码登录
   3. "allow-temp-session: false" 处改为 true 则允许临时会话消息
   4. 最下方 "http: # HTTP 通信设置" 处修改：  
      "#- url: http://127.0.0.1:5701/ # 地址"   
      改为   
      "- url: http://127.0.0.1:5701/ # 地址"
5. 创建机器人（在main.py中）：
   ```python
    # 示例
    from chat_bot import ChatBot
   
    qq = "123"
    qq_list = [66666]  # 输入要定时发送消息的QQ号
    qq_group_list = [123, 321]  # 输入要定时发送消息的QQ群号

    qq_robot = ChatBot(qq, qq_list, qq_group_list)
   
    qq_robot.run()
    ```
6. 运行
   1. 运行 "go-cqhttp.bat" 或 在代码中添加：
    ```python
    import os
    os.system('start cmd /K "go-cqhttp.exe"')
    ```
   2. 运行 "main.py"
7. 运行期间两个窗口都需保持打开

## MacOs:
1. 双击 "go-cqhttp" (darwin_xxx64)
2. 第一次运行会询问生成配置文件，选择   
   "0: HTTP通信"
3. 生成配置文件: "config.yml"   
    位置："User/用户名/config.yml"
4. 修改处同Windows
5. 创建机器人（在main.py中）：
   ```python
    # 示例
    from chat_bot import ChatBot
   
    qq = "123"
    qq_list = [66666]  # 输入要定时发送消息的QQ号
    qq_group_list = [123, 321]  # 输入要定时发送消息的QQ群号

    qq_robot = ChatBot(qq, qq_list, qq_group_list)
   
    qq_robot.run()
    ```
6. 运行
   1. 双击 "go-cqhttp"
   2. 运行 "main.py"
7. 运行期间两个窗口都需保持打开

