import Roles

#用户列表
user_list = ['']

#使用的模型模式
#local:本地ollama部署
#guigi:硅基流动在线api
type="guigi"

#是否告诉对方自己接收到了消息正在思考
# 0为只返回结果
# 1为接收到消息后通知对方等待思考过程
think=0

#Api接口信息
#如果使用硅谷流动的api需要写key
#如果本地，key就给个空
api={
    'key':'',
    "model":"deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
}

#ai能够记住的最大历史记录(api接收有限制，所以不能大)
history=5

#对方角色
#可以去Roles中自行按照格式定义
jole=Roles.roles["猫娘"]