from Common.Logger import logger
from testCase.doUITemp import doUITemp


def test_File_Import():
    actualValue, expectValue, title = doUITemp("File Repair", "test_File_Import",
                                               "DocumentRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_Single_File_Remove():
    actualValue, expectValue, title = doUITemp("File Repair", "test_Single_File_Remove",
                                               "DocumentRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


#
def test_All_Files_Remove():
    actualValue, expectValue, title = doUITemp("File Repair", "test_All_Files_Remove",
                                               "DocumentRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_File_Repair():
    actualValue, expectValue, title = doUITemp("File Repair", "test_File_Repair",
                                               "DocumentRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_File_High_Repair_psd():
    actualValue, expectValue, title = doUITemp("File Repair", "test_File_High_Repair_psd",
                                               "DocumentRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


# psb格式高级修复暂时无资源
def test_File_High_Repair_psb():
    actualValue, expectValue, title = doUITemp("File Repair", "test_File_High_Repair_psb",
                                               "DocumentRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_All_File_Export():
    actualValue, expectValue, title = doUITemp("File Repair", "test_All_File_Export",
                                               "DocumentRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")


def test_Single_File_Export():
    actualValue, expectValue, title = doUITemp("File Repair", "test_Single_File_Export",
                                               "DocumentRepairCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")
