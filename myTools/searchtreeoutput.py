from xml.dom import minidom

import xlwt
import xlrd
from xml.dom.minidom import Document
import codecs
import xml.etree.ElementTree as ET  
  
#全局唯一标识  
unique_id = 1  
  
#遍历所有的节点  
def walkData(root_node, level, result_list):  
    global unique_id  
    temp_list =[unique_id, level, root_node.tag, root_node.attrib]  
    result_list.append(temp_list)  
    unique_id += 1  
      
    #遍历每个子节点  
    children_node = root_node.getchildren()  
    if len(children_node) == 0:  
        return  
    for child in children_node:  
        walkData(child, level + 1, result_list)  
    return  


def getXmlData(file_name):  
    level = 1 #节点的深度从1开始  
    result_list = []  
    root = ET.parse(file_name).getroot()  
    walkData(root, level, result_list)  
  
    return result_list  
  


def checkNoteFromXml():
    strs=input("input tree position :")
    R = getXmlData(strs)  
    for x in R:  
        //判断是否存在name
        print(x)  


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


checkNoteFromXml()
# CreateMainModleInfoxml()