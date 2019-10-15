# -*- coding: utf-8 -*-

import random
import os
import time
import datetime
import json
import re
import http.client
import requests 
from MyPythonLib.Util import RequestUtil,JsonUtil,FileUtil,MysqlUtil,MathUtil,ReUtil

from MyPythonLib.Util.Sqlite3Util import MySqlite3
import sys,shutil
import pymysql

def operaXml(file,num):
    docTree = FileUtil.readXmlDoc(file)
    doc = docTree.documentElement
    tmp = MathUtil.vectorStr2List(doc.getAttribute("initCamParentPos"))
    #print(tmp)
    tmp[1] = tmp[1]+num
    doc.setAttribute("initCamParentPos",MathUtil.vector2Str(tmp))
    tmp = MathUtil.vectorStr2List(doc.getAttribute("initCamPos"))
    #print(tmp)
    tmp[1] = tmp[1]+num
    doc.setAttribute("initCamPos",MathUtil.vector2Str(tmp))
    
    for item in FileUtil.getAllTags(doc,"RecordItem"):
        if item.getAttribute("RecordAction") == "camPos":
            tmp = MathUtil.vectorStr2List(item.getAttribute("raParams"))
            tmp[1] = tmp[1]+num
            item.setAttribute("raParams",MathUtil.vector2Str(tmp))
    FileUtil.writeXml(docTree,file)

def downloadWeiKe():
    conn = http.client.HTTPConnection('api.vesal.cn', port=8000, timeout=10)
    headers = {
        'Cache-Control': "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
        }
    conn.request("GET","/vesal-jiepao-prod/v1/app/struct/initMyStruct?token=1&plat=android&fyId=2&version=1&Timestamp="+str(int(time.time())),headers=headers)
    # 得到返回的 http response
    r1 = conn.getresponse()
    # HTTP 状态码
    print(r1.status,r1.reason)
    # HTTP 头部
    print(r1.getheaders())
    # body 部分
    response = json.loads(r1.read().decode("utf-8")) 
    conn.close()
    #print(response["List"])
    #测验练习
    #微课课程
    for x in response["List"]:
        if x["dict_name"] == "测验练习":
            for Struct in x["StructList"]:
                print(Struct["app_version"])
                ab_path = Struct["ab_path"]
                print(ab_path)
                #FileUtil.downLoadFile(ab_path,"./download/"+FileUtil.getFileName(ab_path))

workPath = "D:/pythonWorkSpaces/pythonlib/MyPythonLib/Util/datas"
os.chdir(workPath)

# needAbList={}
#   # 打开数据库连接
# db = pymysql.connect("localhost", "root", "mysql", "vesal",charset='utf8')
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print("Database version : %s " % data)
# AbToModelDic = MysqlUtil.getAbToModelDic()

# print("len AbToModelDic:"+str(len(AbToModelDic)))

# for file in FileUtil.getFilesInDir("./weike"):
#     needNouns=[]
#     # if ".vsl" in file:
#     #     FileUtil.un_zip(file)
#     if "control.xml" == FileUtil.getFileName(file):
#         wkid = FileUtil.getFilePath(file)
#         wkid = FileUtil.getFileName(wkid)
#         print(wkid)
#         docTree = FileUtil.readXmlDoc(file)
#         Models = FileUtil.getAllTags(docTree,"Model")

#         for Model in Models:
#             noun = Model.getAttribute("modelId")
#             if noun not in needNouns:
#                 needNouns.append(noun)
#         print(needNouns)        
#         for nouno in needNouns:
#             ablist=MysqlUtil.getNounoNeedAbs(AbToModelDic,cursor,nouno)
#             #print(nouno,ablist)
#             # sql = "SELECT ab_list from vesal_struct where app_id = '{0}'".format(nouno)
#             # cursor.execute(sql)
#             # datas = cursor.fetchone()
#             # if datas:
#             #     print(datas[0])
#             # else:
#             #     print(nouno)
        
#             if wkid not in needAbList:
#                 needAbList[wkid] = ablist
#             else:
#                 needAbList[wkid] = MathUtil.andSet(needAbList[wkid],ablist)

#         # sql = "SELECT struct_name,app_id from vesal_struct where struct_name = '{0}'".format(struct_name)
#         # cursor.execute(sql)
#         # datas = cursor.fetchone()
#         # print(data[1])
#         # print()

#         #<Model shapeId="0" id="0" appearTime="0.03291981" endTime="61.48347" Filename="3.rec" x="13.41354" y="107.1198" w="514.6544" h="406.516" modelId="SA0101025">

# for wkid in needAbList:
#     print(wkid,needAbList[wkid])
# for wkid in needAbList:
#     restr = ".*(第.?讲).*"
#     stname = ReUtil.search(wkid,restr)[0]
#     sql = "SELECT app_id from vesal_struct where struct_name like '%{0}%'".format(stname)
#     cursor.execute(sql)
#     datas = cursor.fetchone()
#     if datas:
#         print("update vesal_struct set ab_list = '{0}' where app_id = '{1}'".format(','.join(needAbList[wkid]),datas[0]))

# # 关闭数据库连接
# db.close()

for file in FileUtil.getFilesInDir("./weike"):
    if ".rec" in file and "DrawLine" not in file:
        restr = ".*(第.?讲).*"
        stname = ReUtil.search(file,restr)[0]
        #print(stname)
        pn="-1"
        try:
            restr = ".*/([\d.?])/.*"
            pn = ReUtil.search(file,restr)[0]
        except:
            pass
        if stname == "第七讲" and pn == "6":
            #print(pn)
            print(file)
            operaXml(file,0.055)
            print("down!")
            break