# -*- coding:utf-8 -*-
# File: test_video_repair.py
# Time: 2023/8/3 19:34
# Author: GG Bond

from Common.Logger import logger
from testCase.doUITemp import doUITemp


def test_File_Import():
    actualValue, expectValue, title = doUITemp("Fix Video Errors", "test_File_Import").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_Single_File_Remove(self):
    actualValue, expectValue, title = self.doUITemp("Fix Video Errors", "test_Single_File_Remove").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


#
def test_All_Files_Remove(self):
    actualValue, expectValue, title = self.doUITemp("Fix Video Errors", "test_All_Files_Remove").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_File_Repair(self):
    actualValue, expectValue, title = self.doUITemp("Fix Video Errors", "test_File_Repair").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_File_High_Repair(self):
    actualValue, expectValue, title = self.doUITemp("Fix Video Errors", "test_File_High_Repair").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_File_Preview(self):
    actualValue, expectValue, title = self.doUITemp("Fix Video Errors", "test_File_Preview").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_All_File_Export(self):
    actualValue, expectValue, title = self.doUITemp("Fix Video Errors", "test_All_File_Export").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_Single_File_Export(self):
    actualValue, expectValue, title = self.doUITemp("Fix Video Errors", "test_Single_File_Export").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")
