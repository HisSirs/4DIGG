# -*- coding:utf-8 -*-
# File: Collection.py
# Time: 2023/8/30 18:24
# Author: GG Bond


import os
import pyautogui
import uiautomation
from Common.Logger import logger
from Core.LocalPopup import localPopup
from Page.BasePage import BasePage
from time import sleep
from Core.PathHandle import IMG_DIR



# 等待导入完成
def importComplete(app):
    # sleep会根据单个导入的时间来定
    while True:
        text01 = BasePage(app).get_control_title("window_re", "Repairing Lists(.*)")
        sleep(10)
        text02 = BasePage(app).get_control_title("window_re", "Repairing Lists(.*)")
        if text02 == text01:
            break


def highRepair(app, filePath, num):
    no = 0
    for i in range(int(num)):
        if app["Advanced Repair"]:
            # 点击高级修复按钮
            BasePage(app).control_click("Name", "Advanced Repair")
            sleep(0.5)
            BasePage(app).control_click("Name", "Browse")
            # 添加匹配文件
            localPopup(app=app, filePath=filePath, isMatchFile=True)
            sleep(0.5)
            BasePage(app).control_click("Name", "Start Repair")
            
            logger().info("高级修复中, 请耐心等待")
            sleep(1)
            # 等待高级修修复完成
            waitHighRepairComplete(app)
            sleep(0.5)
            logger().info(f"成功修复{no + 1}个文件")
            sleep(1)
        
        
        app.child_window(auto_id="PART_list", control_type="List").children()[no].click_input()
        no += 1
        pyautogui.press("down")
    
    return True


# 移除单个文件
def singleFileRemove():
    # 点击一次不生效, 未找到原因
    addr = pyautogui.getWindowsWithTitle("4DDiG File Repair")[0]
    sleep(0.1)
    pyautogui.click((600 + addr.left), (235 + addr.top))


# 等待修复完成
def waitRepairComplete(app):
    while True:
        text = BasePage(app).get_control_title("window_re", "Repairing Lists(.*)")
        text = text.split("(")[1][:-1]
        if text == "0":
            break
            
    win = uiautomation.WindowControl(AutomationId="root")
    text = win.TextControl(AutomationId="text").Name
    
    if "successfully." in text:
        success = text.split(" ")[0]
        false = 0
    
    elif "successfully," in text:
        success = text.split(" ")[0]
        false = text.split(",")[1].split(" ")[0]
        logger().info(f"{success}个文件修复成功, {false}个文件修复失败")
    
    else:
        success = 0
        false = text.split(' ')[0]
        
    logger().info(f"{success}个文件修复成功, {false}个文件修复失败")
    
    BasePage(app).control_click("Name", "View Results")
    
    return false, success


# 等待高级修复完成
def waitHighRepairComplete(app):
    while app["Advanced Repair Complete"].exists():
        sleep(1)
        BasePage(app).control_click("Name", "OK")
        
        break


# 等待导出完成
def waitExportComplete(app, isSingleExport=False):
    path = os.path.join(IMG_DIR, "Complete.png")
    while True:
        if pyautogui.locateOnScreen(path):
            break
    if not isSingleExport:
        text = BasePage(app).get_control_title("window_re", "(.*)files exported! You can check them in File Manager.")
        result = int(text.split(" ")[0])
    else:
        result = 1
    sleep(2)
    BasePage(app).control_click("Name", "View Results")
    sleep(2)
    pyautogui.hotkey("Alt", "F4")

    return result
