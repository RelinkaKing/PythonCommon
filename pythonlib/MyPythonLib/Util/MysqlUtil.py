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
from MyPythonLib.Util import FileUtil

def getId(tableName,field,value,search=""):
    sql = "SELECT '%s' from '%s' where '%s' = '%s'" % (search,tableName,field,value)
    cursor.execute(sql)
    return cursor.fetchone()
def inserSql(dbCursor,sqlFilePath):
    with open(sqlFilePath,encoding="utf-8") as file:
        line = file.readline()
        createSql=""
        while line:
            #print(line)
            if "CREATE" in line:
                createSql=createSql+line
                line = file.readline()
                continue
            if  createSql != "":
                createSql=createSql+line
            if  createSql != "" and ";" in line:
                cursor.execute(createSql)
                createSql = "";
            if "INSERT" in line or "DROP" in line:
                cursor.execute(line)
            line = file.readline()    
def getNounoList(dbCursor,value):
    sql = "SELECT %s from %s where %s = '%s'"% ("submodel_id","xml_noun_submodel","noun_id",value)
    cursor.execute(sql)
    tmpDatas = cursor.fetchall()
    tmplist =[]
    for data in datas:
        #print("_getNounoList"+str(data))
        tmplist.append(data[0])

def delblankline(infile,outfile,name):
    infopen = open(infile,'r',encoding="utf-8")
    outfopen = open(outfile,'w',encoding="utf-8")
    lines = infopen.readlines()
    for line in lines:
        if line.split():
            if "encoding" in line:
                line = line.replace("<?xml version=\"1.0\" encoding=\"utf-8\"?> <SA>","<SA>")
            if "整体人2.0.4树形结构数据字典" in line:
                line = line.replace("整体人2.0.4树形结构数据字典",name)
            outfopen.writelines(line)
        else:
            outfopen.writelines("")
    infopen.close()
    outfopen.close()

def selectChinese(englishname,cursor):
    sql = "SELECT sm_ch_name from xml_submodel where sm_name = '%s'"% (englishname)
    cursor.execute(sql)
    return cursor.fetchone()

def getXmlWithDifSys(nounoId,modelList,name,cursor,sys):
    doc = minidom.parse("./SystemTree/"+sys)
    # get root element
    root = doc.documentElement
    mainpart = root.getElementsByTagName("model")
    
    for child in mainpart:
        if(child.hasAttribute("name")):
            if  child.getAttribute("name") not in modelList:
                child.parentNode.removeChild(child)
            else:
                child.setAttribute("Chinese",selectChinese(child.getAttribute("name"),cursor)[0])
    isdele = True
    while isdele:
        f = codecs.open("./"+nounoId+".xml",'w','utf-8')
        doc.writexml(f,addindent='  ',newl=' ',encoding = 'utf-8')
        f.close()
        doc = minidom.parse("./"+nounoId+".xml")
        root = doc.documentElement
        isdele = False
        parts = root.getElementsByTagName("part")
        #print(len(parts))
        for part in parts:
            #print(len(part.childNodes))
            if len(part.childNodes) == 1:
                part.parentNode.removeChild(part)
                isdele = True
    f = codecs.open("./"+nounoId+"tmp.xml",'w','utf-8')
    doc.writexml(f,addindent='  ',newl=' ',encoding = 'utf-8')
    f.close()
    sys=sys.replace(".xml","")
    isExists=os.path.exists("./"+sys)
    if not isExists:
        os.makedirs("./"+sys) 
    isExists=os.path.exists("./"+sys+"_1")
    if not isExists:
        os.makedirs("./"+sys+"_1") 
    mainpart = root.getElementsByTagName("model")
    if len(mainpart) != 0:
        delblankline("./"+nounoId+"tmp.xml","./"+sys+"/"+nounoId+".xml",name)
        # delblankline("./"+nounoId+"tmp.xml","./"+sys+"_1/"+nounoId+"_1.xml",name)
        # delblankline("./"+nounoId+"tmp.xml","./"+sys+"_1/"+nounoId+"_2.xml",name)
    os.remove("./"+nounoId+"tmp.xml")
    os.remove("./"+nounoId+".xml")

def getXml(nounoId,modelList,name,cursor):
    for i in os.listdir("./SystemTree"):
        getXmlWithDifSys(nounoId,modelList,name,cursor,i)

def getAbToModelDic():
    AbToModelDic = {}
    for f in os.listdir("./abxml"):
        fn = FileUtil.getFileNameWithOutSuffix(f)
        #print(fn)
        modelList=[]
        doc = minidom.parse("./abxml/"+f)
        # get root element
        root = doc.documentElement
        mainpart = root.getElementsByTagName("AbInfos")
        for p in mainpart:
            modelList.append(p.getAttribute("name"))
        AbToModelDic[fn] = modelList
    return AbToModelDic
def getNounoToAbList():
    naToAbDic = {}
    sql = "SELECT app_id,ab_list from vesal_struct where 1=1"
    cursor.execute(sql)
    datas = cursor.fetchall()
    for data in datas:
        if data and len(data) == 2:
            naToAbDic[data[0]] = data[1].split(",")
    return naToAbDic
def getModelsByNoun(cursor,nouno):
    sql = "SELECT submodel_list from xml_noun where noun_no='{0}'".format(nouno)
    cursor.execute(sql)
    datas = cursor.fetchone()
    if datas:
        tmpDic= json.loads(datas[0])
        return tmpDic.keys()
    else:
        print("error--------------------",nouno)
def getNounoNeedAbs(AbToModelDic,cursor,nouno):
    tmpDic = getModelsByNoun(cursor,nouno)
    ablist = []
    for key in tmpDic:
        for ab in AbToModelDic:
            if key in AbToModelDic[ab]:
                if ab not in ablist:
                    ablist.append(ab)
    return ablist
if __name__ == '__main__':
    time_start=time.time()
    workPath = "D:/pythonWorkSpaces/pythonlib/MyPythonLib/Util/datas"
    os.chdir(workPath)
    # 打开数据库连接
    #db = pymysql.connect("localhost", "root", "mysql", "vesal",charset='utf8')
    db = pymysql.connect("localhost", "root", "mysql", "imgs",charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)
    #os.chdir(".")
    # inserSql(cursor,"./xml_submodel.sql")
    # db.commit()
    # time_end=time.time()
    # print('xml_submodel totally cost',time_end-time_start)

    # time_start=time.time()
    # inserSql(cursor,"./xml_noun.sql")
    # db.commit()
    # time_end=time.time()
    # print('xml_noun totally cost',time_end-time_start)

    # time_start=time.time()
    # inserSql(cursor,"./vesal_struct.sql")
    # db.commit()
    # time_end=time.time()
    # print('vesal_struct totally cost',time_end-time_start)

    # time_start=time.time()
    # inserSql(cursor,"./xml_noun_submodel.sql")
    # db.commit()

    # time_end=time.time()
    # print('xml_noun totally cost',time_end-time_start)
    # time_start=time.time()

    #查询名词Ablist
    # AbToModelDic = getAbToModelDic()

    # print("len AbToModelDic:"+str(len(AbToModelDic)))
    # naToAbDic = getNounoToAbList()
    # print("naToAbDic AbToModelDic:"+str(len(naToAbDic)))

    # sql = "SELECT * from xml_noun where 1=1"
    sql ="SELECT * from imageupload_img where 1=1"
    cursor.execute(sql)
    datas = cursor.fetchall()
    for data in datas:
        print(data)
    # i=0
    # total = len(datas)
    # count = 0
    # for data in datas:
    #     i = i+1
    #     #print(data)
    #     tmpList = []
    #     #sys.stdout.write('\r{2}:Queue Item: {0}\tNumTag:[{1}]'.format(str(data[2]),(i, len(datas)),str(data[1])))
    #     if not data[16]:
    #         continue
    #     tmpDic= json.loads(data[16])
    #     ablist = []
    #     for key in tmpDic.keys():
    #         for ab in AbToModelDic:
    #             if key in AbToModelDic[ab]:
    #                 if ab not in ablist:
    #                     ablist.append(ab)
        
    #     if data[1] in naToAbDic:
    #         subList = list(set(naToAbDic[data[1]]) | set(ablist) )
    #         sub2 = list(set(naToAbDic[data[1]]) ^ set(subList) )
    #         if len(sub2)>0:
    #             count+=1
    #             #print(count,data[1],ablist,naToAbDic[data[1]])
    #             print("update vesal_struct set ab_list = '{0}' where app_id = '{1}'".format(','.join(ablist),data[1]))

        #print(','.join(ablist))

        #tmpList.append(key)
        #getXml(data[1],tmpList,data[2],cursor);
        # for key,value in tmpDic.items():
        #      print(str(key)+":"+str(value))
        #getNounoList(cursor,data[1])
        #break;

            #resources = root.getElementsByTagName("model")

    #getId("xml_noun","noun_no","SA")
    db.commit()
    # 关闭数据库连接
    db.close()
