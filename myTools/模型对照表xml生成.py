from xml.dom import minidom

import xlwt
import xlrd
from xml.dom.minidom import Document
import codecs

def CreateMainModleInfoxml():
    doc = Document()
    SignInfoList = doc.createElement('EC')
    doc.appendChild(SignInfoList)
# C:\Users\Relinka\Downloads\消化文档2.0.2.xlsx
    strs=input("input excel position :")

    book = xlrd.open_workbook(strs)
    sheet_name=input("input sheet name :")
    sheet1 = book.sheet_by_name(sheet_name)
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
    f = open(r'C:\Users\Relinka\Desktop\models.xml', 'w', encoding='utf-8')
    doc.writexml(f, addindent='  ', newl='\n', encoding='utf-8')

CreateMainModleInfoxml()