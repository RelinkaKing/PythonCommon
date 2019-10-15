#!/usr/bin/env python
# -*- coding:utf-8 -*-
from xml.dom import minidom

import xlwt
import xlrd
from xml.dom.minidom import Document
import codecs
# workbook =xlwt.Workbook(encoding='utf-8',style_compression=0)

# excel  实体数据对象   表test
# sheet= workbook.add_sheet('test',cell_overwrite_ok=True)
# sheet.write(0,0,'firstCellContent')
# sheet.write(1,0,'secondeContent')
# txt='中文名字'
# sheet.write(2,0,txt)
# 保存指定操作,到输出路径
# workbook.save(r'C:\Users\Administrator\Desktop\test.xlsx')
#
# ==由于minidom默认的writexml()函数在读取一个xml文件后，修改后重新写入如果加了newl='\n',会将原有的xml中写入多余的行
#　 ==因此使用下面这个函数来代替

def CreateSignInfoListxml():
    doc=Document()
    SignInfoList=doc.createElement('SignInfoList')
    doc.appendChild(SignInfoList)

    xlsfile=r'C:\Users\Administrator\Desktop\呼吸消化文档2.0.1.xlsx'
    book =xlrd.open_workbook(xlsfile)
    sheet1=book.sheet_by_name('Book01文档')
    count =sheet1.nrows
    colume=sheet1.ncols
    atlasArray=[]
    # 总行数
    # print(count)
    for i in range(0,count):
        if(sheet1.cell_value(i,0) not in atlasArray):
            atlasArray.append(sheet1.cell_value(i, 0))  #不存在图谱  新建节点元素
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
    f=open(r'C:\Users\Administrator\Desktop\SignInfoList.xml','w',encoding='utf-8')
    doc.writexml(f,addindent='  ',newl='\n',encoding='utf-8')

def CreateMainModleInfoxml():
    doc = Document()
    SignInfoList = doc.createElement('EC')
    doc.appendChild(SignInfoList)

    xlsfile =r'C:\Users\Administrator\Desktop\文本\运动系统大纲2.0.1文档.xlsx'
    book = xlrd.open_workbook(xlsfile)
    sheet1 = book.sheet_by_name('模型文档')
    count = sheet1.nrows
    colume = sheet1.ncols
    atlasArray = []
    # 总行数
    # print(count)
    for i in range(1, count):
        SignElement = doc.createElement('model')
        SignElement.setAttribute('chinese', sheet1.cell_value(i, 0))
        SignElement.setAttribute('pinyin', sheet1.cell_value(i, 1))
        SignElement.setAttribute('english', sheet1.cell_value(i, 2))
        SignElement.setAttribute('notes', sheet1.cell_value(i, 3))
        SignInfoList.appendChild(SignElement)
    doc.appendChild(SignInfoList)
    f = open(r'C:\Users\Administrator\Desktop\models.xml', 'w', encoding='utf-8')
    doc.writexml(f, addindent='  ', newl='\n', encoding='utf-8')

# CreateMainModleInfoxml()
CreateSignInfoListxml()