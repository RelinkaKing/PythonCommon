# -*- coding: utf-8 -*-

import random
import os
import time
import datetime
import json
import re
import http.client
import requests 
from MyPythonLib.Util import RequestUtil,JsonUtil,FileUtil
from MyPythonLib.Util.Sqlite3Util import MySqlite3
import sys,shutil

def insertIntoTable(tableName,version,List,db):
    cout = 0
    sumLen = len(List)
    res = db.querry("PRAGMA  table_info('{0}')".format(tableName))
    fileds = []
    popfileds=[]
    for x in res:
        fileds.append(x[1])
    process = -1
    for item in List:
        if popfileds == []:
            for key in item:
                if key not in fileds:
                    popfileds.append(key)
                    print("多余字段:",tableName,key)
        for key in popfileds:
            item.pop(key)
        try:
            sql,objs = db.get_i_sql(tableName,dict(item))
            db.executeWithObjs(sql,objs)
        except BaseException as e:
            print(e)
            print(sql)
            sys.exit(0)
        cout = cout+1
        tmpP = cout/sumLen *100
        if tmpP != process:
            process=tmpP
            x=">"
            # 输出的时候加上'\r'可以让光标退到当前行的开始处，进而实现显示进度的效果
            for r in range(0,100,1):
                if r <process:
                    x=x+">"
                else:
                    x=x+" "
            sys.stdout.write('\r{0}: \tProcess:[{1}]'.format(tableName,x))
    sql = "insert into {0} values('{1}',{2})".format("TableVersions",tableName,version)
    db.execute(sql)
    print("\r\n")
    print(tableName,version)
    print("\r\n")

#response =RequestUtil.getResponse("api.vesal.cn","/vesal-jiepao-prod/v1/app/struct/initMyStruct?token=1&plat=android&fyId=2&version=1",port=8000)
#print(response["List"])
#测验练习
#微课课程
# for x in response["List"]:
#     if x["dict_name"] == "测验练习":
#         for Struct in x["StructList"]:
#             print(Struct["app_version"])
#             ab_path = Struct["ab_path"]
#             print(ab_path)
            #FileUtil.downLoadFile(ab_path,"./download/"+FileUtil.getFileName(ab_path))
#print(data.decode("utf-8"))

#get_server_interface = "http://api.vesal.cn:8000/vesal-jiepao-prod/server?type=0" 
get_server_interface = "http://118.24.119.234:8083/vesal-jiepao-test/server?type=0"
response =RequestUtil.getResponse("118.24.119.234","/vesal-jiepao-test/server?type=0",port=8083)
fix_server_interface = "v1/app/member/getCode";
servlet = "v1/app/xml/"
commonfile = "v1/app/struct/getCommonFile"
tableApis = ["getAllAssHide","getNoun","getSubModel","getNounSubModel","getAllLayerSubmodel","getAllRightMenu","getAllRightMenuLayer","v1/app/struct/getCommonFile"]
tableNames=['ModelRelationModel','GetStructList','GetSubModel','GetNounSubModel','LayserSubModel','RightMenuModel','RightMenuLayerModel','CommonAssetLib']
#('Abfiles',)
#('TableVersions',)

uri = "";
for x in response:
    if x == "List":
        uri = response[x][0]['server']

serverip = uri

downloadpath="D:/pythonDownload/vesali.db"
if not os.path.isfile(downloadpath):
    shutil.copyfile("C:/Users/Administrator/AppData/LocalLow/Vesal/ruanyikeji_vesal_vesal/db/vesali.db",downloadpath)
localDb = MySqlite3(downloadpath)

alltablesql = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
rows = localDb.querry(alltablesql)
for row in rows:
    localDb.resetTable(row[0])
localDb.resetTable("TableVersions")
localDb.resetTable("Abfiles")
localDb.commit()
for i in range(0,len(tableApis),1):
    if "v1" in tableApis[i]:
        uri = serverip+tableApis[i]
    else:
        uri = serverip+servlet+tableApis[i]
    print(uri)
    uri = uri +"?Version=-1"
    jsondata = RequestUtil.getJson(uri)
    insertIntoTable(tableNames[i],jsondata["maxVersion"],jsondata["List"],localDb)
    localDb.commit()
        
#for x in  jsondata["List"]:
#    print(x["platform"],x["version"],x["url"])

sql = "select * from CommonAssetLib"
rows = localDb.querry(sql)
fileRecord = None
path = FileUtil.getFilePath(downloadpath)

if os.path.isfile(path+"/fileRecord.json"):
    fileRecord = JsonUtil.readJsonFromFile(path+"/fileRecord.json")
fileSum = len(rows)
count = 0
for x in rows:
    count += 1
    print("{0} / {1}".format(count,fileSum))
    targetFile=path+"/download/"+x[5]+"/"+x[1]
    print(targetFile)
    if fileRecord:
        if fileRecord[x[5]][x[1]] == x[3] and os.path.isfile(targetFile):
            print(x," skip!")
            continue
    FileUtil.downLoadFile(x[2],targetFile+".tmp")
    if os.path.isfile(targetFile):
        os.remove(targetFile)
    shutil.move(targetFile+".tmp",targetFile)

downloadRecordJson = {'pc':{},'ios':{},'android':{}}
for x in rows:
    print(x)
    downloadRecordJson[x[5]][x[1]]=x[3]

JsonUtil.wirteJsonToFile(downloadRecordJson,path+"/fileRecord.json")
for x in downloadRecordJson:
    JsonUtil.wirteJsonToFile(downloadRecordJson[x],path+"/fileRecord_"+x+".json")
#print(JsonUtil.readJsonFromFile(path+"/fileRecord.json")['pc']['mp3.zip'])

exportPath=path+"/export"
if os.path.isdir(exportPath):
    FileUtil.DeleDir(exportPath)

exportPath = exportPath+"/"

playformDb={}
for x in downloadRecordJson:
    tmpPath=exportPath+x+"/db"
    if not os.path.isdir(tmpPath):
        os.makedirs(tmpPath)
    shutil.copyfile(downloadpath,tmpPath+"/"+FileUtil.getFileName(downloadpath))
    playformDb[x] = tmpPath+"/"+FileUtil.getFileName(downloadpath)
count = 0
for x in rows:
    count += 1
    print("{0} / {1}".format(count,fileSum))
    targetFile=path+"/download/"+x[5]+"/"+x[1]
    if os.path.isfile(targetFile):
        tmpPath = exportPath+x[5]+"/"+x[1]
        if tmpPath.endswith("assetbundle"):
            # 以字节只读模式打开图片文件
            iFile = open(targetFile, "rb")
            iBytes = iFile.read()
            # print(iBytes)
            bFile = open(tmpPath, "xb")
            head = iBytes[0:1024]
            print(len(head))
            sql = "insert into Abfiles values(?,?)"
            objects=[]
            objects.append(x[1])
            objects.append(head)
            tmpdb = MySqlite3(playformDb[x[5]])
            tmpdb.executeWithObjs(sql,objects)
            tmpdb.commit()
            tmpdb.closeDb()

            byteCount = bFile.write(iBytes[1024:])
            bFile.close()
            iFile.close()
            pass
        if tmpPath.endswith("zip"):
            FileUtil.un_zip(targetFile,FileUtil.getFilePath(tmpPath))
            pass



localDb.closeDb()