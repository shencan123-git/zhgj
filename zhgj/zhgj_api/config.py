#__author__ = 'Daolin.Yang'
#coding=utf-8
#!/usr/bin/python


import os
import codecs
import configparser
#拼接路径
fileDir = os.path.split(os.path.realpath(__file__))[0]
configPath=os.path.join(fileDir,"config.ini")
print configPath
class config:
    #打开configPath文件
    def __init__(self):
        fd=open(configPath)
        data=fd.read()
        ##判断是否为带BOM文件，如果带直接改写文件内容
        if data[::3]==codecs.BOM_UTF8:
            data=data[3:]
            file=codecs.open(configPath,"w")
            file.write(data)
            file.close()
        fd.close()
        ##  实例化configParser对象
        self.cf=configparser.ConfigParser()
        self.cf.read(configPath)

    #获取HTTP分组下指定name的值
    def get_http(self,name):
        value=self.cf.get("HTTP",name)
        return value
    #获取HEADERS分组下指定name的值
    def get_headers(self,name):
        value=self.cf.get("HEADERS",name)
        return value
    #获取HEADERS分组下指定name的值
    def get_DB(self,name):
        value=self.cf.get("mysql",name)
        return str(value)
    #修改headers分组下指定name的值value
    def set_headers(self, name, value):
        self.cf.set("HEADERS", name, value)
        with open(configPath, 'w+') as f:
            self.cf.write(f)
            f.close()
#test
if __name__ == '__main__':
    test=config()
    value=test.get_DB("user")
    print(value)