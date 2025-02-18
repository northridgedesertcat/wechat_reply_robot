from openai import OpenAI
import requests
import json


#1.5b
def chat_withit_1_5b(values,model):
    #对接deepseek，返回内容
    client = OpenAI(
        base_url='http://127.0.0.1:11434/v1/',
        # required but ignored
        api_key='ollama',
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': values,
            }
        ],
        model=model,
    )
    result=info_control(chat_completion.choices[0].message.content)
    return result

def info_control(value):
    #去除思考过程，仅保留结果
    list=value.split("</think>")
    list=list[1:]
    print(list)
    result="".join(list)
    result = result.lstrip("\n")
    return result




###########################################################################################################################
#8b



def chat_withit_8b(send_value,key,guigi_model):
    url = "https://api.siliconflow.cn/v1/chat/completions"
    payload = {
        "model": guigi_model,
        "messages": send_value,
        "stream": False,
        "max_tokens": 512,
        "stop": ["null"],
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "response_format": {"type": "text"},
    }
    headers = {
        "Authorization": "Bearer {}".format(key),
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    assistant_content=analysis_content(response)
    if assistant_content=="":
        assistant_content="服务器繁忙，请稍后重试！"
    return assistant_content

def analysis_content(response):
    #解析返回内容
    print(f"接收到在线模型消息:{response.text}")
    data = json.loads(response.text)
    choices = data['choices']
    assistant_content = choices[0]['message']['content']
    print(assistant_content)
    return assistant_content



if __name__=="__main__":
    a=1
