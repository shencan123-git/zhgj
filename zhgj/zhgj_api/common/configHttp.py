#__author__ = 'Daolin.Yang'
#coding=utf-8
#!/usr/bin/python

import requests
import config

#获取文件路径
localconfig = config.config()


class configHttp:
    def __init__(self):
        #定义在函数外的变量赋值
        global scheme,baseurl,port,timeout
        #参数化设定请求接口
        scheme = localconfig.get_http("scheme")
        baseurl = localconfig.get_http("baseurl")
        port = localconfig.get_http("port")
        timeout = localconfig.get_http("timeout")
        # self.log = MyLog.get_log()
        # self.logger = self.log.get_logger()
        self.url = None
        self.method = None
        self.headers = {}
        self.data = {}
        self.params = {}
        self.files = {}
        self.file_path = None

    #取config的值，完成url拼接
    def set_url(self,url):
        self.url=scheme + '://'+ baseurl +'/'+url
        return self.url
    #取config的值
    def set_headers(self, header):
        self.headers = header
        return self.headers
    #请求参数
    def set_params(self, param):
        self.params = param
        return self.params
    def set_files(self, files):
        self.files = files
        return self.params
    #请求参数
    def set_data(self, data):
        self.data = data
        return self.data

    def HttpMethod(self,method):
        self.method=method
        if self.method == 'get':
        #请求方式名称为get，传params
            response = requests.get(self.url,params=self.params,headers=self.headers,timeout=float(timeout),verify=False)
            return response
        #请求方式名称为post，传data
        elif self.method == 'post':
            response = requests.post(self.url, data=self.data, headers=self.headers, timeout=float(timeout),verify=False)
            return response
        #请求方式名称为postWithFile，传data,files
        elif self.method == 'postWithFile':
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,timeout=float(timeout),verify=False)
            return response
        #请求方式名称为postWithJson，传json
        elif self.method == 'postWithJson':
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout),verify=False)
            return response
        # else:
        #     self.logger.error("No this interface's method:" + self.method)


if __name__=="__main__":
    print("ConfigHTTP")