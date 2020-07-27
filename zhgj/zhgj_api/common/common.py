#__author__ = 'Daolin.Yang'
#coding=utf-8
#!/usr/bin/python
import re
import os
import json
from xml.etree import ElementTree as ElementTree
import config


fileDir = config.fileDir
localconfig=config.config()
'''
#获取请求接口前，传入参数
def get_authorization(json,name):
     info = json['data']
     value = info[name]
     return value

#获取请求接口后，接收参数
def show_return_json(response):
     url = response.url
     info = response.text
     print("\nrequest url:"+url)
     #要输出中文需要指定ensure_ascii参数为False，如下代码片段
     print("\nreturn json info:"+'\n'+json.dumps(json.loads(info), ensure_ascii=False, sort_keys=True, indent=4))
     return info
'''

#解析xml文件，拼接一个接口地址
def GetUrl_from_xml(name):
    url_list = []
    #拼接路径
    url_path = os.path.join(fileDir, 'TestFile', 'zhgj.xml')
    #载入数据
    tree = ElementTree.parse(url_path)
    #findall查找根节点url的name
    for u in tree.findall('url'):
        url_name = u.get('name')
        if url_name == name:
            #读根节点url下的子节点
            for c in u.getchildren():
                url_list.append(c.text)

    url ='/'.join(url_list)
    return url
database = {}
def set_xml():
    if len(database) == 0:
        sql_path = os.path.join(fileDir, "testFile", "SQL.xml")
        #载入数据
        tree = ElementTree.parse(sql_path)
        #findall查找根节点database的name
        for db in tree.findall("database"):
            db_name = db.get("name")
            #print(db_name)
            table = {}
            #读根节点database下的子节点table
            for tb in db.getchildren():
                table_name = tb.get("name")
                #print(table_name)
                sql = {}
                #读根节点table下的子节点sql
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    #print(sql_id)
                    sql[sql_id] = data.text
                    if table.values() and table_name in table:
                        #满足条件，添加update，到字典中
                        table[table_name].update(sql)
                    else:
                        table[table_name]=sql
            database[db_name] = table
            #print(database)


def get_xml_dict(database_name, table_name):
    set_xml()
    #get返回字典值
    database_dict = database.get(database_name).get(table_name)
    return database_dict

def get_sql(database_name, table_name, sql_id):
    #db_env = get_DB_ENV()
    #get返回字典值
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    #sql_value = db.get(sql_id)
    #pattern = re.compile(r'-.+?(?=`)')
    #print(pattern.findall(sql_value))
    #sql = re.sub(pattern, '-'+db_env, sql_value)
    return sql
'''
def get_DB_ENV():
    value = localconfig.get_DB('username')
    suffix = re.findall('_(.*)',value)
    db_name = ''.join(suffix)
    return db_name
'''


if __name__=='__main__':
    xml=GetUrl_from_xml('zhgj_caller_Code')
    print(xml)
    a = get_sql("caller","caller_code_verify","caller_code_verify")
    print(a)
