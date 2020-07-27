#__author__ = 'Daolin.Yang'
#coding=utf-8
#!/usr/bin/python

from common import common
from common import configxls
from common.Log import MyLog as Log
import unittest
import paramunittest
import logging
import raed_path
from TestCase.user_module.Test1_user_login_flow import raed_configmysql
from TestCase.user_module.Test1_user_login_flow import raed_config
from TestCase.user_module.Test1_user_login_flow import raed_configHttp



raed_xml = common.GetUrl_from_xml('zhgj_staff_add')
xls = configxls.get_xls('user.xlsx','staff_add')
raed_xls = xls.get_rows
@paramunittest.parametrized(*raed_xls)
class test1_staff_add(unittest.TestCase):
    def setParameters(self,case_name,method,workerName,myPhone,nation,address,isLogin,idcardNumber,birthday,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
        self.workerName = workerName
        self.myPhone = myPhone
        self.nation = nation
        self.address = address
        self.isLogin = isLogin
        self.idcardNumber = idcardNumber
        self.birthday = birthday
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

    def test1_staff_add(self):
        #set_url
        url = raed_xml
        raed_configHttp.set_url(url)
        print(raed_configHttp.set_url(url))

        #set_head
        #'Content-Type':raed_config.get_headers('Content-Type')删除，否则报500
        header = {
                  'token':raed_config.get_headers('token')
                  }
        raed_configHttp.set_headers(header)
        print(raed_configHttp.set_headers(header))

        #set_data
        data = {"myCompanyEmployeeId": "",
                "workerName": self.workerName,
                "myPhone": self.myPhone,
                "nation":self.nation,
                "address": self.address,
                "myDepartmentId": raed_config.get_headers('myDepartmentId'),
                "isLogin": self.isLogin,
                "idcardNumber":self.idcardNumber,
                "birthday": self.birthday
                }
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

        #ste_file
        files = {'file':('2.jpg',open(str(raed_path.get_imsg_pash('1.jpg')),'rb'),'image/jpeg')}
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



raed_xml1 = common.GetUrl_from_xml('zhgj_staff_info')
xls1 = configxls.get_xls('user.xlsx','staff_info')
raed_xls1 = xls1.get_rows
@paramunittest.parametrized(*raed_xls1)
class test2_staff_info_list(unittest.TestCase):
    def setParameters(self,case_name,method,keyword,pageNum,pageSize,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
        self.keyword = keyword
        self.pageNum = pageNum
        self.pageSize = pageSize
        self.result = result
        self.code = code
        self.msg = msg
        self.info = None
        self.response = None

    def setUp(self):
        print("-------statest---------")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()

    def test1_staff_info_list(self):
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
            "keyword": "",
            "myDepartmentId": raed_config.get_headers("myDepartmentId"),
            "pageNum": self.pageNum,
            "pageSize": self.pageSize
                }
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

        #请求接口
        self.response = raed_configHttp.HttpMethod(self.method)
        print(self.response.text)

        self.add_result()

    def tearDown(self):
        self.info = self.response.json()
        self.info1 = str(self.info['data']['list'][0]['companyEmployeeId'])
        raed_config.set_headers('companyEmployeeId',self.info1)
        self.info2 = str(self.info['data']['list'][1]['companyEmployeeId'])
        raed_config.set_headers('companyEmployeeId_1',self.info2)

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

raed_xml2 = common.GetUrl_from_xml('zhgj_staff_info_staff')
xls2 = configxls.get_xls('user.xlsx','staff_info_staff')
raed_xls2 = xls2.get_rows
@paramunittest.parametrized(*raed_xls2)
class test3_staff_info_shaff(unittest.TestCase):
    def setParameters(self,case_name,method,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
        self.result = result
        self.code = code
        self.msg = msg
        self.response = None


    def setUp(self):
        print("-------statest---------")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()

    def test1_staff_info_staff(self):
        #set_url
        url = raed_xml2
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
                 "myCompanyEmployeeId": raed_config.get_headers("companyemployeeid")
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

raed_xml3 = common.GetUrl_from_xml('zhgj_staff_add')
xls3 = configxls.get_xls('user.xlsx','staff_amend')
raed_xls3 = xls3.get_rows
@paramunittest.parametrized(*raed_xls3)
class test4_staff_amend(unittest.TestCase):
    def setParameters(self,case_name,method,workerName,myPhone,nation,address,isLogin,idcardNumber,birthday,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
        self.workerName = workerName
        self.myPhone = myPhone
        self.nation = nation
        self.address = address
        self.isLogin = isLogin
        self.idcardNumber = idcardNumber
        self.birthday = birthday
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

    def test1_staff_amend(self):
        #set_url
        url = raed_xml3
        raed_configHttp.set_url(url)
        print(raed_configHttp.set_url(url))

        #set_head
        #'Content-Type':raed_config.get_headers('Content-Type')删除，否则报500
        header = {
                     'token':raed_config.get_headers('token')
                  }
        raed_configHttp.set_headers(header)
        print(raed_configHttp.set_headers(header))

        #set_data
        data = {"myCompanyEmployeeId":raed_config.get_headers('companyemployeeid'),
                "workerName": self.workerName,
                "myPhone": self.myPhone,
                "nation": self.nation,
                "address": self.address,
                "myDepartmentId": raed_config.get_headers('mydepartmentid'),
                "isLogin": self.isLogin,
                "idcardNumber": self.idcardNumber,
                 "birthday": self.birthday
                }
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

        #ste_file
        files = {'file':('3.jpg',open(str(raed_path.get_imsg_pash('3.jpg')),'rb'),'image/jpeg')}
        raed_configHttp.set_files(files)
        print(raed_configHttp.set_files(files))

        #请求接口
        self.response = raed_configHttp.HttpMethod(self.method)
        print(self.response.text)

        self.add_result()

    def tearDown(self):
        if self.info['msg'] == '操作成功':
            self.sql =raed_configmysql.query_one(common.get_sql("user","staff_amend","staff_amend"))
            if str(self.sql) ==self.workerName:
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

raed_xml4 = common.GetUrl_from_xml('zhgj_staff_export')
xls4 = configxls.get_xls('user.xlsx','staff_export')
raed_xls4 = xls4.get_rows
@paramunittest.parametrized(*raed_xls4)
class test5_staff_export(unittest.TestCase):
    def setParameters(self,case_name,method,keyword,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
        self.operateType = str(keyword)
        self.result = result
        self.code = code
        self.msg = msg
        self.response = None
        self.sql = None


    def setUp(self):
        print("-------statest---------")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()

    def test1_staff_export(self):
        #set_url
        url = raed_xml4
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
                 "keyword":"",
                "myDepartmentId": raed_config.get_headers("companyemployeeid")
                }
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

        #请求接口
        self.response = raed_configHttp.HttpMethod(self.method)

        self.add_result()

    def tearDown(self):
        logging.info("导出接口可用")
    def add_result(self):
        #common.show_return_json(self.response)
        if self.response.text is not None:
            pass



raed_xml5 = common.GetUrl_from_xml('zhgj_staff_mangea')
xls5 = configxls.get_xls('user.xlsx','staff_manage')
raed_xls5 = xls5.get_rows
@paramunittest.parametrized(*raed_xls5)
class test6_staff_managa(unittest.TestCase):
    def setParameters(self,case_name,method,operateType,result,code,msg):
        self.case_name=str(case_name)
        self.method = str(method)
        self.operateType = str(operateType)
        self.result = result
        self.code = code
        self.msg = msg
        self.response = None
        self.sql = None


    def setUp(self):
        print("-------statest---------")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()

    def test1_staff_manage(self):
        #set_url
        url = raed_xml5
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
                 "myCompanyEmployeeId": raed_config.get_headers("companyemployeeid"),
                    "operateType": self.operateType
                }
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

        #请求接口
        self.response = raed_configHttp.HttpMethod(self.method)
        print(self.response.text)


        self.add_result()

    def test2_staff_manage(self):
        #set_url
        url = raed_xml5
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
                 "myCompanyEmployeeId": raed_config.get_headers("companyEmployeeId_1"),
                    "operateType": self.operateType
                }
        raed_configHttp.set_data(data)
        print(raed_configHttp.set_data(data))

        #请求接口
        self.response = raed_configHttp.HttpMethod(self.method)
        print(self.response.text)

        self.add_result()
    def tearDown(self):
        if self.operateType in str(range(1,4)):
            self.log.build_case_line(self.case_name, str(self.info["code"]), str(self.info['msg']))
        elif self.operateType == str(4):
            self.sql = raed_configmysql.query_one(common.get_sql("user","staff_del","staff_del"))
            if self.sql == 1:
                self.log.build_case_line(self.case_name, str(self.info["code"]), str(self.info['msg']))
                self.log.build__sql_pass_line(self.case_name)
        else:
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

