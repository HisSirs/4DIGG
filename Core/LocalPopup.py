# -*- coding:utf-8 -*-
# File: LocalPopup.py
# Time: 2023/7/31 16:19
# Author: GG Bond


import os
import shutil

import pyautogui
import pyperclip
from Common.Logger import logger
from time import sleep


# 导入弹窗
def localPopup(app, filePath, isMatchFile=False):
    # 将路径添加至剪切板
    pyperclip.copy(filePath)
    # 确定底部的输入框
    app.child_window(title="文件名(N):", auto_id="1148", control_type="ComboBox").child_window(
        title="文件名(N):", auto_id="1148", control_type="Edit").click_input()
    # 输入自定义路径
    pyautogui.hotkey("ctrl", "v")
    # 点击“打开”按钮
    app.child_window(title="打开(O)", auto_id="1", control_type="Button").click_input()

    logger().info(f"文件导入路径: {filePath}")

    app.child_window(auto_id="0", control_type="ListItem").click_input()

    if not isMatchFile:
        # 全选
        pyautogui.hotkey("ctrl", "a")
    # 点击“打开”按钮
    app.child_window(title="打开(O)", auto_id="1", control_type="Button").click_input()


# 导出弹窗
def exportPopup(app, filePath):
    if os.path.exists(filePath):
        shutil.rmtree(filePath)

    try:
        # 路径不能创建时, 直接失败
        os.mkdir(filePath)
        path = filePath.split("\\")

        app.child_window(title="此电脑", control_type="TreeItem").click_input()
        while True:

            app.child_window(title_re=f"(.*)({path[0]})", control_type="TreeItem").click_input()
            for i in range(1, len(path)):
                match path[i]:
                    case "Documents":
                        path[i] = "文档"
                    case "Pictures":
                        path[i] = "图片"
                    case "Downloads":
                        path[i] = "下载"
                    case "Videos":
                        path[i] = "视频"
                    case "Music":
                        path[i] = "音乐"
                try:
                    app.child_window(title=f"{path[i]}", control_type="TreeItem").click_input()
                    sleep(2)

                except:
                    for _ in range(5):
                        pyautogui.press("down")
            break

        app["确定"].click_input()

        return True

    except FileNotFoundError as e:
        logger().error(e)

        return False
