# # -*- coding:utf-8 -*-
# # File: RobotNotification.py
# # Time: 2023/8/1 11:51
# # Author: GG Bond
#
#
# import json
# import os
# import time
# import zipfile
# import requests
# import shutil
# from Core.PathHandle import LOG_DIR, REPORT_DIR, FILE_DIR
#
#
# def copy_file(input_file,output_file):
#     if not os.path.exists(output_file):
#         os.makedirs(output_file)
#
#     if os.path.exists(input_file):
#         for root, dirs, files in os.walk(input_file):
#             for file in files:
#                 src_file = os.path.join(root, file)
#                 shutil.copy(src_file, output_file)
#
#
# def zipfile_(input_file, output_file):
#     _zip = zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED)
#     for root, dirs, file in os.walk(input_file):
#         fpath = root.replace(input_file, "")
#
#         for fname in file:
#             _zip.write(os.path.join(root, fname), os.path.join(fpath, output_file))
#
#     _zip.close()
#
#
# # 发送文本消息
# def send_msg(webhook, msg, header, mentioned_list=None):
#     data = {
#         "msg type": "text",
#         "text": {
#             "content": msg,
#             "mentioned_list": mentioned_list
#         }
#     }
#
#     data = json.dumps(data)
#
#     info = requests.post(url=webhook, data=data, headers=header)
#
#
# # 发送markdown消息
# def send_md(webhook, content, header):
#     data = {
#
#         "msg type": "markdown",
#         "markdown": {
#             "content": content
#         }
#     }
#     data = json.dumps(data)
#     info = requests.post(url=webhook, data=data, headers=header)
#
#
# # 发送文件
# def send_file(webhook, file, header):
#     # 获取media_id
#     key = webhook.split('key=')[1]
#     id_url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file"
#     files = {"file": open(file, "rb")}
#     res = requests.post(url=id_url, files=files)
#     media_id = res.json()['media_id']
#
#     data = {
#         "msg type": "file",
#         "file": {
#             "media_id": media_id
#         }
#     }
#     data = json.dumps(data)
#     info = requests.post(url=webhook, data=data, headers=header)
#
#
# def run(webhook):
#     msg = "用例已经执行完成, 请查收测试报告! "
#     file = os.path.join(LOG_DIR, time.strftime("%Y-%m-%d", time.localtime()) + ".log")  # 文件路径
#
#
# if __name__ == '__main__':
#
#     # 微信机器人的webhook
#     webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=925257ca-7355-4ac9-b4d1-0ff080506841"
#
#     # mentioned_list = ["@all", ]  # @全体成员
#     # send_msg(webhook, msg=msg, mentioned_list=mentioned_list)
#
#     # passContent = f"# 用例执行结果通知 \n " \
#     #               "用例标题: {} \n " \
#     #               "用例结果: PASS"
#     #
#     # failContent = f"# 用例执行结果通知 \n " \
#     #               "用例标题: {} \n " \
#     #               "用例结果: FAIL"
#
#     # send_md(webhook, content=content)
#
#     # send_file(webhook, file=file)
