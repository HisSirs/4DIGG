from Common.AppStart import closeApp, openApp
from Common.Logger import logger
from testCase.doUITemp import doUITemp

class Test_Document:
    # def setUp(self):
    #     openApp()
    #
    # def tearDown(self):
    #     closeApp()
    # 

    def test_File_Import(self):
        actualValue, expectValue, title = doUITemp("File Repair", "test_File_Import",
                                                   "DocumentRepairCase.json").doUiTemp()
        assert actualValue == expectValue
        logger().info(f"{title} Pass")
    
    
    def test_Single_File_Remove(self):
        actualValue, expectValue, title = doUITemp("File Repair", "test_Single_File_Remove",
                                                   "DocumentRepairCase.json").doUiTemp()
        assert actualValue == expectValue
        logger().info(f"{title} Pass")
    
    
    #
    def test_All_Files_Remove(self):
        actualValue, expectValue, title = doUITemp("File Repair", "test_All_Files_Remove",
                                                   "DocumentRepairCase.json").doUiTemp()
        assert actualValue == expectValue
        logger().info(f"{title} Pass")
    
    
    def test_File_Repair(self):
        actualValue, expectValue, title = doUITemp("File Repair", "test_File_Repair",
                                                   "DocumentRepairCase.json").doUiTemp()
        assert actualValue == expectValue
        logger().info(f"{title} Pass")
    
    
    def test_File_High_Repair_psd(self):
        actualValue, expectValue, title = doUITemp("File Repair", "test_File_High_Repair_psd",
                                                   "DocumentRepairCase.json").doUiTemp()
        assert actualValue == expectValue
        logger().info(f"{title} Pass")
    
    
    # psb格式高级修复暂时无资源
    def test_File_High_Repair_psb(self):
        actualValue, expectValue, title = doUITemp("File Repair", "test_File_High_Repair_psb",
                                                   "DocumentRepairCase.json").doUiTemp()
        assert actualValue == expectValue
        logger().info(f"{title} Pass")
    
    
    def test_All_File_Export(self):
        actualValue, expectValue, title = doUITemp("File Repair", "test_All_File_Export",
                                                   "DocumentRepairCase.json").doUiTemp()
        assert actualValue == expectValue
        logger().info(f"{title} Pass")
    
    
    def test_Single_File_Export(self):
        actualValue, expectValue, title = doUITemp("File Repair", "test_Single_File_Export",
                                                   "DocumentRepairCase.json").doUiTemp()
        assert actualValue == expectValue
        logger().info(f"{title} Pass")
