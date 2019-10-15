# -*- coding: utf-8 -*-
import PIL.Image as Image
import random
import os
from PIL import ImageFont,ImageDraw
import datetime
import json
import re
import xlwt
from xlwt import Workbook
canUseRGB = [x for x in range(0,255,5)]
randomColorList = []
def getRandomColor():
    sumL = len(canUseRGB)-1
    randomColor = lambda:(canUseRGB[random.randint(0,sumL)],canUseRGB[random.randint(0,sumL)],canUseRGB[random.randint(0,sumL)])
    tmpColro = randomColor()
    while tmpColro in randomColorList:
        tmpColro = randomColor()
    randomColorList.append(tmpColro)
    
    return tmpColro

def saveAllColor(num,outputPath):
    usedColor = []
    for i in range(0,num,1):
        usedColor.append(getRandomColor())
    writeToExcel(outputPath,usedColor)
def writeToExcel(outputPath,colros):
    book = Workbook(encoding='utf-8')
    sheet1 = book.add_sheet("default",cell_overwrite_ok=True)
    count = 0
    sheet1.write(0,0,"Id")
    sheet1.write(0,1,"Color(rgb)")
    sheet1.write(0,2,"ColorHex")
    sheet1.write(0,3,"ColorBlock")
    tmpPngPath = "tmpcc.bmp"
    rowCount = 1
    for color in colros:
        tmpColor = color
        while "X" in str(toHex(tmpColor)):
            tmpColor = getRandomColor()
        #tmpColor = (tmpColor[2],tmpColor[1],tmpColor[0])
        im = Image.new("RGB",(50,20),tmpColor)
        im.save(tmpPngPath,"bmp")
        sheet1.write(rowCount,0,str(count))
        sheet1.write(rowCount,1,str(tmpColor))
        print("%d / %d"%(count+1,len(colros)))
        print(str(tmpColor))
        print(str(toHex(tmpColor)))
        sheet1.write(rowCount,2,str(toHex(tmpColor)))
        sheet1.insert_bitmap(tmpPngPath,rowCount,3)
        
        count = count+1
        rowCount= rowCount+1
    os.remove(tmpPngPath)
    # 保存Excel book.save('path/文件名称.xls')
    book.save(outputPath)
    return
def toHex(rgb):
    #rgb=(255, 255,255)
    #XAFADC
    #0x100bd7
    #7FFFFF
    r,g,b=rgb
    return str(hex((r << 16)|(g << 8)|b | (0x1000000)))[-6:].upper()
    # strs = ""
    # for j in range (0, len(rgb)):
    #     #每次转换之后只取0x7b的后两位，拼接到strs中
    #     strs += str(hex(rgb[j]))[-2:]
    # return strs.upper()

if __name__ == '__main__':
    # workPath = "D:/pythonWorkSpaces/pythonlib/MyPythonLib/Util/datas"
    # os.chdir(workPath)
    while(True):
        a = input("number:")
        x=eval(a)
        if type(x)==int:
            saveAllColor(x,"randomColor.xls")
            break
        else:
            print(str(a) +" is number?")    
    print("down")