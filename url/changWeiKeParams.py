# -*- coding: utf-8 -*-

import random
import os
import time
import datetime
import json
import re
import FileUtil
import MathUitl
import zipfile

compress_type=zipfile.ZIP_DEFLATED

def changeParams(files):
    for file in files:
        if not "DrawLine" in file:
            print(file)
            operaXml(file)

def operaXml(file):
    docTree = FileUtil.readXmlDoc(file)
    doc = docTree.documentElement
    tmp = MathUitl.vectorStr2List(doc.getAttribute("initCamParentPos"))
    #print(tmp)
    tmp[1] = tmp[1]-1.0
    doc.setAttribute("initCamParentPos",MathUitl.vector2Str(tmp))
    tmp = MathUitl.vectorStr2List(doc.getAttribute("initCamPos"))
    #print(tmp)
    tmp[1] = tmp[1]-1.0
    doc.setAttribute("initCamPos",MathUitl.vector2Str(tmp))
    
    for item in FileUtil.getAllTags(doc,"RecordItem"):
        if item.getAttribute("RecordAction") == "camPos":
            tmp = MathUitl.vectorStr2List(item.getAttribute("raParams"))
            tmp[1] = tmp[1]-1.0
            item.setAttribute("raParams",MathUitl.vector2Str(tmp))
    FileUtil.writeXml(docTree,file)

tp = os.getcwd()+"/download/WK/"
tpr = os.getcwd()+"/download/WK/result/"
if not os.path.isdir(tpr):
    os.mkdir(tpr)

for file in  FileUtil.getFilesInDir(tp,True,[".vsl"]):
    print(file)
    tmpName = FileUtil.getFileNameWithOutSuffix(file)
    tmpPath = FileUtil.getFilePath(file)
    targetPath = tmpPath+"/"+tmpName
    FileUtil.un_zip(file,targetPath,compression=compress_type)
    
    #print(targetPath)
    recFiles= FileUtil.getFilesInDir(targetPath,True,[".rec"])
    changeParams(recFiles)

    files = FileUtil.getFilesInDir(targetPath)
    FileUtil.zip(files,tpr+ FileUtil.getFileName(file),targetPath,compress_type=compress_type)

    FileUtil.DeleDir(targetPath)
    #break