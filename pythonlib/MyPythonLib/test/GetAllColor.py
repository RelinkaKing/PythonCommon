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
from MyPythonLib.Util import FileUtil
import xlrd

def saveAllColor(inputPath,outputPath):
    image = cv.imread(inputPath)
    usedColor = []
    w,h =image.shape[:2]
    for i in range(0,w,1):
        for j in range(0,h,1):
            transTuple = lambda x : (x[2],x[1],x[0])
            tmpColor = transTuple(tuple(image[i,j]))
            if tmpColor not in usedColor:
                usedColor.append(tmpColor)
    writeToExcel(outputPath,usedColor)
def writeToExcel(outputPath,colros):
    book = Workbook(encoding='utf-8')
    sheet1 = book.add_sheet("default",cell_overwrite_ok=True)
    count = 0
    sheet1.write(0,0,"Id")
    sheet1.write(0,1,"Color(rgb)")
    sheet1.write(0,2,"ColorBlock")
    sheet1.write(1,0,"Id")
    sheet1.write(1,1,"Color(rgb)")
    sheet1.write(1,2,"ColorBlock")
    tmpPngPath = "tmpcc.bmp"
    rowCount = 2
    for color in colros:
        tmpColor = color
        #tmpColor = (tmpColor[2],tmpColor[1],tmpColor[0])
        im = Image.new("RGB",(50,20),tmpColor)
        im.save(tmpPngPath,"bmp")
        sheet1.write(rowCount,0,str(count))
        sheet1.write(rowCount,1,str(tmpColor))
        sheet1.insert_bitmap(tmpPngPath,rowCount,2)
        count = count+1
        rowCount= rowCount+1
    os.remove(tmpPngPath)
    # 保存Excel book.save('path/文件名称.xls')
    book.save(outputPath)
    return


if __name__ == '__main__':
    # workPath = "D:/pythonWorkSpaces/pythonlib/MyPythonLib/Util/datas"
    # os.chdir(workPath)

    suffix = [".png",".jpg"]
    for file in os.listdir('./'):
        if  FileUtil.getFileSuffix(file).lower() in suffix:
            print(file)
            #FileUtil.getFilePath(file) + 
            outputPath = FileUtil.getFileNameWithOutSuffix(file) + "_result.xls"
            saveAllColor(file,outputPath)


    usedColor = []
    for i in os.listdir("./"):
        #print(i)
        if "result" in i and ".xls" in i:
            book = xlrd.open_workbook(i)
            while not book.sheet_loaded(0):
                pass
            table = book.sheet_by_index(0)

            for x in table.col(1,start_rowx=1):
                
                usedColor.append(tuple(int(x) for x in re.findall(r"\d+",x.value)))
                #print(x.value)

    usedColor.append((0,0,0))
    for i in os.listdir("./"):
        #print(i)
        if "result" in i and ".xls" in i:
            pass
        elif ".xls" in i:
            book = xlrd.open_workbook(i)
            table = book.sheet_by_index(0)
            usedColor2 = []
            usedColor3 = []
            #usedColor2.append((0,0,0))
            for i in range(2,table.nrows,1):
                row = table.row_values(i) 
                try:
                    start = (int(row[3]),int(row[4]),int(row[5]))

                    # if start not in usedColor2:
                    #     usedColor2.append(start)
                    # elif start != (0,0,0):
                    #     print(i-1,row[0],"start repeat:",start)    
                    #     usedColor3.append(start)

                    if start not in usedColor:
                        print(i-1,row[0],"start",start)
                except:
                    pass

                try:
                    start = (int(row[6]),int(row[7]),int(row[8]))
                    # if start not in usedColor2:
                    #     usedColor2.append(start)
                    # elif start != (0,0,0):
                    #     print(i-1,row[0],"start repeat:",start)
                    #     usedColor3.append(start)  

                    if start not in usedColor:
                        print(i-1,row[0],"end",start)
                except:
                    pass
            print("======================down============================")
    input("enter any key to quit!")