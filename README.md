# wechat_reply_robot

功能简介
能够利用windows自动化，模拟人为操作的方式，操控PC的微信。
能够实现监听指定用户，对接在线或者本地的ai，实现微信聊天机器人。

环境要求:
可适配微信3.9，其他版本未测试。

使用教程:
安装依赖:
下载好文件之后，解压出来，运行
pip install -r requirements.txt
一键安装依赖库。

安装完成后点开conf文件。
在conf中进行配置选项
你可以自行利用ollama在本地部署ai模型。
也可以前往硅谷流动去使用在线的api。

结束后登录自己的微信，启动本脚本即可自动化对接ai回复信息。


对接硅基流动api:
去硅谷流动，自行注册账号，选择一个付费或者是免费的模型，在文件中的配置项中写入即可。

对接本地ollama模型：
只需要设置为本地模式，然后写模型即可。


可能出现的问题:
您可以选择监听一个群聊，或者多个用户。
因为开发框架他自身原因，导致你如果同时监听群聊和用户的话，会出现误把历史信息当做新消息回复的情况。

更新日志：
ai模型添加了记忆功能，可以在conf中进行配置最大记忆长度。
ai模型添加了角色模拟功能，能够让ai充当特定的角色进行交流。
