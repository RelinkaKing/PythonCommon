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
import xlrd
import xlwt

modelname=[]
out_doc = Document()
modellist = out_doc.createElement('EC')
out_doc.appendChild(modellist)
key=[]
rightkey=[]
rightdic={}

def checkSameName():
    xmlname=input("xml name:")
    i=os.listdir('./'+xmlname+'.xml')
    doc=minidom.parse(i)
    root=doc.documentElement
    resources=root.getElementsByTagName("mainpart") 


def rightmenu():
    for i in os.listdir('./'):
        if "rightmenu.xml" in i:
            doc =minidom.parse(i)
            root=doc.documentElement
            resources=root.getElementsByTagName("partition")
            for node in resources:
                partname=node.getAttribute("name")
                types =node.getAttribute("type")
                print(partname+' '+types+' '+i)
                if partname not in rightkey:
                    keys=node.getElementsByTagName("model")
                    if(len(keys)>10):
                        rightkey.append(partname)
                    partele=out_doc.createElement("partition")
                    partele.setAttribute("name",partname)
                    partele.setAttribute("type",types)
                    modellist.appendChild(partele)
                    if(types=='A'):
                        keychild=node.getElementsByTagName("model")
                        for child in keychild:
                            partele.appendChild(child)
                    else:
                        keypart=node.getElementsByTagName("Layered")
                        for layer in keypart:
                            layerele=out_doc.createElement("Layered")
                            layerele.setAttribute('name',layer.getAttribute("name"))
                            partele.appendChild(layerele)
                            layerchild=layer.getElementsByTagName("model")
                            for model in layerchild:
                                layerele.appendChild(model)
    f = open(r'C:\Users\Relinka\Desktop\rightmenu.xml', 'w', encoding='utf-8')
    out_doc.writexml(f, addindent='  ', newl='\n', encoding='utf-8')

def littleMap():
    for i in os.listdir('./'):
        if "littlemap.xml" in i:
            # print(i)
            doc =minidom.parse(i)
            root=doc.documentElement
            resources=root.getElementsByTagName("partition")
            for node in resources:
                partname=node.getAttribute("name")
                if(partname not in key):
                    key.append(partname)
    
    for i in key:
        findOneKey(i)
    f = open(r'C:\Users\Relinka\Desktop\littlemap.xml', 'w', encoding='utf-8')
    out_doc.writexml(f, addindent='  ', newl='\n', encoding='utf-8')

def findOneKey(keyname):
    namecombine=[]
    partList=out_doc.createElement('partition')
    partList.setAttribute("name",keyname)
    modellist.appendChild(partList)
    for i in os.listdir('./'):
        if "littlemap.xml" in i:
            doc =minidom.parse(i)
            root=doc.documentElement
            key_resources=root.getElementsByTagName("partition")#当前 partition的所有子节点
            for node in key_resources:
                partname=node.getAttribute("name")
                if partname == keyname:
                    son_model=node.getElementsByTagName("model")
                    for i in son_model:
                        pinyin =i.getAttribute("name")
                        if(pinyin not in namecombine):
                            namecombine.append(pinyin)
                            partList.appendChild(i)

def modelsToMysql(nodeList,fileName):
    for node in nodeList:
        chinese_name = node.getAttribute("chinese").strip()
        english_name = node.getAttribute("english").strip()
        notes = node.getAttribute("notes").strip()
        notes = notes.replace("\"","'")
        model_name = node.getAttribute("pinyin")
        if(model_name not in modelname):
            modelname.append(model_name)
            modellist.appendChild(node)

def modelCombine():
    for i in os.listdir('./'):
        if "models.xml" in i:
            # print(i)
            doc = minidom.parse(i)
            # get root element
            root = doc.documentElement
            resources = root.getElementsByTagName("SignElement")
            modelsToMysql(resources,i)
            resources = root.getElementsByTagName("model")
            modelsToMysql(resources,i)
    # for i in modellist:

    f = open(r'C:\Users\Relinka\Desktop\models.xml', 'w', encoding='utf-8')
    out_doc.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
    i=0
    for a in modelname:
        print(a+' '+str(i))
        i=i+1
    print(len(modelname))

def compareName():
    str_1=input("firstxml:")
    str_2=input("secondxml:")
    a1=[]
    a2=[]
    for i in os.listdir('./'):
        if str_1 in i:
            doc1 = minidom.parse(i)
            root1 = doc1.documentElement
            resources1 = root1.getElementsByTagName("model")
            for r in resources1:
                name=r.getAttribute("pinyin")
                a1.append(name)
    for i in os.listdir('./'):
        if str_2 in i:
            doc2 = minidom.parse(i)
            root2 = doc2.documentElement
            resources2 = root2.getElementsByTagName("model")
            for r in resources2:
                name=r.getAttribute("pinyin")
                a2.append(name)
    print(len(a1))
    print(len(a2))
    # tmp=[val for val in a1 if val in a2]#交集
    tmp1=set(a2).difference(set(a1))#差集
    print(len(tmp1))
    tmp2=set(a1).difference(set(a2))#差集
    print(len(tmp2))
    # tmp=set(tmp1).intersection(set(tmp2))#交际
    tmp=set(tmp1).union(set(tmp2))
    print(len(tmp))
    file=open(r'C:\Users\Relinka\Desktop\models.txt', 'w')
    for i in tmp:
        file.write(i+'\n')

def combineFileInfo():
    for i in os.listdir('./'):
        print(i)
        

combineFileInfo()
# compareName()
# modelCombine()
# littleMap()
# rightmenu()
# treecombine()