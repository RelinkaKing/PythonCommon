from xml.dom import minidom

import xlwt
import xlrd
from xml.dom.minidom import Document
import codecs

def CreateMainModleInfoxml():
    doc = Document()
    SignInfoList = doc.createElement('partition')
    SignInfoList.setAttribute('name', '动脉')
    SignInfoList.setAttribute('type', 'B')

    doc.appendChild(SignInfoList)

    strs=input("input excel position :")

    book = xlrd.open_workbook(strs)
    sheet_name=input("input sheet name :")
    sheet1 = book.sheet_by_name(sheet_name)
    count = sheet1.nrows
    # 总行数
    # print(count)

    LayerElement=doc.createElement('Layered')
    LayerElement.setAttribute('name', 'L01')
    SignInfoList.appendChild(LayerElement)
    for i in range(1, count):
        if sheet1.cell_value(i, 0) is '':
            break
        SignElement = doc.createElement('model')
        SignElement.setAttribute('name', sheet1.cell_value(i, 0))
        LayerElement.appendChild(SignElement)

    LayerElement=doc.createElement('Layered')
    LayerElement.setAttribute('name', 'L02')
    SignInfoList.appendChild(LayerElement)
    for i in range(1, count):
        if sheet1.cell_value(i, 1) is '':
            break
        SignElement = doc.createElement('model')
        SignElement.setAttribute('name', sheet1.cell_value(i, 1))
        LayerElement.appendChild(SignElement)
    
    LayerElement=doc.createElement('Layered')
    LayerElement.setAttribute('name', 'L03')
    SignInfoList.appendChild(LayerElement)
    for i in range(1, count):
        if sheet1.cell_value(i, 2) is '':
            break
        SignElement = doc.createElement('model')
        SignElement.setAttribute('name', sheet1.cell_value(i, 2))
        LayerElement.appendChild(SignElement)       
    doc.appendChild(SignInfoList)
    f = open(r'C:\Users\Relinka\Desktop\models.xml', 'w', encoding='utf-8')
    doc.writexml(f, addindent='  ', newl='\n', encoding='utf-8')

CreateMainModleInfoxml()