#__author__ = 'Daolin.Yang'
#coding=utf-8
#!/usr/bin/python


import logging
from datetime import datetime
import threading
import config
import os

class Log:
    def __init__(self):
        global logPath, resultPath, fileDir
        fileDir = config.fileDir
        resultPath = os.path.join(fileDir, "result")
        # # 判断resultPath文件夹是否存在，不存在则创建
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        #拼接一个路径：common/result/%Y%m%d%H%M%S
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        #判断resultPath文件夹下，是否存在文件，不存在则创建
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        # 初始化日志
        self.logger = logging.getLogger()
        # 设置日志级别
        self.logger.setLevel(logging.INFO)
        # 输出日志到文件
        handler = logging.FileHandler(os.path.join(logPath, "output.txt"),encoding="utf-8-sig")
        # 设置日志的log信息顺序,结构和内容
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 写入log文件
        handler.setFormatter(formatter)
        # 刷新log文件
        self.logger.addHandler(handler)
    # 初始化日志
    def get_logger(self):
        return self.logger

    def build_start_line(self, case_no):
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        self.logger.info("--------" + case_no + " END--------")

    def build_case_line(self, case_name, code, msg):
        self.logger.info(case_name+" - Code:"+code+" - msg:"+msg)

    def build__sql_pass_line(self, case_name):
        self.logger.info(case_name+str(" - 数据库对比成功"))

    def build__sql_fail_line(self, case_name):
        self.logger.info(case_name+str(" - 数据库对比失败"))

    def get_report_path(self):
        report_path = os.path.join(logPath, "report.html")
        return report_path

    def get_log_path(self):
        log_path = os.path.join(logPath, "output.txt")
        return log_path

    def get_result_path(self):
        return logPath

    def write_result(self, result):
        result_path = os.path.join(logPath, "report.txt")
        fb = open(result_path, "wb")
        fb.write(result)



class MyLog:
    #使用递归锁,创建Rlock对象，在需要加锁时使用
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            #只有一个线程能成功地获取锁
            MyLog.mutex.acquire()
            MyLog.log = Log()
            #解锁
            MyLog.mutex.release()

        return MyLog.log

if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")