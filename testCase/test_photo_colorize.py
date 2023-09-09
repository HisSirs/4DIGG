from Common.Logger import logger
from testCase.doUITemp import doUITemp


def test_File_Import():
    actualValue, expectValue, title = doUITemp("Colorize Photos", "test_File_Import",
                                               "ColorizePhotosCase.json").doUiTemp()
    assert actualValue == expectValue
    logger().info(f"{title} Pass")