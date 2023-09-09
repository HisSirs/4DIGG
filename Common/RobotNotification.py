# -*- coding:utf-8 -*-
# File: RobotNotification.py
# Time: 2023/8/1 11:51
# Author: GG Bond


import json
import os
import time
import zipfile
import requests
from Common.Logger import logger
from Core.PathHandle import REPORT_DIR


def zipfile_(input_file, output_file):
    for root, dirs, files in os.walk(input_file):
        fpath = root.replace(input_file, "")
        _zip = zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED)
        for file in files:
            _zip.write(os.path.join(root, file), os.path.join(fpath, file))
        
        _zip.close()


# 发送文本消息
def send_msg(webhook, msg, header):
    data = {
        "msgtype": "text",
        "text": {
            "content": msg
        }
    }
    
    data = json.dumps(data)
    info = requests.post(url=webhook, data=data, headers=header)
    logger().info(f"文本发送结果: {info.text}")


# 发送文件
def send_file(webhook, file, header):
    # 获取media_id
    key = webhook.split('key=')[1]
    id_url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file"
    files = {"file": open(file, "rb")}
    res = requests.post(url=id_url, files=files)
    media_id = res.json()['media_id']
    
    data = {
        "msgtype": "file",
        "file": {
            "media_id": media_id
        }
    }
    data = json.dumps(data)
    info = requests.post(url=webhook, data=data, headers=header)
    logger().info(f"文件发送结果: {info.text}")


def run():
    # webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=925257ca-7355-4ac9-b4d1-0ff080506841"
    webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6ccf6239-322c-4e02-b58c-7ce9bd2112d0"
    msg = "用例执行完成, 请查收测试报告! "
    headers = {"Content-Type": "text/plain"}
    
    fname = f'测试报告_{time.strftime("%Y-%m-%d", time.localtime())}.zip'
    
    zipfile_(input_file=REPORT_DIR, output_file=os.path.join(REPORT_DIR, fname))
    
    file = os.path.join(REPORT_DIR, fname)
    
    send_msg(webhook, msg, headers)
    send_file(webhook, file, headers)
