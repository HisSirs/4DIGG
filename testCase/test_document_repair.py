import pytest

from Common.AppStart import closeApp, openApp
from Common.Logger import logger
from testCase.doUITemp import DoUITemp


def setup_function():
    """"""


def teardown_function():
    closeApp()


def test_File_Import():
    actualValue, expectValue, title = DoUITemp("File Repair", "test_File_Import",
                                               "DocumentRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_Single_File_Remove():
    actualValue, expectValue, title = DoUITemp("File Repair", "test_Single_File_Remove",
                                               "DocumentRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_All_Files_Remove():
    actualValue, expectValue, title = DoUITemp("File Repair", "test_All_Files_Remove",
                                               "DocumentRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_File_Repair():
    actualValue, expectValue, title = DoUITemp("File Repair", "test_File_Repair",
                                               "DocumentRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_File_High_Repair_psd():
    actualValue, expectValue, title = DoUITemp("File Repair", "test_File_High_Repair_psd",
                                               "DocumentRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


# psb格式高级修复暂时无资源
@pytest.mark.skip(reason="psb格式高级修复暂时无资源, 跳过运行")
def test_File_High_Repair_psb():
    actualValue, expectValue, title = DoUITemp("File Repair", "test_File_High_Repair",
                                               "DocumentRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_All_File_Export():
    actualValue, expectValue, title = DoUITemp("File Repair", "test_All_File_Export",
                                               "DocumentRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue


def test_Single_File_Export():
    actualValue, expectValue, title = DoUITemp("File Repair", "test_Single_File_Export",
                                               "DocumentRepairCase.json", openApp()).doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")
