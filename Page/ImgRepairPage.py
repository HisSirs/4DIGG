# -*- coding:utf-8 -*-
# File: ImgRepairPage.py
# Time: 2023/7/31 15:05
# Author: GG Bond

from Page.BasePage import BasePage

class ImgRepairPage(BasePage):
    def __init__(self):
        super().__init__()

        # 控件元素
        self.imgRepair = "TabItem6"