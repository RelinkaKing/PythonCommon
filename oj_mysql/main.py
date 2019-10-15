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
def findModelFromMysql(chineseName):
    sql = "select * from vesal_model_info where chinese_name = '%s'" % chineseName
    cursor.execute(sql)
    data = cursor.fetchone()
    return data
def findLittleMapFromMysql(modelName):
    sql = "select little_map_name,tmp_file_name,chinese_name from vesal_model_info where model_name = '%s'" % modelName
    cursor.execute(sql)
    data = cursor.fetchone()
    return data
def findrightMenuFromMysql(modelName):
    sql = "select right_menu_name,right_menu_type,tmp_file_name,chinese_name from vesal_model_info where model_name = '%s'" % modelName
    cursor.execute(sql)
    data = cursor.fetchone()
    return data
def writeToLog(message):
    with open('../log.txt', 'a+') as f:
        f.write(message)
        f.write("\r\n")
def modelsToMysql(nodeList,fileName):
    for node in nodeList:
        chinese_name = node.getAttribute("chinese").strip()
        english_name = node.getAttribute("english").strip()
        notes = node.getAttribute("notes").strip()
        notes = notes.replace("\"","'");
        model_name = node.getAttribute("pinyin").strip()
        result = findModelFromMysql(chinese_name)
        if result:
            if result[1] == model_name and result[4] == english_name and chinese_name == result[3] and result[5] == notes:
                continue
            #if result[1] != model_name or result[4] != english_name or chinese_name != result[3]:
            #     sql = "exists VALUES('%s','%s','%s','%s');" % (chinese_name,english_name,model_name,fileName)
            #     print(sql)
            #     print("repeat VALUES('%s','%s','%s','%s');" % (result[3],result[4],result[1],result[9]))
            # elif  result[5] != notes:
            #     if result[5] == "":
            #         sql = "UPDATE vesal_model_info set notes = \"%s\" where chinese_name =\"%s\"" % (notes,chinese_name)
            #     elif notes != "":
            #         sql = "exists VALUES('%s',notes:\"%s\",'%s');" % (chinese_name,notes,fileName)
            #         print(sql)
            #         print("repeat VALUES('%s',notes:\"%s\",'%s');" % (result[3],result[5],result[9]))
        #else:
        try:
            sql = "INSERT INTO vesal_model_info(chinese_name,english_name,model_name,notes,tmp_file_name)\
                VALUES('%s','%s','%s',\"%s\",'%s');" % (chinese_name,english_name,model_name,notes,fileName)
            cursor.execute(sql)
        except Exception as e:
            print(sql)
            print(e.with_traceback)
            break;
        # sql = "INSERT INTO vesal_model_info(chinese_name,english_name,little_map_name,model_id,model_name,notes,right_menu_name,right_menu_type,tree_id)\
        #     VALUES(%s,'varchar','varchar','bigint','varchar','text','varchar','varchar','bigint');" %(chinese_name,)
def littleMapToMysql(nodeList,fileName):
    for node in nodeList:
        nodeName = node.getAttribute("name").strip()
        models=node.getElementsByTagName("model")
        for model in models:
            modelName = model.getAttribute("name").strip()
            result = findLittleMapFromMysql(modelName)
            if result and result[0] and result[0] != nodeName:
                writeToLog(modelName+"  "+result[0]+"  "+result[1]+"  "+nodeName+"  "+fileName)
                sql = "INSERT INTO vesal_model_info(little_map_name,model_name,tmp_file_name)\
                    VALUES('%s','%s','%s');" % (nodeName,modelName,fileName)
                cursor.execute(sql)
            else:
                #sqs =[]
                cursor.execute("UPDATE vesal_model_info set little_map_name = '%s' where model_name = '%s'" % (nodeName,modelName))
                cursor.execute("UPDATE vesal_model_info set tmp_file_name = '%s' where model_name = '%s'" % (fileName,modelName))
                #cursor.executemany(sqs)


def rightMenuToMysql(nodeList,fileName):
    for node in nodeList:
        nodeName = node.getAttribute("name").strip()
        rtype = node.getAttribute("type").strip()
        models=node.getElementsByTagName("model")
        for model in models:
            modelName = model.getAttribute("name").strip()
            result = findrightMenuFromMysql(modelName)
            if result and result[0]:
                if result[0] != nodeName or result[1] != rtype:
                    sql = "INSERT INTO vesal_model_info(right_menu_name,right_menu_type,model_name,tmp_file_name)\
                        VALUES('%s','%s','%s','%s');" % (nodeName,rtype,modelName,fileName)
                    cursor.execute(sql)
            else:
                #sqs =[]
                cursor.execute("UPDATE vesal_model_info set right_menu_name = '%s' where model_name = '%s'" % (nodeName,modelName))
                cursor.execute("UPDATE vesal_model_info set right_menu_type = '%s' where model_name = '%s'" % (rtype,modelName))
                cursor.execute("UPDATE vesal_model_info set tmp_file_name = '%s' where model_name = '%s'" % (fileName,modelName))
                #cursor.execute(sql)
                #cursor.executemany(sqs)
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
    if "models.xml" in i:
        print(i)
        doc = minidom.parse(i)
        # get root element
        root = doc.documentElement
        resources = root.getElementsByTagName("SignElement")
        modelsToMysql(resources,i)
        resources = root.getElementsByTagName("model")
        modelsToMysql(resources,i)
print("-------------")
for i in os.listdir('./'):
    if "littlemap.xml" in i:
        print(i)
        doc = minidom.parse(i)
        root = doc.documentElement
        partitions = root.getElementsByTagName("partition")
        littleMapToMysql(partitions,i)
# print("-------------")
# for i in os.listdir('./'):
#     if "rightmenu.xml" in i:
#         print(i)
#         doc = minidom.parse(i)
#         root = doc.documentElement
#         partitions = root.getElementsByTagName("partition")
#         rightMenuToMysql(partitions,i)
        #break
        

# 关闭数据库连接
db.close()