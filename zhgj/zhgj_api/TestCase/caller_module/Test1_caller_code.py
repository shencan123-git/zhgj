#__author__ = 'Daolin.Yang'
#coding=utf-8
#!/usr/bin/python

import config
from common import common
from common import configxls
from common.Log import MyLog as Log
import unittest
import paramunittest
from TestCase.user_module.Test1_user_login_flow import raed_configmysql
from TestCase.user_module.Test1_user_login_flow import raed_config
from TestCase.user_module.Test1_user_login_flow import raed_configHttp



raed_xml = common.GetUrl_from_xml('zhgj_caller_Code')
xls = configxls.get_xls('caller.xlsx','caller_code')
raed_xls = xls.get_rows
@paramunittest.parametrized(*raed_xls)
class staff_code(unittest.TestCase):
    def setParameters(self,case_name,method,phone,sendType,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
        self.phone = phone
        self.sendType = sendType
        self.result = result
        self.code = str(code)
        self.msg = str(msg)
        self.info = None
        self.response = None
        self.sql = None


    def setUp(self):
        print("-------statest---------")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()

    def test1_staff_code(self):
        #set_url
        url = raed_xml
        raed_configHttp.set_url(url)
        print(raed_configHttp.set_url(url))

        #set_head
        header = {'Content-Type':raed_config.get_headers('Content-Type'),
                  'token':raed_config.get_headers('token')
                  }
        raed_configHttp.set_headers(header)
        print(raed_configHttp.set_headers(header))

        #set_data
        data = {
                "phone": self.phone,
                "sendType": self.sendType
                }
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

        #请求接口
        self.response = raed_configHttp.HttpMethod(self.method)
        print(self.response.text)

        self.add_result()

    def tearDown(self):
        self.sql =raed_configmysql.query_one(common.get_sql("caller","caller_code","caller_code"))
        if str(self.sql) == str(self.phone):
            self.log.build_case_line(self.case_name, str(self.info["code"]), str(self.info['msg']))
            self.log.build__sql_pass_line(self.case_name)
        else:
            self.log.build_case_line(self.case_name, str(self.info["code"]), str(self.info['msg']))
            self.log.build__sql_fail_line(self.case_name)
    def add_result(self):
        self.info = self.response.json()
        #common.show_return_json(self.response)
        if self.result == '0':
            self.assertEqual(str(self.info['code']),self.code)
            self.assertEqual(str(self.info['msg']),self.msg)
        if self.result == '1':
            self.assertEqual(str(self.info['code']),self.code)
            self.assertEqual(str(self.info['msg']),self.msg)

if __name__ == '__main__':
    unittest.main()

