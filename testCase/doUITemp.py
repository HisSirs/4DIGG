# -*- coding:utf-8 -*-
# File: doUITemp.py
# Time: 2023/8/29 16:36
# Author: GG Bond

import os
import random
import time
from Common.Logger import logger
from Core.Collection import singleFileRemove, waitRepairComplete, waitExportComplete, highRepair, importComplete
from Core.LocalPopup import localPopup, exportPopup
from Core.ReadFile import readJson
from Page.BasePage import BasePage


class DoUITemp:
    def __init__(self, func, case, CaseFile, app):
        self.func = func
        self.case = case
        self.app = app
        self.UseCases = readJson(CaseFile)

        # 解析用例中的title, type, expectValue
        self.title = self.UseCases[self.case]["Title"]
        self.expectValue = self.UseCases[self.case]["test_assert"]["Text"]
        self.importFilePath = self.UseCases[self.case]["importFilePath"]
        if "High" in self.case:
            self.highRepairPath = self.UseCases[self.case]["highRepairPath"]
        if "Export" in self.case:
            self.exportFilePath = self.UseCases[self.case]["exportFilePath"]

    def result(self, flag, action):
        return f"File {action} Successfully", self.expectValue, self.title if flag else f"File {action} Failed", self.expectValue, self.title

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
                flag = self.importFile()
                return self.result(flag, "Import")

            case "test_Single_File_Remove":
                flag = self.singleFileRemove()
                return self.result(flag, "Remove")

            case "test_All_Files_Remove":
                flag = self.allFileRemove()
                return self.result(flag, "Remove")

            case "test_File_Repair":
                flag = self.fileRepair()
                return self.result(flag, "Repair")

            case "test_File_Preview":
                flag = self.filePreview()
                return self.result(flag, "Preview")

            case "test_All_File_Export":
                flag = self.allFileExport()
                return self.result(flag, "Export")

            case "test_Single_File_Export":
                flag = self.singleFileExport()
                return self.result(flag, "Export")

            # 高级修复的匹配文件需要对应格式,若要支持多用例, 只能用通配符匹配, 其他用例名不能有错
            case _:
                flag = self.fileHighRepair()
                return self.result(flag, "Repair")

    # 文件导入
    def importFile(self):
        """
        导入功能, 由于是导入全部文件, 所以只看修复列表中有无文件, 有文件则就算导入成功
        """
        # 点击添加文件按钮
        BasePage(self.app).control_click("Name", "Add Video(s)")
        logger().info("打开本地文件导入弹窗")

        # 本地弹窗的处理
        localPopup(self.app, filePath=self.importFilePath)
        logger().info("文件导入中, 请耐心等待")

        # 等待导入完成
        importComplete(self.app)
        # 获取导入成功的文件数量
        if "Fix" in self.func or "Repair" in self.func:
            text = BasePage(self.app).get_control_title("Name", "Repairing Lists")

        elif "Colorize" in self.func:
            text = BasePage(self.app).get_control_title("Name", "Items to Colorize")

        elif "Enhance" in self.func:
            text = BasePage(self.app).get_control_title("Name", "Pending Items")

        else:
            text = None

        fileNumber = int(text.split("(")[1][:-1])
        logger().info(f"文件导入完成, 已成功导入{fileNumber}个文件")

        return fileNumber if fileNumber != 0 else False

    # 单个文件移除
    def singleFileRemove(self):
        """
        单个文件移除功能, 导入多少个文件, 就全部进行移除, 修复列表中的文件数为0, 则表示移除成功
        """
        # 导入文件
        importNumber = self.importFile()

        # 随机移除任意数量的文件, 移除最大数量为最大值-1
        if importNumber != 1:
            removeNum = random.randint(1, importNumber - 1)
        else:
            removeNum = 1
        logger().info(f"随机移除{removeNum}个文件, 请耐心等待")
        # 第一次点击无效, 需要多点击一次
        singleFileRemove(self.func)
        for _ in range(removeNum):
            singleFileRemove(self.func)

        # 获取移除之后的数量
        text = BasePage(self.app).get_control_title("Name", "Repairing Lists")
        removeNumber = int(text.split("(")[1][:-1])
        logger().info(f"移除之后剩余{removeNumber}个文件")

        return True if importNumber == removeNumber + removeNum else False

    # 移除所有文件
    def allFileRemove(self):
        """
         所有文件移除功能, 移除一次, 修复列表中的文件数为0, 则表示移除成功
        """
        # 导入文件
        self.importFile()

        # 移除所有文件
        BasePage(self.app).control_click("Name", "Remove All")
        BasePage(self.app).control_click("Name", "Sure")
        logger().info("移除所有的文件")

        # 获取移除之后的文件数量
        text = BasePage(self.app).get_control_title("Name", "Repairing Lists")
        removeNumber = int(text.split("(")[1][:-1])
        logger().info(f"移除之后剩余{removeNumber}个文件")

        return True if removeNumber == 0 else False

    # 文件普通修复
    def fileRepair(self):
        """
        文件普通修复功能, 导入均是无损坏的文件, 正常修复, 修复成功的数量与导入数量一致就算成功
        """
        # 导入文件
        importNumber = self.importFile()

        # 点击修复按钮
        BasePage(self.app).control_click("Name", "Start Repair")
        logger().info("修复中, 请耐心等待")

        # 等待修复完成，正常情况是都额能修复成功
        _, successNum = waitRepairComplete(self.app)
        return True if importNumber == int(successNum) else False

    # 文件高级修复
    def fileHighRepair(self):
        """
        文件普通修复功能, 导入均是损坏的文件, 正常修复后, 在进行高级修复, 修复成功的数量与导入数量一致就算成功
        """
        # 导入文件
        self.importFile()

        # 点击修复按钮
        BasePage(self.app).control_click("Name", "Start Repair")
        logger().info("修复中, 请耐心等待")

        # 等待修高级复完成
        failNum, successNum = waitRepairComplete(self.app)

        # 高级修复功能
        return True if highRepair(self.app, self.highRepairPath, failNum) else False

    # 文件预览
    def filePreview(self):
        """
        文件预览功能, 随机播放几秒, 对比播放时长, 一致就算通过
        """
        # 导入文件
        self.importFile()

        # 点击修复按钮
        BasePage(self.app).control_click("Name", "Start Repair")
        logger().info("修复中, 请耐心等待")

        # 等待修复完成
        _, successNum = waitRepairComplete(self.app)

        # 点击播放按钮, 播放时长用time.sleep()控制

        BasePage(self.app).control_click("auto_id", "playTB")
        logger().info("正在播放")
        time.sleep(3)
        BasePage(self.app).control_click("auto_id", "playTB")

        # 获取当前播放进度, 只要不是00:00:00就算正确
        try:
            if BasePage(self.app).get_control_title("window_re", "00:00:00"):
                return True
        except:
            return False

    # 所有文件导出
    def allFileExport(self):
        """
        所有文件导出功能, 对比导出成功的文件数/导出路径下的文件数和导入文件数, 一致就算成功
        """
        # 导入文件
        importNumber = self.importFile()

        # 点击修复按钮
        BasePage(self.app).control_click("Name", "Start Repair")
        logger().info("修复中, 请耐心等待")

        # 等待修复完成
        _, successNum = waitRepairComplete(self.app)

        # 点击全选和导出
        BasePage(self.app).control_click("Name", "Select All")
        time.sleep(0.5)
        BasePage(self.app).control_click("Name", "Export Selected")

        # 根据导出路径选择文件夹, 路径不能创建成功则直接失败
        if exportPopup(self.app, self.exportFilePath):
            # 等待导出完成
            result = waitExportComplete(self.app)

            # 获取导出路径下的文件数
            for root, dirs, file in os.walk(self.exportFilePath):
                if len(file) == importNumber and importNumber == result:
                    logger().info(f"成功导出{len(file)}个文件")

                    return True
                return False
        else:
            return False

    # 单个文件导出
    def singleFileExport(self):
        """
        单个文件导出功能, 导出一个文件, 对比导出成功的文件数/导出路径下的文件数是不是1, 是就算成功
        """
        # 导入文件
        self.importFile()

        # 点击修复按钮
        BasePage(self.app).control_click("Name", "Start Repair")
        logger().info("修复中, 请耐心等待")

        # 等待修复完
        waitRepairComplete(self.app)

        # 点击导出
        BasePage(self.app).control_click("Name", "Succeeded")
        if not BasePage(self.app).control_exists("浏览文件夹"):
            BasePage(self.app).control_click("Name", "Export")

        # 根据导出路径选择文件夹
        if exportPopup(self.app, self.exportFilePath):
            # 等待导出完成
            result = waitExportComplete(self.app)

            # 获取导出路径下的文件数
            for root, dirs, file in os.walk(self.exportFilePath):
                if len(file) == 1 and result == 1:
                    logger().info(f"成功导出{len(file)}个文件")

                    return True
                return False
        else:
            return False
