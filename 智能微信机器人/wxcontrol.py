import chat_ai

def start_respond(wx,user,model,think,api,jole,history_num):
    #初始化创建监听
    send_value=[jole,]
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
                    new_info={"role": "user","content": msg.content}
                    history_sendvalue(send_value,history_num,new_info)
                    if think==1:
                        chat.SendMsg("我已收到您的问题，正在组织语言....")
                    value = chat_with_ai(model,send_value,api['key'],api['model'])
                    chat.SendMsg(value)
                    new_info={"role": "assistant","content": value}
                    history_sendvalue(send_value, history_num, new_info)
                    print("ai发送消息:{value}")


def chat_with_ai(type,send_value,key,model):
    if type=="local":
        result=chat_ai.chat_withit_1_5b(send_value,model)
    elif type=="guigi":
        result=chat_ai.chat_withit_8b(send_value,key,model)
    return result

def history_sendvalue(send_Value,history_num,new_value):
    send_Value.append(new_value)
    if len(send_Value)>=2*history_num+1:
        send_Value.pop(1)
        send_Value.pop(1)




if __name__=="__main__":
    a=1