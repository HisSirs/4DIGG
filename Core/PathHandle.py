# -*- coding:utf-8 -*-
# File: PathHandle.py
# Time: 2023/8/1 10:30
# Author: GG Bond

import os

BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))  # 获取项目根目录
CORE_DIR = os.path.join(BASE_DIR, 'Core')  # 获取项目core路径
LOG_DIR = os.path.join(BASE_DIR, 'Logs')  # 获取项目logs路径
DATA_DIR = os.path.join(BASE_DIR, 'Data')  # 获取项目Data路径
PAGE_DIR = os.path.join(BASE_DIR, 'Page')  # 获取项目page路径
TEST_CASE_DIR = os.path.join(BASE_DIR, 'testCase')  # 获取测试脚本路径
CONFIG_DIR = os.path.join(BASE_DIR, "config.ini")  # 获取项目Config.ini路径
IMG_DIR = os.path.join(BASE_DIR, "IMG")  # 获取项目IMG路径
COMMON_DIR = os.path.join(BASE_DIR, "Common")  # 获取项目Common路径
REPORT_DIR = os.path.join(BASE_DIR, "Report")  # 获取项目Common路径
FILE_DIR = os.path.join(BASE_DIR, "File")  # 获取项目Common路径

if __name__ == '__main__':
    print(f"项目根目录: {BASE_DIR}")
    print(f"项目core路径: {CORE_DIR}")
    print(f"项目logs路径: {LOG_DIR}")
    print(f"项目Data路径: {DATA_DIR}")
    print(f"项目page路径: {PAGE_DIR}")
    print(f"测试脚本路径: {TEST_CASE_DIR}")
    print(f"项目Config路径: {CONFIG_DIR}")
    print(f"项目IMG路径: {IMG_DIR}")
    print(f"项目Common路径: {COMMON_DIR}")
    print(f"项目Report路径: {REPORT_DIR}")

