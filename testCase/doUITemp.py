# -*- coding:utf-8 -*-
# File: doUITemp.py
# Time: 2023/8/29 16:36
# Author: GG Bond

import random

from Common.AppStart import openApp
from Common.Logger import logger
from Core.ImgOcr import importComplete
from Core.LocalPopup import localPopup
from Core.ReadFile import readJson
from Core.SingleFileRemove import singleFileRemove
from Page.BasePage import BasePage


class doUITemp:
    def __init__(self, func, case):
        self.func = func
        self.case = case
        self.UseCases = readJson("VideoRepairCase.json")
        
        # 解析用例中的title, type, expectValue
        self.title = self.UseCases[self.case]["Title"]
        self.expectValue = self.UseCases[self.case]["test_assert"]["Text"]
        if "port" in self.case:
            self.filePath = self.UseCases[self.case]["filePath"]
        
        # 程序启动
        self.app = openApp()
    
    # 根据传入case调用不同的方法
    def doUiTemp(self):
        # 进入到导入文件页面
        match self.func:
            case "Fix Video Errors":
                BasePage(self.app).control_click("Name", "Video Repair")
                BasePage(self.app).control_click("Name", "Fix Video Errors")
            case "Enhance Video Quality":
                BasePage(self.app).control_click("Name", "Video Repair")
                BasePage(self.app).control_click("Name", "Enhance Video Quality")
            case "Colorize Videos":
                BasePage(self.app).control_click("Name", "Video Repair")
                BasePage(self.app).control_click("Name", "Colorize Videos")
            case "Fix Photo Errors":
                BasePage(self.app).control_click("Name", "Photo Repair")
                BasePage(self.app).control_click("Name", "Fix Photo Errors")
            case "Enhance Photo Quality":
                BasePage(self.app).control_click("Name", "Photo Repair")
                BasePage(self.app).control_click("Name", "Enhance Photo Quality")
            case "Colorize Photos":
                BasePage(self.app).control_click("Name", "Photo Repair")
                BasePage(self.app).control_click("Name", "Colorize Photos")
            case "File Repair":
                BasePage(self.app).control_click("Name", "File Repair")
            case "Audio Repair":
                BasePage(self.app).control_click("Name", "Audio Repair")
            case _:
                logger().error("未实现该功能, 请参考其他的功能进行实现")
        
        # 通过用例调用方法
        match self.case:
            case "test_File_Import":
                fileNumber = self.importFile()
                if fileNumber != 0:
                    return "File imported successfully", self.expectValue, self.title
                else:
                    return "File imported failed", self.expectValue, self.title
            
            case "test_Single_File_Remove":
                importNumber, removeNumber = self.singleFileRemove()
                if importNumber == removeNumber:
                    return "File removed successfully", self.expectValue, self.title
                else:
                    return "File removed failed", self.expectValue, self.title
            
            case "test_All_Files_Remove":
                removeNumber = self.singleFileRemove()
                if removeNumber == 0:
                    return "File removed successfully", self.expectValue, self.title
                else:
                    return "File removed failed", self.expectValue, self.title
                
            case "test_File_Repair":
                self.fileRepair()
            case "test_File_High_Repair":
                self.fileHighRepair()
            case "test_File_Preview":
                self.filePreview()
            case "test_All_File_Export":
                self.allFileExport()
            case "test_Single_File_Export":
                self.singleFileExport()
    
    # 文件导入
    def importFile(self):
        # 点击添加文件按钮
        BasePage(self.app).control_click("Name", "Add Video(s)")
        logger().info("1. 打开本地文件导入弹窗")
        # 本地弹窗的处理
        localPopup(self.app, filePath=self.filePath)
        logger().info("2. 文件导入中, 请稍等")
        # 等待导入完成
        importComplete()
        logger().info("3. 文件导入完成")
        # 获取导入成功的文件数量
        text = BasePage(self.app).get_control_title("Name", "Repairing Lists")
        fileNumber = int(text.split("(")[1][:-1])
        logger().info(f"4. 已成功导入{fileNumber}个文件")
        
        return fileNumber
    
    # 单个文件移除
    def singleFileRemove(self):
        # 导入文件
        importNumber = self.importFile()
        logger().info(f"1. 导入{importNumber}个文件")
        # 随机移除任意数量的文件
        removeNum = random.randint(1, importNumber)
        logger().info(f"2. 移除{removeNum}个文件")
        for _ in range(removeNum):
            singleFileRemove()
        # 获取移除之后的数量
        text = BasePage(self.app).get_control_title("Name", "Repairing Lists")
        removeNumber = int(text.split("(")[1][:-1])
        logger().info(f"3. 移除之后剩余{removeNumber}个文件")
        
        return importNumber, removeNumber + removeNum
    
    # 移除所有文件
    def allFileRemove(self):
        # 导入文件
        importNumber = self.importFile()
        logger().info(f"1. 导入{importNumber}个文件")
        # 移除所有文件
        BasePage(self.app).control_click("Name", "Remove All")
        BasePage(self.app).control_click("Name", "Sure")
        logger().info("2. 移除所有的文件")
        # 获取移除之后的文件数量
        text = BasePage(self.app).get_control_title("Name", "Repairing Lists")
        removeNumber = int(text.split("(")[1][:-1])
        logger().info(f"3. 移除之后剩余{removeNumber}个文件")
        
        return removeNumber
        
    # 文件普通修复
    def fileRepair(self):
        # 导入文件
        importNumber = self.importFile()
        logger().info(f"1. 导入{importNumber}个文件")
        # 点击修复按钮
        BasePage(self.app).control_click("Name","Start Repair")
        logger().info("2. 点击修复按钮")
        # 等待修复完成
        
    
    # 文件高级修复
    def fileHighRepair(self):
        pass
    
    # 文件预览
    def filePreview(self):
        pass
    
    # 所有文件导出
    def allFileExport(self):
        pass
    
    # 单个文件导出
    def singleFileExport(self):
        pass
