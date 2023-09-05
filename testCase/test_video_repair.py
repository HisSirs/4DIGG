# -*- coding:utf-8 -*-
# File: test_video_repair.py
# Time: 2023/8/3 19:34
# Author: GG Bond

from Common.Logger import logger
from testCase.doUITemp import doUITemp


def test_File_Import():
    actualValue, expectValue, title = doUITemp("Fix Video Errors", "test_File_Import",
                                               "VideoRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_Single_File_Remove():
    actualValue, expectValue, title = doUITemp("Fix Video Errors", "test_Single_File_Remove",
                                               "VideoRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


#
def test_All_Files_Remove():
    actualValue, expectValue, title = doUITemp("Fix Video Errors", "test_All_Files_Remove",
                                               "VideoRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_File_Repair():
    actualValue, expectValue, title = doUITemp("Fix Video Errors", "test_File_Repair",
                                               "VideoRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_File_High_Repair():
    actualValue, expectValue, title = doUITemp("Fix Video Errors", "test_File_High_Repair",
                                               "VideoRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_File_Preview():
    actualValue, expectValue, title = doUITemp("Fix Video Errors", "test_File_Preview",
                                               "VideoRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_All_File_Export():
    actualValue, expectValue, title = doUITemp("Fix Video Errors", "test_All_File_Export",
                                               "VideoRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_Single_File_Export():
    actualValue, expectValue, title = doUITemp("Fix Video Errors", "test_Single_File_Export",
                                               "VideoRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")
