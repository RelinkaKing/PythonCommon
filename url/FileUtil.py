# -*- coding: utf-8 -*-

import random
import os
import time
import datetime
import json
import re
import http.client
import requests 
import zipfile
import lzma
from xml.dom.minidom import Document
from xml.dom.minidom import parse
import xml.dom.minidom
import uuid
import shutil
def getUUID():
    return str(uuid.uuid1())

def readXmlDoc(xmlPath):
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(xmlPath)
    #DOMTree.documentElement
    return DOMTree

def getAllTags(doc,tagName):
    return doc.getElementsByTagName(tagName)

def writeXml(doc,file,indent="\t"):  
    #indent = '\t'
    # xml_str = 
    # repl = lambda x: ">%s</" % x.group(1).strip() if len(x.group(1).strip()) != 0 else x.group(0)
    # pretty_str = re.sub(r'>\n\s*([^<]+)</', repl, str(xml_str))
    tmpFileName = file+getUUID()
    with open(tmpFileName, 'wb') as f:
        f.write(doc.toprettyxml(indent=indent, encoding='utf-8'))
    if os.path.isfile(file):
        os.remove(file)
    delblankline(tmpFileName,file)
    if os.path.isfile(tmpFileName):
        os.remove(tmpFileName)
    

def delblankline(infile,outfile):
    infopen = open(infile,'r')
    outfopen = open(outfile,'w')
    lines = infopen.readlines()
    for line in lines:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")
    infopen.close()
    outfopen.close()
    

def un_zip(file_name,targetPath="",pwd=None,isOverWrite = True,compression=zipfile.ZIP_STORED):
    """unzip zip file"""
    if targetPath == "":
        tmpName = getFileNameWithOutSuffix(file_name)
        tmpPath = getFilePath(file_name)
        targetPath = tmpPath+"/"+tmpName
    #ZIP_LZMA
    zip_file = zipfile.ZipFile(file_name,compression=compression)

    
    targetPath = targetPath.replace("\\","/")
    if os.path.isdir(targetPath):
        pass
    else:
        os.mkdir(targetPath)
    if not targetPath.endswith("/"):
        targetPath = targetPath+"/"
    for names in zip_file.namelist():
        names = names.replace("\\","/")
        tmpZipFileName = names
        try:
            tmpZipFileName = tmpZipFileName.encode('cp437').decode('gbk')
        except:
            tmpZipFileName = tmpZipFileName.encode('utf-8').decode('utf-8')
        member = targetPath+tmpZipFileName
        if names[-1] == '/':
            if not os.path.isdir(member):
                os.mkdir(member)
        else:
            if os.path.isfile(member):
                if isOverWrite:
                    os.remove(member)
                else:
                    continue
            with zip_file.open(names, pwd=pwd) as source, \
                open(member, "wb") as target:
                shutil.copyfileobj(source, target)
    zip_file.close()
def zip(files,tartgetZip,replaceRootPath = "",compress_type=zipfile.ZIP_STORED):
    tmpPath = getFilePath(tartgetZip)
    if not os.path.isdir(tmpPath):
        os.mkdir(tmpPath)
    # 新建压缩包，放文件进去,若压缩包已经存在，将覆盖。可选择用a模式，追加
    azip = zipfile.ZipFile(tartgetZip, 'w')
    # 必须保证路径存在,将bb件夹（及其下aa.txt）添加到压缩包,压缩算法LZMA
    for file in files:
        azip.write(file,file.replace(replaceRootPath,""), compress_type=compress_type)
    # 写入一个新文件到压缩包中，data是该文件的具体内容，可以是str或者是byte。
    # 这里是新建一个bb文件夹，其下再新建一个cc.txt,将hello world写入到文本中
    #azip.writestr('bb/cc.txt', data='Hello World', compress_type=zipfile.ZIP_DEFLATED)
    # 关闭资源
    azip.close()
def getFilesInDir(dirPath,isRecursion=True,suffixFilter=[]):
    # for x,y,z in  os.walk("./download/"):
    #     #print(x+"  "+y+"  "+z)
    #     # print(x)
    #     # print(y)
    #     # print(z)
    #     tmpPath = x.replace("\\","/")
    #     if not tmpPath.endswith("/"):
    #         tmpPath = tmpPath+"/"
    #     for file in z:
    #         print(tmpPath+file)

    files = []
    dirPath = dirPath.replace("\\","/")
    if not dirPath.endswith("/"):
        dirPath = dirPath+"/"
    if os.path.isdir(dirPath):
        for x in os.listdir(dirPath):
            if os.path.isdir(dirPath+x) and isRecursion:
                files.extend(getFilesInDir(dirPath+x,isRecursion,suffixFilter))
            else:
                if suffixFilter == [] or  getFileSuffix(x).lower() in suffixFilter:
                    files.append(dirPath+x)
    return files
def DeleDir(dirPath):
    try:
        shutil.rmtree(dirPath)
    except:
        pass
def downLoadFile(url,targetPath):
    print("start Download:"+url)
    r = requests.get(url) 
    with open(targetPath, "wb") as code:
        code.write(r.content)
    print("down!")

def getFileName(url):
    # (filepath,tempfilename) = os.path.split(filename);
    # (shotname,extension) = os.path.splitext(tempfilename);
    _,name= os.path.split(url)
    return name
def getFileNameWithOutSuffix(url):
    # (filepath,tempfilename) = os.path.split(filename);
    _,name= os.path.split(url)
    shotname,extension = os.path.splitext(name)
    return shotname
def getFileSuffix(name):
    shotname,extension = os.path.splitext(name)
    return extension
def getUrlSuffix(url):
    _,name= os.path.split(url)
    return getFileSuffix(name)
def getFilePath(url):
    path,name= os.path.split(url)
    return path

class FileUtil:
    def __init__(self, *args, **kwargs):
            return super().__init__(*args, **kwargs)

