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
import mysql
import xl's
import json

editlist=[]
isEdit = True
def selectChinese(englishname,cursor):
    sql = "SELECT sm_ch_name from xml_submodel where sm_name = '%s'"% (englishname)
    cursor.execute(sql)
    return cursor.fetchone()

def editRepeat(parentNode,name,i):
    if parentNode.getAttribute("name") == name:
        if i not in editlist:
            editlist.append(i)
        isEdit = True
        parentNode.setAttribute("name",name+" ")
    if parentNode.tagName != "mainpart":
        editRepeat(parentNode.parentNode,name,i)

print("start")
# 打开数据库连接
db = mysql.connect("localhost", "root", "mysql", "vesal",charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print("Database version : %s " % data)

def EditRepeatXml(i):
    doc = minidom.parse(i)
    root = doc.documentElement
    models = root.getElementsByTagName("model")
    for model in models:
        #print(model.getAttribute("name"))
        tmpData = selectChinese(model.getAttribute("name"),cursor)
        if tmpData:
            model.setAttribute("Chinese",tmpData[0])
        else:
            model.parentNode.removeChild(model)

    #删除空part
    isEdit = True
    while isEdit:
        f = codecs.open(i,'w','utf-8')
        doc.writexml(f,addindent='  ',newl=' ',encoding = 'utf-8')
        f.close()
        doc = minidom.parse(i)
        root = doc.documentElement
        isEdit = False
        parts = root.getElementsByTagName("part")
        #print(len(parts))
        for part in parts:
            #print(len(part.childNodes))
            if len(part.childNodes) == 1:
                part.parentNode.removeChild(part)
                isEdit = True

    #model 中文名 父节点重复名字加空格
    isEdit = True
    while isEdit:
        f = codecs.open(i,'w','utf-8')
        doc.writexml(f,addindent='  ',newl=' ',encoding = 'utf-8')
        f.close()
        doc = minidom.parse(i)
        root = doc.documentElement
        isEdit = False
        models = root.getElementsByTagName("model")
        for model in models:
            editRepeat(model.parentNode,model.getAttribute("Chinese"),i)

    #替换part父节点重复名
    isEdit = True
    while isEdit:
        f = codecs.open(i,'w','utf-8')
        doc.writexml(f,addindent='  ',newl=' ',encoding = 'utf-8')
        f.close()
        doc = minidom.parse(i)
        root = doc.documentElement
        isEdit = False
        parts = root.getElementsByTagName("part")
        #print(len(parts))
        for part in parts:
            #print(len(part.childNodes))
            editRepeat(model.parentNode,model.getAttribute("name"),i)

    f = codecs.open(i,'w','utf-8')
    doc.writexml(f,addindent='  ',newl=' ',encoding = 'utf-8')
    f.close()


time_start=time.time()
files = os.listdir("./XML结构最终版")
i = 0
for f in files:
    i = i+1
    print("%d / %d" % (i,len(files)))
    try:
        EditRepeatXml("./XML结构最终版/"+f)
    except BaseException as e:
        print(f)
        print(e)

time_end=time.time()
print('totally cost',time_end-time_start)

print("done")
print(editlist)