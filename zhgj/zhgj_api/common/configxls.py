#__author__ = 'Daolin.Yang'
#coding=utf-8
#!/usr/bin/python

import xlrd
import os
import config


fileDir=config.fileDir


class get_xls(object):
    def __init__(self,xls_name,sheetname):
        self.xls_name=xls_name
        self.sheetname=sheetname
#        self.rowindex=rowindex
        #拼接路径文件self.xls_name
        self.xlsfilepath=os.path.join(fileDir,'TestFile','case',self.xls_name)

     #获取索引
    @property
    def getsheet(self):
        #打开文件
        workbook=xlrd.open_workbook(self.xlsfilepath)
        #获取所有sheet工作表名
        sheetname=workbook.sheet_by_name(self.sheetname)
        return sheetname

    #获取所有行
    @property
    def getrows(self):
        rows=self.getsheet.nrows
        return rows

    #获取所有列
    @property
    def getclos(self):
        cols=self.getsheet.ncols
        return cols

    @property
    def get_rows(self):
        rows=[]
        #获所有行
        rowNum=self.getsheet.nrows
        #获取指定行
        rowlist=self.getsheet.row_values
        #判断指定行的数据，是否为case_name
        for i in range(rowNum):
            if rowlist(i)[0] != u'case_name':
                rows.append(rowlist(i))
        return rows


if __name__=="__main__":
    excel=get_xls('caller.xlsx','caller_code')
    print(excel)
    id_xls=excel.get_rows
    print(id_xls)
