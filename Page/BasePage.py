# -*- coding:utf-8 -*-
# File: BasePage.py
# Time: 2023/7/31 11:50
# Author: GG Bond


import time


class BasePage(object):
    def __init__(self, app):
        self.app = app
    
    # 点击控件
    def control_click(self, method, attr):
        match method:
            case "Name":
                self.app[attr].click_input()
            case "ClassName":
                self.app[attr].click_input()
            case "auto_id":
                self.app.child_window(auto_id=attr, control_type="Button").click_input()
            case "Button":
                self.app.child_window(title=attr, control_type="Button").click_input()
    
    # 获取控件名称
    def get_control_title(self, method, attr):
        match method:
            case "Name":
                return self.app[attr].window_text()
            case "ClassName":
                return self.app[attr].window_text()
            case "window_re":
                return self.app.child_window(title_re=attr, control_type="Text").window_text()
    
    # 画框(调试)
    def draw_outline(self, control):
        while True:
            self.app[control].draw_outline(colour="red", thickness=5)
            time.sleep(3)
            break
    
    # 判断控件是否存在
    def control_exists(self, controls):
        if self.app[controls].exists():
            return True
        else:
            return False
