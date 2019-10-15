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

def writeToLog(message):
    with open('../log.txt', 'a+') as f:
        f.write(message)
        f.write("\r\n")
def getId(nodeName):
    sql = "SELECT tree_id from vesal_model_tree where node_name = '%s'" % (nodeName)
    cursor.execute(sql)
    return cursor.fetchone()

def getAllInfo(nodeName):
    sql = "SELECT * from vesal_model_tree where node_name = '%s'" % (nodeName)
    cursor.execute(sql)
    return cursor.fetchone()

def getParentName(nodeName):
    sql = "SELECT parent_node_name from vesal_model_tree where node_name = '%s'" % (nodeName)
    cursor.execute(sql)
    return cursor.fetchone()

def insertNode(nodeName,parentName):
    sql = "INSERT INTO vesal_model_tree(node_name,parent_node_name) VALUES('%s','%s')" % (nodeName,parentName)
    cursor.execute(sql)
def isExist(nodeName):
    if getId(nodeName):
        return True
    else:
        return False
def findParent(node):
        if not node.parentNode:
            return
        nodeName = node.getAttribute("name").strip()
        tagName = node.tagName
        if tagName == "mainpart":
            if not isExist(nodeName):
                insertNode(nodeName,"-")
            return nodeName
        elif tagName == "part":
            parentName = findParent(node.parentNode)
            if not isExist(nodeName):
                insertNode(nodeName,parentName)    
            else:
                data = getAllInfo(nodeName)
                if data[1] != nodeName or data[2] != parentName:
                    print(data)
                    print(nodeName,parentName)
            return nodeName
        elif tagName == "model":
            parentName = findParent(node.parentNode)
            if not parentName:
                print(str(node),"---------------=")
                print(nodeName)
                print(node.parentNode.tagName)
            if not isExist(nodeName):
                insertNode(nodeName,parentName)
            else:
                data = getAllInfo(nodeName)
                if data[1] != nodeName or data[2] != parentName:
                    print(data,"$$$$$$")
                    print(nodeName,parentName)
        else:
            print(nodeName,tagName)
#def treeToMysql(nodeList,fileName):
    #for node in nodeList:
        #node.


# 打开数据库连接
db = pymysql.connect("localhost", "root", "mysql", "vesal",charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print("Database version : %s " % data)

# sql = "SELECT chinese_name,english_name,model_name,notes,tmp_file_name FROM vesal_model_info where model_name=\"ZhuDongMaiGong\""
# cursor.execute(sql)
# data = cursor.fetchall()
# print(str(data[0]))
# print(str(data[1]))
# print(data[0][0] == data[1][0])
# print(data[0][1] == data[1][1])
# print(data[0][2] == data[1][2])
# print(data[0][3] == data[1][3])
os.chdir('./整体人文案')
for i in os.listdir('./'):
    if "Sport.xml" in i:
        print(i)
        doc = minidom.parse(i)
        # get root element
        root = doc.documentElement
        models = root.getElementsByTagName("model")
        for model in models:
            findParent(model)
            #sys.exit(0)


# 关闭数据库连接
db.close()