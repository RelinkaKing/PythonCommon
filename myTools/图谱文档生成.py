# -*- coding:utf-8 -*-
from xml.dom import minidom

import xlwt
import xlrd
from xml.dom.minidom import Document
import codecs

def CreateSignInfoListxml():
    doc=Document()
    SignInfoList=doc.createElement('SignInfoList')
    doc.appendChild(SignInfoList)

    strs=input("input excel position :")
    book =xlrd.open_workbook(strs)

    sheet_name=input("input sheet name :")
    sheet1 = book.sheet_by_name(sheet_name)
    # xlsfile=r'C:\Users\Administrator\Desktop\生殖泌尿2.1.xlsx'
    count =sheet1.nrows
    atlasArray=[]
    for i in range(0,count):
        if(sheet1.cell_value(i,0) not in atlasArray):
            atlasArray.append(sheet1.cell_value(i, 0))  
            Atlas=doc.createElement('Atlas')
            Atlas.setAttribute('AtlasID',sheet1.cell_value(i,0))
            SignInfoList.appendChild(Atlas)
        SignElement = doc.createElement('SignElement')
        # SignElement.setAttribute('AtlasId', sheet1.cell_value(i, 0))
        SignElement.setAttribute('SignId', sheet1.cell_value(i, 2))
        SignElement.setAttribute('SignName', sheet1.cell_value(i, 3))
        SignElement.setAttribute('SignChinese', sheet1.cell_value(i, 1))
        SignElement.setAttribute('SignEnglish', sheet1.cell_value(i, 4))
        SignElement.setAttribute('SignExplain', sheet1.cell_value(i, 5))
        Atlas.appendChild(SignElement)
    doc.appendChild(SignInfoList)
    f=open(r'C:\Users\Relinka\Desktop\SignInfoList.xml','w',encoding='utf-8')
    doc.writexml(f,addindent='  ',newl='\n',encoding='utf-8')


def CreateAtlaslistxml():
    doc=Document()
    SignInfoList=doc.createElement('AtlasList')
    doc.appendChild(SignInfoList)

    strs=input("input excel position :")
    book =xlrd.open_workbook(strs)
    sheet_name=input("input sheet name :")
    sheet1 = book.sheet_by_name(sheet_name)
    count =sheet1.nrows
    atlasArray=[]
    for i in range(1,count):
        if(sheet1.cell_value(i,0) not in atlasArray):
            atlasArray.append(sheet1.cell_value(i, 0))  
            Atlas=doc.createElement('Atlas')
            Atlas.setAttribute('AtlasId',str(sheet1.cell_value(i,0)))
            Atlas.setAttribute('DingziName',str(sheet1.cell_value(i,0)))
            Atlas.setAttribute('PictureName',str(sheet1.cell_value(i,0)))
            Atlas.setAttribute('B','255')
            Atlas.setAttribute('Chinese','ch_nise')
            Atlas.setAttribute('G','0')
            Atlas.setAttribute('R','255')
            Atlas.setAttribute('cameraBackXRot','0')
            Atlas.setAttribute('cameraBackYRot','0')
            Atlas.setAttribute('cameraBackZRot','0')
            Atlas.setAttribute('fieldOfView','10')
            Atlas.setAttribute('maxDis','0')
            Atlas.setAttribute('minDis','0')
            Atlas.setAttribute('signDistance','1.4')
            Atlas.setAttribute('signPositionX','0')
            Atlas.setAttribute('signPositionY','0')
            Atlas.setAttribute('signSize','20')
            Atlas.setAttribute('version','0')
            SignInfoList.appendChild(Atlas)
        SignElement = doc.createElement('model')
        SignElement.setAttribute('ModelName', sheet1.cell_value(i, 1))
        SignElement.setAttribute('IsTranslucent', str(sheet1.cell_value(i, 2)))
        Atlas.appendChild(SignElement)
    doc.appendChild(SignInfoList)
    f=open(r'C:\Users\Relinka\Desktop\AtlasList.xml','w',encoding='utf-8')
    doc.writexml(f,addindent='  ',newl='\n',encoding='utf-8')



CreateAtlaslistxml()
# CreateSignInfoListxml()