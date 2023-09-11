# -*- coding:utf-8 -*-
# File: main.py
# Time: 2023/8/8 17:30
# Author: GG Bond


import sys
import pytest
from Common.Logger import logger
from Core.PathHandle import CONFIG_DIR
from Core.ReadFile import readConfig
from Common.RobotNotification import run


def main():
    # 运行 pytest 命令来生成自定义路径的 HTML 报告
    args = [
        "--report=4DDiG File Repair Report.html",  # 指定报告文件名
        "--title=4DDiG File Repair测试报告",  # 指定报告标题
        "--tester=4DDiG自动化小组成员",  # 指定报告中的测试者
        "--desc=完成4DDiG File Repair Checklist的自动化",  # 指定报告中的项目描述
        "--template=2",  # 指定报告模板样式（1 or 2）
        "-W", "ignore::pytest.PytestWarning"
    ]

    pytest.main(args)


if __name__ == "__main__":
    logger().info(f"python版本: Python{sys.version.split(' ')[0]}")
    logger().info(f"配置文件路径: {CONFIG_DIR}")
    logger().info(f"程序安装路径: {readConfig()['App']['AppPath']}")
    logger().info("***" * 20 + "Start" + "***" * 20)
    main()
    run()
    logger().info("***" * 20 + " End " + "***" * 20)
