# -*- coding:utf-8 -*-
# File: FileRepairPage.py
# Time: 2023/7/31 15:05
# Author: GG Bond


from Page.BasePage import BasePage

class FileRepairPage(BasePage):
    def __init__(self):
        super().__init__()

        # 控件元素
        self.fileRepair = "TabItem7"