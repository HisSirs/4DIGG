# -*- coding:utf-8 -*-
# File: AppStart.py
# Time: 2023/8/8 20:21
# Author: GG Bond
import os

import psutil
from pywinauto.application import Application
from Core.ReadFile import readConfig


def openApp(isClose=False):

    config = readConfig()

    # 检查进程是否存在
    for pid in psutil.pids():
        if psutil.Process(pid).name() == config["App"]["ProcessName"]:
            os.system(f"taskkill /f /pid {pid}")
        else:
            pass

    if not isClose:
        Application("uia").start(config["App"]["AppPath"])

        # 连接程序, 方便调试
        app_connect = Application("uia").connect(path=config["App"]["AppPath"])

        # 获取窗口对象
        app = app_connect[config["App"]["ProductName"]]
        while app.exists():
            break

        return app


if __name__ == '__main__':
    openApp(True)