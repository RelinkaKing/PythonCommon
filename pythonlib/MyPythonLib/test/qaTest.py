# -*- coding: utf-8 -*-

import random
import os
import time
import datetime
import json
import re
import http.client
import requests 
from MyPythonLib.Util import RequestUtil,JsonUtil,FileUtil,MysqlUtil,MathUtil
from MyPythonLib.Util.Sqlite3Util import MySqlite3
import sys,shutil

def downloadQaZipAndCompareMd5():
    dic1 = {}
    response =RequestUtil.getResponse("api.vesal.cn","/vesal-jiepao-prod/v1/app/struct/initMyStruct?token=1&plat=android&fyId=2&version=1",port=8000)
    #http://118.24.119.234:8083/vesal-jiepao-test/server?type=0
    #print(response["List"])
    #测验练习
    #微课课程
    for x in response["List"]:
        if x["dict_name"] == "测验练习":
            for Struct in x["StructList"]:
                #print(Struct["app_version"])
                ab_path = Struct["ab_path"]
                print(ab_path)
                filePath = "./download/"+FileUtil.getFileName(ab_path)
                FileUtil.downLoadFile(ab_path,filePath)
                if os.path.isfile(filePath):
                    md5 = FileUtil.getMd5(filePath)
                    print(FileUtil.getFileName(ab_path),md5)
                    dic1[FileUtil.getFileName(ab_path)]=md5
    #print(data.decode("utf-8"))


    response =RequestUtil.getResponse("118.24.119.234","/vesal-jiepao-test/v1/app/struct/initMyStruct?token=1&plat=android&fyId=2&version=1",port=8083)
    #print(response["List"])
    #测验练习
    #微课课程
    for x in response["List"]:
        if x["dict_name"] == "测验练习":
            for Struct in x["StructList"]:
                #print(Struct["app_version"])
                ab_path = Struct["ab_path"]
                #print(ab_path)
                filePath = "./download/teset/"+FileUtil.getFileName(ab_path)
                FileUtil.downLoadFile(ab_path,filePath)
                if os.path.isfile(filePath):
                    md5 = FileUtil.getMd5(filePath)
                    print(FileUtil.getFileName(ab_path),md5)
                    dic1["test_"+FileUtil.getFileName(ab_path)]=md5

    for i in range(0,10,1):
        print("================="+str(i)+"======================")
        for key in dic1:
            if str(i)+".zip" in key:
                print(dic1[key])
        print("===========================================")

workPath = "D:/pythonWorkSpaces/pythonlib/MyPythonLib/Util/datas"
os.chdir(workPath)
#downloadQaZipAndCompareMd5

# for i in os.listdir('./download'):
#     file = "D:/pythonWorkSpaces/pythonlib/MyPythonLib/Util/datas/download/"+i
#     if ".zip" in file:
#         FileUtil.un_zip(file)
abModlDic = MysqlUtil.getAbToModelDic()
print(len(abModlDic))
needAbList={}
for file in FileUtil.getFilesInDir("./download"):
    if "lib" in file:
        print(file)
        qaid = FileUtil.getFilePath(file)
        qaid = FileUtil.getFileName(qaid)
        print(qaid)
        docTree = FileUtil.readXmlDoc(file)
        hls = FileUtil.getAllTags(docTree,"highLightName")
        needModels = []
        for hl in hls:
            #help(hl.ownerDocument)
            hlobj = json.loads(hl.firstChild.data)
            
            for key in hlobj["keys"]:
                if key not in  needModels:
                    needModels.append(key)
        
        ablist = []
        for model in needModels:
            finded = False
            for ab in abModlDic:
                if model in abModlDic[ab]:
                    if finded:
                        print("----repeat:"+model)
                    if ab not in ablist:
                        ablist.append(ab)
                        finded = True
                        
        if qaid not in needAbList:
            needAbList[qaid] = ablist
        else:
            needAbList[qaid] = MathUtil.andSet(needAbList[qaid],ablist)
        #break

for nab in needAbList:
    #print(nab,','.join(needAbList[nab]))
    print("update vesal_struct set ab_list = '{0}' where app_id = '{1}'".format(','.join(needAbList[nab]),nab))

