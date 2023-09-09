# -*- coding:utf-8 -*-
# File: debug.py
# Time: 2023/9/7 19:35
# Author: GG Bond


from pywinauto.application import Application


app = Application("uia").connect(path=r"C:\Program Files\4DDiG File Repair\4DDiG File Repair.exe")
app = app["4DDiG File Repair"]


app["Repairing Lists"].click_input()