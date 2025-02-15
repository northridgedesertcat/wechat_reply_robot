from wxauto import WeChat
import wxcontrol

#用户列表
user_list = ['测试一下']

#使用的模型模式
#local:本地ollama部署
#guigu:硅谷流动在线api
type="local"

#是否告诉对方自己接收到了消息正在思考
# 0为只返回结果
# 1为接收到消息后通知对方等待思考过程
think=0

#Api接口信息
#如果使用硅谷流动的api需要写key
#如果本地，key就给个空
api={
    'key':'',
    "model":"deepseek-r1:1.5b"
}



if __name__=="__main__":
    wx = WeChat()
    wxcontrol.start_respond(wx,user_list,type,think,api)
