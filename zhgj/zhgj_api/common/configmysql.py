#__author__ = 'Daolin.Yang'
#coding=utf-8
#!/usr/bin/python

import pymysql
import config
import time
import common

localconfig = config.config()

class DBMsql():
    def __init__(self,):
        host = localconfig.get_DB('host')
        port = localconfig.get_DB('port')
        user = localconfig.get_DB('user')
        password = localconfig.get_DB('password')
        charset = localconfig.get_DB('charset')
        database = localconfig.get_DB('database')
        self.num = 0
        while self.num <= 3:
            try:
                # 连接数据库
                self.conn = pymysql.connect(host=host,
                                    port=int(port),
                                    user=user,
                                    password=password,
                                    charset=charset,
                                    database=database,
                                    )
                self.cursor = self.conn.cursor()
                print("Connect DB successfully!")
                break
            except Exception as ex:
                self.num+=1
                print("Connect DB failed and The No.%s Attempting connection to the database" %self.num)
                time.sleep(2)

    def query_one(self, sql, args=None):
        """
        执行生气了语句，返回单数据
        :param sql:
        :param args: 列表或者元祖，此参数主要为sql语句中的占位提供参数
        :return:
        """
        self.conn.commit()
        self.cursor.execute(sql, args)
        resuit = self.cursor.fetchone()
        # 关闭数据库连接
        #self.cursor.close()
        #self.conn.close()
        print(resuit[0])
        return resuit[0]



if __name__ == '__main__':
    a = DBMsql().query_one(common.get_sql("user","div_del","div_del"))