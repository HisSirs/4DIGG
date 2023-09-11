# -*- coding:utf-8 -*-
# File: test_video_repair.py
# Time: 2023/8/3 19:34
# Author: GG Bond

from Common.Logger import logger
from testCase.doUITemp import DoUITemp

from Common.AppStart import openApp


def setup_function():
    """"""


def teardown_function():
    openApp(isClose=True)


def test_File_Import():
    actualValue, expectValue, title = DoUITemp("Fix Video Errors", "test_File_Import",
                                               "VideoRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_Single_File_Remove():
    actualValue, expectValue, title = DoUITemp("Fix Video Errors", "test_Single_File_Remove",
                                               "VideoRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


#
def test_All_Files_Remove():
    actualValue, expectValue, title = DoUITemp("Fix Video Errors", "test_All_Files_Remove",
                                               "VideoRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_File_Repair():
    actualValue, expectValue, title = DoUITemp("Fix Video Errors", "test_File_Repair",
                                               "VideoRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_File_High_Repair():
    actualValue, expectValue, title = DoUITemp("Fix Video Errors", "test_File_High_Repair",
                                               "VideoRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_File_Preview():
    actualValue, expectValue, title = DoUITemp("Fix Video Errors", "test_File_Preview",
                                               "VideoRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_All_File_Export():
    actualValue, expectValue, title = DoUITemp("Fix Video Errors", "test_All_File_Export",
                                               "VideoRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_Single_File_Export():
    actualValue, expectValue, title = DoUITemp("Fix Video Errors", "test_Single_File_Export",
                                               "VideoRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")
