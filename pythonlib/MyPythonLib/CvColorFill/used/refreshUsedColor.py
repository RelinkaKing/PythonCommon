# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
import PIL.Image as Image
import matplotlib.pylab as plt
import scipy.misc
import random
import os
from PIL import ImageFont,ImageDraw
from xml.dom.minidom import Document
import datetime
import json
import re
import xlwt
from xlwt import Workbook
import xlrd

print(os.getcwd())

def getTupleFromStr(tstr):
    #t = re.sub("\D", ",",tstr).split(',')
    return tuple(int(x) for x in re.findall(r"\d+",tstr))

filterColorList=[]
config_dict={}
with open("config.json",'r') as load_f:
    config_dict = json.load(load_f)
    getListFromDic = lambda tmpDic : [getTupleFromStr(tmpDic[key]) for key in tmpDic]
    filterColorList = getListFromDic(config_dict["FilterColor"])
    #dict(zip(getKeys(self.randomColorList),itemToString(self.randomColorList)))

filterColorListText=[]
itemToString = lambda tmpList: [str(x) for x in tmpList]

for i in os.listdir("usedColor"):
    print(i)
    book = xlrd.open_workbook("./usedColor/"+i)
    while not book.sheet_loaded(0):
        pass
    table = book.sheet_by_index(0)

    for x in table.col(1,start_rowx=1):
        if x in filterColorListText:
            print("warnning repeat:"+x)
        else:
            #help(x)
            filterColorListText.append(x.value)

for n in filterColorList:
    if n in filterColorListText:
        print("warnning repeat:"+n)
    else:
        #help(x)
        filterColorListText.append(n)

getKeys = lambda tmpList: [x for x in range(1,len(tmpList)+1,1)]
config_dict["FilterColor"] = dict(zip(getKeys(filterColorListText),itemToString(filterColorListText)))

print(config_dict["FilterColor"])

with open("config.json","w") as f:
    json.dump(config_dict,f,indent="\t")