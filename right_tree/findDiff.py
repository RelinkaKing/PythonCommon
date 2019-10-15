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
import json

def getNameList(sys):
    doc = minidom.parse(sys)
    # get root element
    root = doc.documentElement
    mainpart = root.getElementsByTagName("AbInfos")
    modelList = []
    for child in mainpart:
        if(child.hasAttribute("name")):
            tmpname = child.getAttribute("name")
            if tmpname not in modelList:
                modelList.append(tmpname)
            else:
                print(sys+" repeat:"+tmpname)
    return modelList
def getDbList():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "mysql", "vesal",charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)
    sql = "SELECT sm_name from xml_submodel "
    cursor.execute(sql)
    datas = cursor.fetchall()
    modelList = []
    for data in datas:
        tmpname = data[0]
        if "PS_" in tmpname or "PS=" in tmpname:
            continue
        if tmpname not in modelList:
            modelList.append(tmpname)
        else:
            print("db repeat:"+tmpname)
    return modelList
def getTreeList():
    doc = minidom.parse("D:\\pythonWorkSpaces\\vesal_right_tree\\SystemTree\\SearchTree.xml")
    # get root element
    root = doc.documentElement
    mainpart = root.getElementsByTagName("model")
    modelList = []
    for child in mainpart:
        if(child.hasAttribute("name")):
            tmpname = child.getAttribute("name")
            if tmpname not in modelList:
                modelList.append(tmpname)
            else:
                print("SearchTree repeat:"+tmpname)
    return modelList
list1 = [1,2,3]
list2 = [2,3,4]
ret = list(set(list1)^set(list2))
# [1, 4]
print(ret)
ret = list(set(list1)|set(list2))
# [1, 2, 3, 4]
print(ret)
ret = list(set(list1)&set(list2))
# [2, 3]
print(ret)
tmpOid = time.strftime('%Y%m%d-%H%M-%S-', time.localtime()) + str(uuid.uuid4())
print(tmpOid)
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org'))

path = os.getcwd()+"\\xml"
xmlList = []
for root ,dirs,files in os.walk(path):
    print(root)
    print(files)
    for file in files:
        tmpList = getNameList(root+"\\"+file)
        xmlList = list(set(xmlList)|set(tmpList))

print("len xmlList:"+str(len(xmlList)))
# dbList = getDbList()
# print("len dbList:"+str(len(dbList)))
rightTree = getTreeList()
print("rightTree dbList:"+str(len(rightTree)))
#交集
ret = list(set(xmlList)&set(rightTree))

xmlRet = list(set(xmlList)^set(ret))
f = open("xmlRet.txt","w")
f.writelines("\n".join(str(i) for i in xmlRet))
f.close()
rightTreeRet = list(set(rightTree)^set(ret))
f = open("rightTreeRet.txt","w")
f.writelines("\n".join(str(i) for i in rightTreeRet))
f.close()
print()