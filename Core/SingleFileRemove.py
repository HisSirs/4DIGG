# -*- coding:utf-8 -*-
# File: SingleFileRemove.py
# Time: 2023/8/30 18:24
# Author: GG Bond

import pyautogui


def singleFileRemove():
    # 点击一次不生效, 未找到原因
    addr = pyautogui.getWindowsWithTitle("4DDiG File Repair")[0]
    for _ in range(2):
        pyautogui.click((600 + addr.left), (235 + addr.top))