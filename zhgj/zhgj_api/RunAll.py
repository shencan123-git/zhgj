#__author__ = 'Daolin.Yang'
#coding=utf-8
#!/usr/bin/python

from threading import Thread
import raed_path
import os
import unittest
#from BeautifulReport import BeautifulReport
import config as config
#from common.HTMLTestRunner import HTMLTestRunner
import HTMLTestRunner
from common.Log import MyLog as Log
#from common.configEmail import MyEmail
#import Training_interface.common.configDingTalk as DingTalk
import threading

add_path = raed_path.get_path()
localReadConfig = config.config()

class AllTest:
    def __init__(self):
        global log, logger, resultPath,log_path,beauReportPath, DingTalk_on_off#Email_on_off
        log = Log.get_log()
        logger = log.get_logger()
        resultPath = log.get_report_path()
        log_path = log.get_log_path()
        beauReportPath=log.get_result_path()
        self.caseListFile = os.path.join(config.fileDir, "caselist.txt")
        self.caseFile = os.path.join(config.fileDir, "TestCase")
        #Email_on_off = localReadConfig.get_email("on_off")
        # DingTalk_on_off = localReadConfig.get_DingTalk("on_off")
        #self.caseFile = None
        #self.email = MyEmail.get_email()
        # self.Dingtalk = DingTalk.DingTalk()
    #读取caselist.txt文件，放入self.caseList
        self.caseList = []
    def set_case_list(self):
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        #执行set_case_list
        self.set_case_list()
        suite_module = []
        #实例化测试套件
        test_suite = unittest.TestSuite()
        #循环列表self.caseList
        for case in self.caseList:
            case_name = case.split("/")[-1]
            print(case_name)
            if case_name in add_path:
                #加载用例
                discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name)
                suite_module.append(discover)
                # runner = unittest.TextTestRunner()
                # runner.run(discover)
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    #添加测试集
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite


    def run(self):
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("********TEST START********")
                #添加测试报告文件
                with open(resultPath, mode='wb') as fp:
                        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告',description=u'测试执行情况')
                        runner.run(suit)



                # with open(resultPath, mode='wb') as fp:
                #     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Interface Test Report',description='Test Description')
                #     demo = runner.run(suit)
                #     fp.write(demo)
            else:
                logger.info("Have no case to test.")
        except Exception as ex:
            logger.error(str(ex))

if __name__ == '__main__':
    obj = AllTest()
    mutex = threading.Lock()

    def __init__(self):
        pass
    def get_log():

        if obj.run is not None:
            #只有一个线程能成功地获取锁
            obj.mutex.acquire()
            MyLog.log = Log()
            #解锁
            MyLog.mutex.release()

        return MyLog.log
        '''
        finally:
            logger.info("*********TEST END*********")
            # send test report by email
            if Email_on_off == 'on':
                self.email.send_email()
            elif Email_on_off == 'off':
                logger.info("Doesn't send report email to developer.")
            else:
                logger.info("Unknow state.")
            # # send test report by DingTalk
            # if DingTalk_on_off == 'on':
            #     #self.Dingtalk.send_message_to_robot()
            # elif DingTalk_on_off == 'off':
            #     logger.info("Doesn't send report DingTalk to developer.")
            # else:
            #     logger.info("Unknow state.")
'''       '''
if __name__ == '__main__':
    obj = AllTest()
    obj.run()
'''
'''
from TestCase import TestLogin
from TestCase import TestLoginfailed
import HTMLTestRunner
import unittest
import sys

# testcase=TestLogin.LoginTest
# testcase1=TestLoginfailed.LoginTestFailed

#run()方法
#构造测试集
# suite = unittest.TestSuite()
# suite.addTest(testcase('test_login'))
# suite.addTest(testcase1('test_login_failed'))
#
# #执行测试集合
# runner = unittest.TextTestRunner()
# runner.run(suite)
#discover方法

test_dir = 'D:\\Training_interface1111111\\common'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')
# runner = unittest.TextTestRunner()
# runner.run(discover)
if discover is not None:
    print("********TEST START********")
    # generate by HTMLTestrunner
    fp = open('D:\Training_interface1111111\\testreport.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
    runner.run(discover)
    fp.close()
    print("********TEST END********")
else:
    print("Have no case to test.")
'''


