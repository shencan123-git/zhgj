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

raed_config  = config.config()
raed_configHttp = configHttp.configHttp()
raed_configmysql = configmysql.DBMsql()




raed_xml = common.GetUrl_from_xml('zhgj_login')
xls = configxls.get_xls('user.xlsx','login1')
raed_xls = xls.get_rows
@paramunittest.parametrized(*raed_xls)
@unittest.skip("token有效，跳过登录")
class test1_user_login(unittest.TestCase):
    def setParameters(self,case_name,method,username,password,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
        self.username = str(username)
        self.password = str(password)
        self.result = result
        self.code = code
        self.msg = msg
        self.info = ""
        self.response = ""
        self.token = None


    def setUp(self):
        print("-------statest---------")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
    def test1_login1(self):
        #set_url
        url = raed_xml
        raed_configHttp.set_url(url)
        print(raed_configHttp.set_url(url))

        #set_head
        header = {'Content-Type':raed_config.get_headers('Content-Type')}
        raed_configHttp.set_headers(header)
        print(raed_configHttp.set_headers(header))

        #set_data
        data = {'deviceInfo': "WEB :dc3798ad-3d14-473a-8187-a7e63c4d9165",
                'password': self.password,
                'username': self.username
                }
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

        #请求接口
        self.response = raed_configHttp.HttpMethod(self.method)
        print(self.response.text)


        self.add_result()


    def tearDown(self):
        self.info = self.response.json()
        self.token = self.info["data"]["token"]
        raed_config.set_headers("token",self.token)
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



raed_xml1 = common.GetUrl_from_xml('zhgj_userInfo')
xls1 = configxls.get_xls('user.xlsx','userinfo')
raed_xls1 = xls1.get_rows
@paramunittest.parametrized(*raed_xls1)
class test2_user_info(unittest.TestCase):#执行用例
    def setParameters(self,case_name,method,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
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

    def test2_user_info(self):
        #set_url
        url = raed_xml1
        raed_configHttp.set_url(url)
        print(raed_configHttp.set_url(url))

        #set_head
        header = {'Content-Type':raed_config.get_headers('Content-Type'),
                  'token':raed_config.get_headers('token')
                  }
        raed_configHttp.set_headers(header)
        print(raed_configHttp.set_headers(header))

        #set_data
        data = {}
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

        #请求接口
        self.response = raed_configHttp.HttpMethod(self.method)
        print(self.response.text)


        self.add_result()


    def tearDown(self):
        self.info = self.response.json()
        self.sql =raed_configmysql.query_one(common.get_sql("user","info","user_info"))
        self.username = self.info["data"]["username"]
        if self.sql == self.username:
            raed_config.set_headers("myDepartmentId",self.info['data']['departmentId'])
            raed_config.set_headers("subContractorId",str(self.info['data']['subContractorId']))
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
            self.assertEqual(self.info['msg'],self.msg)
        if self.result == '1':
            self.assertEqual(str(self.info['code']),self.code)
            self.assertEqual(self.info['msg'],self.msg)


if __name__ == '__main__':
    unittest.main()