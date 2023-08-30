# -*- coding:utf-8 -*-
# File: VideoRepairPage.py
# Time: 2023/7/31 12:55
# Author: GG Bond

from Common.AppStart import openApp
from Core.LocalPopup import Popup
from Common.Logger import logger
from Page.BasePage import BasePage
from Core.ImgOcr import importComplete

logger = logger()


class VideoRepairPage(BasePage):
    def fixVideoErrorsAction(self, testCase):
        match testCase:
            case "test_File_Import":
                pass
            case "test_Single_File_Remove":
                pass
            case "test_All_Files_Remove":
                pass
            case "test_File_Repair":
                pass
            case "test_File_High_Repair":
                pass
            case "test_File_Preview":
                pass
            case "test_All_File_Export":
                pass
            case "test_Single_File_Export":
                pass


if __name__ == '__main__':
    app = openApp()

