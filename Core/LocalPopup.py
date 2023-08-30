# -*- coding:utf-8 -*-
# File: LocalPopup.py
# Time: 2023/7/31 16:19
# Author: GG Bond


import os
import pyautogui
import pyperclip
from Common.Logger import logger


# 本地弹窗
def localPopup(app, filePath):
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
    # 全选
    pyautogui.hotkey("ctrl", "a")
    # 点击“打开”按钮
    app.child_window(title="打开(O)", auto_id="1", control_type="Button").click_input()
