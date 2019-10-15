# -*- coding:utf-8 -*-
from xml.dom import minidom

import os
import xlwt
import xlrd
from xml.dom.minidom import Document
import codecs

def CreateSignInfoListxml():
    doc=Document()
    SignInfoList=doc.createElement('SignInfoList')
    doc.appendChild(SignInfoList)

    print(os.getcwd())
    path=os.getcwd()
    strs=input("input excel position :")
    book =xlrd.open_workbook(path+'/'+strs)

    sheet_name=input("input sheet name :")
    sheet1 = book.sheet_by_name(sheet_name)
    # xlsfile=r'C:\Users\Administrator\Desktop\生殖泌尿2.1.xlsx'
    count =sheet1.nrows
    atlasArray={}
    for i in range(0,count):
        print(sheet1.cell_value(i, 0)+'  '+sheet1.cell_value(i, 1))
        if(sheet1.cell_value(i,0) not in atlasArray):
            atlasArray[sheet1.cell_value(i, 0)]=sheet1.cell_value(i, 1)


    strs2=input("input excel position :")
    book2 =xlrd.open_workbook(path+'/'+strs2)

    sheet_name2=input("input sheet name :")
    sheet2 = book2.sheet_by_name(sheet_name2)
    # xlsfile=r'C:\Users\Administrator\Desktop\生殖泌尿2.1.xlsx'
    count2 =sheet2.nrows
    atlasArray2=[]
    for i in range(0,count2):
        if(sheet2.cell_value(i,0)==""):
            continue
        if(sheet2.cell_value(i,0) not in atlasArray2):
            atlasArray2.append(sheet1.cell_value(i, 0))  
            try:
                Atlas=doc.createElement('Atlas')
                Atlas.setAttribute("signSA",atlasArray[sheet2.cell_value(i, 1)])
            except :
                print(sheet2.cell_value(i, 1)+'     ------------------')
                continue
            Atlas.setAttribute("signId",str(sheet2.cell_value(i, 0)))
            Atlas.setAttribute("signName",str(sheet2.cell_value(i, 1)))
            SignInfoList.appendChild(Atlas)
    doc.appendChild(SignInfoList)
    f=open(r'C:\Users\Relinka\Desktop\SignInfoList.xml','w',encoding='utf-8')
    doc.writexml(f,addindent='  ',newl='\n',encoding='utf-8')

CreateSignInfoListxml()