# -*- coding:utf-8 -*-
# File: EmailSend.py
# Time: 2023/8/1 11:51
# Author: GG Bond


import json
import os
import time
import requests

from Core.PathHandle import LOG_DIR


# 发送文本消息
def send_msg(webhook, msg, header, mentioned_list=None):
    data = {
        "msg type": "text",
        "text": {
            "content": msg,
            "mentioned_list": mentioned_list
        }
    }
    
    data = json.dumps(data)
    
    info = requests.post(url=webhook, data=data, headers=header)


# 发送markdown消息
def send_md(webhook, content, header):
    data = {
        
        "msg type": "markdown",
        "markdown": {
            "content": content
        }
    }
    data = json.dumps(data)
    info = requests.post(url=webhook, data=data, headers=header)


# 发送文件
def send_file(webhook, file, header):
    # 获取media_id
    key = webhook.split('key=')[1]
    id_url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file"
    files = {"file": open(file, "rb")}
    res = requests.post(url=id_url, files=files)
    media_id = res.json()['media_id']
    
    data = {
        "msg type": "file",
        "file": {
            "media_id": media_id
        }
    }
    data = json.dumps(data)
    info = requests.post(url=webhook, data=data, headers=header)


if __name__ == '__main__':
    # 微信机器人的webhook
    webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=925257ca-7355-4ac9-b4d1-0ff080506841"
    
    msg = "测试消息通知! "
    mentioned_list = ["@all", ]  # @全体成员
    # send_msg(webhook, msg=msg, mentioned_list=mentioned_list)
    
    passContent = f"# 用例执行结果通知 \n " \
                  "用例标题: {} \n " \
                  "用例结果: PASS"
    
    failContent = f"# 用例执行结果通知 \n " \
                  "用例标题: {} \n " \
                  "用例结果: FAIL"
    
    # send_md(webhook, content=content)
    
    file = os.path.join(LOG_DIR, time.strftime("%Y-%m-%d", time.localtime()) + ".log")  # 文件路径
    # send_file(webhook, file=file)
