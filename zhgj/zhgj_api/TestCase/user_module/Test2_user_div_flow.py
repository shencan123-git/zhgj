#__author__ = 'Daolin.Yang'
#coding=utf-8
#!/usr/bin/python

from common import common
from common import configxls
from common.Log import MyLog as Log
import unittest
import paramunittest
from TestCase.user_module.Test1_user_login_flow import raed_configmysql
from TestCase.user_module.Test1_user_login_flow import raed_config
from TestCase.user_module.Test1_user_login_flow import raed_configHttp


raed_xml = common.GetUrl_from_xml('zhgj_userdiv')
xls = configxls.get_xls('user.xlsx','userdiv')
raed_xls = xls.get_rows
@paramunittest.parametrized(*raed_xls)
class test1_user_div(unittest.TestCase):
    def setParameters(self,case_name,method,myDepartmentId,parentId,departmentName,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
        self.myDepartmentId = myDepartmentId
        self.parentId = parentId
        self.departmentName = departmentName
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

    def test1_user_div(self):
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
                "myDepartmentId": self.myDepartmentId,
                "parentId": self.parentId,
                 "departmentName": self.departmentName
                }
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

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



raed_xml1 = common.GetUrl_from_xml('zhgj_userdiv_info')
xls1 = configxls.get_xls('user.xlsx','userdiv_info')
raed_xls1 = xls1.get_rows
@paramunittest.parametrized(*raed_xls1)
class test2_user_div_info(unittest.TestCase):
    def setParameters(self,case_name,method,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
        self.result = result
        self.code = code
        self.msg = msg
        self.info = None
        self.info1 = None
        self.info2 = None
        self.response = None


    def setUp(self):
        print("-------statest---------")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()

    def test1_user_div_info(self):
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
        data = {
                }
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

        #请求接口
        self.response = raed_configHttp.HttpMethod(self.method)
        print(self.response.text)

        self.add_result()

    def tearDown(self):
        self.info = self.response.json()
        if self.info['msg'] == '操作成功':
            self.info1 = str(self.info['data'][0]['childList'][0]['departmentId'])
            if self.info1  is not None:
                raed_config.set_headers('departmentId',self.info1)
            self.info2 = str(self.info['data'][0]['childList'][0]['parentId'])
            if self.info2  is not None:
                raed_config.set_headers('parentId',self.info2)
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


raed_xm2 = common.GetUrl_from_xml('zhgj_userdiv')
xls2 = configxls.get_xls('user.xlsx','userdiv_amend')
raed_xls2 = xls2.get_rows
@paramunittest.parametrized(*raed_xls2)
class test3_user_div_amend(unittest.TestCase):
    def setParameters(self,case_name,method,departmentName,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
        self.departmentName = str(departmentName)
        self.result = result
        self.code = code
        self.msg = msg
        self.info = None
        self.response = None
        self.sql = None


    def setUp(self):
        print("-------statest---------")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()

    def test1_user_div_amend(self):
        #set_url
        url = raed_xm2
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
                "myDepartmentId": raed_config.get_headers('departmentid'),
                "parentId": raed_config.get_headers('parentid'),
                 "departmentName": self.departmentName
                }
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

        #请求接口
        self.response = raed_configHttp.HttpMethod(self.method)
        print(self.response.text)

        self.add_result()

    def tearDown(self):
        if self.info['msg'] == '操作成功':
            self.sql =raed_configmysql.query_one(common.get_sql("user","div_info","div_info"))
            if str(self.sql) ==self.departmentName:
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


raed_xml3 = common.GetUrl_from_xml('zhgj_userdiv_del')
xls3 = configxls.get_xls('user.xlsx','userdiv_del')
raed_xls3 = xls3.get_rows
@paramunittest.parametrized(*raed_xls3)
class test4_user_div_del(unittest.TestCase):
    def setParameters(self,case_name,method,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
        self.result = result
        self.code = code
        self.msg = msg
        self.response = None
        self.sql = None
        self.info = None

    def setUp(self):
        print("-------statest---------")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()

    def test1_user_div_del(self):
        #set_url
        url = raed_xml3
        raed_configHttp.set_url(url)
        print(raed_configHttp.set_url(url))

        #set_head
        header = {'Content-Type':raed_config.get_headers('Content-Type'),
                  'token':raed_config.get_headers('token')
                  }
        raed_configHttp.set_headers(header)
        print(raed_configHttp.set_headers(header))

        #set_data
        data = {"myDepartmentId": raed_config.get_headers('departmentid')
                }
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

        #请求接口
        self.response = raed_configHttp.HttpMethod(self.method)
        print(self.response.text)

        self.add_result()

    def tearDown(self):
            self.sql =raed_configmysql.query_one(common.get_sql("user","div_del","div_del"))
            if self.sql == 1:
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

