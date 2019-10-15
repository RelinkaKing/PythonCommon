# -*- coding:utf-8 -*-
import os
import xlrd
import os
import json
import traceback
from xml.dom import minidom

import xlwt
import xlrd
from xml.dom.minidom import Document
import codecs
mp3 = "http://down.vesal.cn/vesal_mp3/"
assetbundle = "http://down.vesal.cn/vesal_assetbundle563/"
db = "http://down.vesal.cn/vesal_db/"
xml = "http://down.vesal.cn/vesal_xml563/"
mp4 = "http://down.vesal.cn/vesal_mp4/"
picture = "http://down.vesal.cn/vesal_picture/"

# 遍历 树形文件夹，读取 data.txt 生成最终子节点

os.chdir('.')
for i in os.listdir('./'):
    if "xml" in i:
        print(i)
        doc = minidom.parse(i)
        # get root element
        root = doc.documentElement
        resources = root.getElementsByTagName("resource")
        for resource in resources:
            if not resource.hasAttribute("url"):
                name = resource.getAttribute("name");
                print(name);
                name = name.lower()
                value = ""
                if name.endswith("mp3"):
                    value = mp3
                if name.endswith("assetbundle"):
                    value = assetbundle    
                if name.endswith("db"):
                    value = db
                if name.endswith("xml"):
                    value = xml    
                if name.endswith("mp4"):
                    value = mp4
                if name.endswith("jpg") or name.endswith("png"):
                    value = picture    
                resource.setAttribute("url",value)
        f = open( i , 'w') 
        doc.writexml(f,addindent = ' ',encoding='utf-8')
        f.close()
