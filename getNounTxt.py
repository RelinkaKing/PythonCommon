# -*- conding:utf-8 -*-
import codecs
import json
import os
import re
import sys
import time
import traceback
import uuid
from datetime import datetime
from xml.dom import minidom
from xml.dom.minidom import Document

import pymysql
import xlrd
import xlwt
import urllib
import urllib.request


# test_data = {'ServiceCode':'aaaa','b':'bbbbb'}
# test_data_urlencode = urllib.urlencode(test_data)

# requrl = "http://192.168.81.16/cgi-bin/python_test/test.py"

# req = urllib2.Request(url = requrl,data =test_data_urlencode)
# print req

# res_data = urllib2.urlopen(req)
# res = res_data.read()
# print res




def writeXml(subInfoList):
    f = open("result.txt",'w',encoding='utf-8')
    
    for row in subInfoList:
        f.write(row["nounName"])
        print(row["nounName"])
        f.write("\n")
    f.flush()
    f.close()


url = "http://118.24.119.234/vesal-jiepao/v1/app/xml/getNoun?Version=1"
req=urllib.request.urlopen(url)
result = req.read()
str1=str(result, encoding = "utf-8")  
data=eval(str1)
print(data['List'])
writeXml(data['List'])
# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "mysql", "vesal",charset='utf8')

# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print("Database version : %s " % data)
