#__author__ = 'Daolin.Yang'
#coding=utf-8
#!/usr/bin/python

import config
from common import common
from common import configHttp
from common import configxls
from common import configmysql
from common.Log import MyLog as Log
import unittest
import paramunittest
import logging
import json
import raed_path
import os


raed_config  = config.config()
raed_xml = common.GetUrl_from_xml('zhgj_caller_add')
xls = configxls.get_xls('caller.xlsx','caller_add')
raed_xls = xls.get_rows
raed_configHttp = configHttp.configHttp()
raed_configmysql = configmysql.DBMsql()


@paramunittest.parametrized(*raed_xls)
class caller_add(unittest.TestCase):
    def setParameters(self,case_name,method,visitorPhone,workerName,note,idCardNumber,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
        self.visitorPhone = visitorPhone
        self.workerName = workerName
        self.note = note
        self.idCardNumber = idCardNumber
        self.result = result
        self.code = code
        self.msg = msg
        self.info = None
        self.response = None
        self.username = None


    def setUp(self):
        print("-------statest---------")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()

    def test2_caller_add(self):
        #set_url
        url = raed_xml
        raed_configHttp.set_url(url)
        print(raed_configHttp.set_url(url))

        #set_head
        #'Content-Type':raed_config.get_headers('Content-Type')去掉，否则报500
        header = {
                  'token':raed_config.get_headers('token')
                  }
        raed_configHttp.set_headers(header)
        print(raed_configHttp.set_headers(header))

        #set_data
        data = {
                "visitorPhone": self.visitorPhone,
                "workerName":self.workerName,
                "note": self.note,
                "idCardNumber": self.idCardNumber,
                "checkCode":str(raed_configmysql.query_one(common.get_sql("caller","caller_code_verify","caller_code_verify"))),
                "subContractorId": raed_config.get_headers('subContractorId')
                }
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

        #ste_file
        files = {'headImage':('6.jpg',open(str(raed_path.get_imsg_pash('6.jpg')),'rb'),'image/jpeg')}
        raed_configHttp.set_files(files)
        print(raed_configHttp.set_files(files))

        #请求接口
        self.response = raed_configHttp.HttpMethod(self.method)
        print(self.response.text)


        self.add_result()

    def tearDown(self):
        self.log.build_case_line(self.case_name, str(self.info["code"]), str(self.info['msg']))
    def add_result(self):
        self.info = self.response.json()
        #common.show_return_json(self.response)
        if self.result == '0':
            self.assertEqual(str(self.info['code']),self.code)
            self.assertEqual(self.info['msg'],self.msg)
        if self.result == '1':
            self.assertEqual(str(self.info['code']),self.code)
            self.assertEqual(self.info['msg'],self.msg)

if __name__ == '__main__':
    unittest.main()

