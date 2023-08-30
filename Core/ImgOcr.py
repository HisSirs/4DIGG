# -*- coding:utf-8 -*-
# File: ImgOcr.py
# Time: 2023/8/19 9:04
# Author: GG Bond

import os
import pyautogui
from Core.PathHandle import IMG_DIR
from time import sleep

def importComplete():
    imgPath = os.path.join(IMG_DIR, "Button.png")
    sleep(2)
    while True:
        if pyautogui.locateOnScreen(imgPath):
            break


def highRepairBtnLocal():
    imgPath = os.path.join(IMG_DIR, "RepairButton.png")
    a = pyautogui.locateAllOnScreen(imgPath)
    print(a)
    for i in a:
        print(i)


if __name__ == '__main__':
    importComplete()
    highRepairBtnLocal()