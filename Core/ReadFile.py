# -*- coding:utf-8 -*-
# File: ReadFile.py
# Time: 2023/8/8 20:14
# Author: GG Bond

import os
import json
import configparser
from Core.PathHandle import BASE_DIR,DATA_DIR


def readConfig():
    # 读取配置文件
    config = configparser.ConfigParser()
    # 获取配置文件路径
    ini_path = os.path.join(BASE_DIR, "config.ini")
    # 获取程序路径
    config.read(ini_path, encoding="utf8")
    return config

def readJson(jsonName):
    jsonPath = os.path.join(DATA_DIR, jsonName)
    with open(jsonPath, "r", encoding="utf8") as fs:
        return json.loads(fs.read())



if __name__ == '__main__':
    AppPath = readConfig()['App']["AppPath"]
    ProductName = readConfig()['App']["ProductName"]
    ProcessName = readConfig()['App']["ProcessName"]
    print(AppPath)
    print(ProductName)
    print(ProcessName)
    print()
    
    case = readJson("VideoRepairCase.json")
    print(case)

