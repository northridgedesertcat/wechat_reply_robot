import chat_ai

def start_respond(wx,user,model,think,api):
    #初始化创建监听
    for i in user:
        wx.AddListenChat(who=i)
    #循环监听
    while True:
        msgs = wx.GetListenMessage()
        if msgs != {}:
            print("########################################################")
            print(f"获取信息:{msgs}")
            for chat in msgs:
                one_msgs = msgs.get(chat)
            # 回复收到
            for msg in one_msgs:
                print(f"当前信息类型为:{msg.type}")
                if msg.type == 'friend':
                    print(f"对方发送消息:{msg.content}")
                    if think==1:
                        chat.SendMsg("我已收到您的问题，正在组织语言....")
                    value = chat_with_ai(model,msg.content,api['key'],api['model'])
                    chat.SendMsg(value)
                    print("ai发送消息:{value}")


def chat_with_ai(type,value,key,model):
    if type=="local":
        result=chat_ai.chat_withit_1_5b(value,model)
    elif type=="guigu":
        result=chat_ai.chat_withit_8b(value,key,model)
    return result


if __name__=="__main__":
    a=1