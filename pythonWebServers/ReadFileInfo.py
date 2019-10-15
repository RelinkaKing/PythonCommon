from lib2to3.pgen2 import driver

import xlrd
from xml.dom.minidom import Document

def littleMap():
    doc=Document()
    litte=doc.createElement('LittleMap')
    doc.appendChild(litte)
    book = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\运动系统2.0.1导出文件\SA2.0发布需求导出.xlsx')
    sheet=book.sheet_by_name('人体分区对照表')
    list=[]
    for i in range(1,sheet.nrows):
        list.append(sheet.cell_value(i,0))
    # print(list)
    sheet2=book.sheet_by_name('小地图文档')
    # print(sheet2.nrows)
    startposition = []
    middle=0
    nextposition = []
    a=0
    for s in list:
        # find  start position   end position
        for i in range(0,sheet2.nrows):
            if s in sheet2.cell_value(i,0):
                middle=i
        startposition.append(middle)
    for i in startposition:
        nextposition.append(i)
    nextposition.remove(0)
    nextposition.append(sheet2.nrows-1)
    print(startposition,nextposition)
    for s in list:
        second = doc.createElement('partition')
        second.setAttribute('name',s)
        litte.appendChild(second)
        for i in range(startposition[a]+1,nextposition[a]-1):
            model = doc.createElement('model')
            model.setAttribute('name',sheet2.cell_value(i,0))
            second.appendChild(model)
        a+=1
    doc.writexml(open(r'C:\Users\Administrator\Desktop\sportlittlemap.xml','w',encoding='utf-8'),addindent='   ',newl='\n',encoding='utf-8')

littleMap()

# book=xlrd.open_workbook(r'C:\Users\Administrator\Desktop\运动系统2.0.1导出文件\SA2.0发布需求导出.xlsx')
# sheet=book.sheet_by_name('肌肉分层')
#
# doc=Document()
# partition=doc.createElement('partition')
# partition.setAttribute('type','B')
# partition.setAttribute('name','肌学')
# doc.appendChild(partition)
# for i in range(0,sheet.ncols):
#     fenceng = doc.createElement('Layered')
#     fenceng.setAttribute('name',sheet.cell_value(0,i))
#     partition.appendChild(fenceng)
#     for j in range(1,sheet.nrows):
#         if sheet.cell_value(j,i) is '':
#             break
#         element = doc.createElement('model')
#         element.setAttribute('name',sheet.cell_value(j,i))
#         fenceng.appendChild(element)
# doc.writexml(open(r'C:\Users\Administrator\Desktop\RightMenu.xml','w',encoding='utf-8'),addindent='   ',newl='\n',encoding='utf-8')

