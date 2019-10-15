import xlrd
from xml.dom.minidom import Document
import xml
from xml.dom.minidom import parse

def CreateAtlasListXmlOld():

    doc=Document()
    AtlasList=doc.createElement('AtlasList')
    doc.appendChild(AtlasList)

    Book=xlrd.open_workbook(r'C:\Users\Administrator\Desktop\运动系统2.0.1图钉文件增加模型020211.xlsx')
    sheet=Book.sheet_by_name('图谱文档')

    list=[]
    for i in range(1,sheet.nrows):
        if sheet.cell_value(i,0) not in list:
            list.append(sheet.cell_value(i,0))
            atlas=doc.createElement('Atlas')
            temp=sheet.cell_value(i,0)
            atlas.setAttribute('AtlasId',temp)
            atlas.setAttribute('Chinese', sheet.cell_value(i, 1))
            atlas.setAttribute('DingziName', temp)
            atlas.setAttribute('version', '0')
            atlas.setAttribute('PictureName',temp)
            atlas.setAttribute('minDis', '0')
            atlas.setAttribute('maxDis', '0')
            atlas.setAttribute('signPositionX', '0')
            atlas.setAttribute('signPositionY', '0')
            atlas.setAttribute('signDistance', '0')
            atlas.setAttribute('signSize', '20')
            atlas.setAttribute('cameraBackXRot', '0')
            atlas.setAttribute('cameraBackYRot', '0')
            atlas.setAttribute('cameraBackZRot', '0')
            atlas.setAttribute('R', '255')
            atlas.setAttribute('G', '0')
            atlas.setAttribute('B', '255')
            atlas.setAttribute('fieldOfView', '2')
            AtlasList.appendChild(atlas)
            if sheet.cell_value(i,2) !='null':
                model = doc.createElement('modelTex')
                model.setAttribute('ModelName', sheet.cell_value(i, 2))
                # model.setAttribute('textureName', sheet.cell_value(i, 3))
                # model.setAttribute('normal', sheet.cell_value(i, 4))
                # model.setAttribute('texVersion','0')
                atlas.appendChild(model)
            else:
                model =doc.createElement('modelTex')
                model.setAttribute('ModelName',sheet.cell_value(i,2))
                # # # model.setAttribute('textureName',sheet.cell_value(i, 3))
                # # model.setAttribute('normal', sheet.cell_value(i, 4))
                # model.setAttribute('texVersion', '0')
                atlas.appendChild(model)
            if sheet.cell_value(i,0)==52:
                # 结束判定
                break
    doc.writexml(open(r'C:\Users\Administrator\Desktop\AtlasList.xml','w',encoding='utf-8'),addindent='   ',newl='\n',encoding='utf-8')

def CreateAtlasListxmlType2():
    dict={}
    xlsfile0 = r'C:\Users\Administrator\Desktop\大脑解剖2.0.1_0文档.xlsx'
    book = xlrd.open_workbook(xlsfile0)
    sheet0 = book.sheet_by_name('图谱编号')
    for i in range(1,sheet0.nrows):
        dict[sheet0.cell_value(i,0)]=sheet0.cell_value(i,1)

    # print(len(dict))
    doc=Document()
    SignInfoList=doc.createElement('AtlasList')
    doc.appendChild(SignInfoList)

    xlsfile=r'C:\Users\Administrator\Desktop\大脑解剖2.0.1_0文档.xlsx'
    book =xlrd.open_workbook(xlsfile)
    sheet1=book.sheet_by_name('Book02文档')
    count =sheet1.nrows
    colume=sheet1.ncols
    atlasArray=[]
    # 总行数
    # print(count)
    for i in range(1,count):
        if(sheet1.cell_value(i,0) not in atlasArray):
            atlasArray.append(sheet1.cell_value(i, 0))  #不存在图谱  新建节点元素
            atlas=doc.createElement('Atlas')
            temp=str(sheet1.cell_value(i ,0))
            atlas.setAttribute('AtlasId',temp)
            atlas.setAttribute('Chinese', dict.get(temp))
            atlas.setAttribute('DingziName', temp)
            atlas.setAttribute('version', '0')
            atlas.setAttribute('PictureName',temp)
            atlas.setAttribute('minDis', '0')
            atlas.setAttribute('maxDis', '0')
            atlas.setAttribute('signPositionX', '0')
            atlas.setAttribute('signPositionY', '0')
            atlas.setAttribute('signDistance', '0')
            atlas.setAttribute('signSize', '20')
            atlas.setAttribute('cameraBackXRot', '0')
            atlas.setAttribute('cameraBackYRot', '0')
            atlas.setAttribute('cameraBackZRot', '0')
            atlas.setAttribute('R', '255')
            atlas.setAttribute('G', '0')
            atlas.setAttribute('B', '255')
            atlas.setAttribute('fieldOfView', '2')
            SignInfoList.appendChild(atlas)
        SignElement = doc.createElement('model')
        # SignElement.setAttribute('AtlasId', sheet1.cell_value(i, 0))
        SignElement.setAttribute('ModelName', sheet1.cell_value(i, 1))
        SignElement.setAttribute('IsTranslucent', str(sheet1.cell_value(i, 2)))
        atlas.appendChild(SignElement)
    doc.appendChild(SignInfoList)
    f=open(r'C:\Users\Administrator\Desktop\AtlasList.xml','w',encoding='utf-8')
    doc.writexml(f,addindent='  ',newl='\n',encoding='utf-8')


class type2(object):
    def __init__(self,atlasName):
        self.atlasName=atlasName
    namelist=[]


def CreateAtlasElement(atlasID):
    dict111={}
    xlsfile0 = r'C:\Users\Administrator\Desktop\运动系统2.0.1图钉bookmarktype02.xlsx'
    book = xlrd.open_workbook(xlsfile0)
    sheet0 = book.sheet_by_name('111')
    for i in range(1,sheet0.nrows):
        dict111[sheet0.cell_value(i,0)]=sheet0.cell_value(i,1)
    # dict222={}
    # xlsfile0 = r'C:\Users\Administrator\Desktop\运动系统2.0.1图钉bookmarktype02.xlsx'
    # book = xlrd.open_workbook(xlsfile0)
    # sheet0 = book.sheet_by_name('222')
    # for i in range(1,sheet0.nrows):
    #     dict222[sheet0.cell_value(i,0)]=sheet0.cell_value(i,1)
    doc = Document()
    SignInfoList = doc.createElement('AtlasList')
    doc.appendChild(SignInfoList)
    xlsfile = r'C:\Users\Administrator\Desktop\运动系统2.0.1图钉bookmarktype02.xlsx'
    book = xlrd.open_workbook(xlsfile)
    sheet1 = book.sheet_by_name('type2')
    count = sheet1.nrows
    atlasArray = []
    nameType2Dict={}
    for i in range(1,count):
        if(sheet1.cell_value(i,0) not in atlasArray):
            atlasArray.append(sheet1.cell_value(i,0))
        for j in atlasArray:
            t2=type2(j)
            t2.namelist=[]
            for i in range(1, count):
                if(sheet1.cell_value(i,0) == j):
                    t2.namelist.append(sheet1.cell_value(i,1))
            nameType2Dict[j]=t2
    mainkeys=nameType2Dict.keys()

    atlas = doc.createElement('Atlas')
    atlas.setAttribute('AtlasId', atlasID)
    atlas.setAttribute('Chinese', dict111.get(atlasID))
    atlas.setAttribute('DingziName',atlasID)
    atlas.setAttribute('version', '0')
    atlas.setAttribute('PictureName',atlasID)
    atlas.setAttribute('minDis', '0')
    atlas.setAttribute('maxDis', '0')
    atlas.setAttribute('signPositionX', '0')
    atlas.setAttribute('signPositionY', '0')
    atlas.setAttribute('signDistance', '0')
    atlas.setAttribute('signSize', '20')
    atlas.setAttribute('cameraBackXRot', '0')
    atlas.setAttribute('cameraBackYRot', '0')
    atlas.setAttribute('cameraBackZRot', '0')
    atlas.setAttribute('R', '255')
    atlas.setAttribute('G', '0')
    atlas.setAttribute('B', '255')
    atlas.setAttribute('fieldOfView', '2')
    SignInfoList.appendChild(atlas)
    # print(i)
    #解析对应type2 模型p
    t2=nameType2Dict.get(atlasID)
    if(len(t2.namelist)>0):
        for j in t2.namelist :
            SignElement = doc.createElement('model')
            SignElement.setAttribute('ModelName', j)
            SignElement.setAttribute('IsTranslucent', '0')
            atlas.appendChild(SignElement)

    doc.appendChild(SignInfoList)
    f=open(r'C:\Users\Administrator\Desktop\atlaselement.xml','w',encoding='utf-8')
    doc.writexml(f,addindent='  ',newl='\n',encoding='utf-8')

def CombineType12():
    # 表头字典查找表，用于列表生成对应图谱
    dict111={}
    xlsfile0 = r'C:\Users\Administrator\Desktop\大脑解剖2.0.1_0文档.xlsx'
    book = xlrd.open_workbook(xlsfile0)
    sheet0 = book.sheet_by_name('图谱编号')
    for i in range(1,sheet0.nrows):
        dict111[sheet0.cell_value(i,0)]=sheet0.cell_value(i,1)
    print(len(dict111))
    dict222={}
    xlsfile0 = r'C:\Users\Administrator\Desktop\大脑解剖2.0.1_0文档.xlsx'
    book = xlrd.open_workbook(xlsfile0)
    sheet0 = book.sheet_by_name('图谱编号')
    for i in range(1,sheet0.nrows):
        dict222[sheet0.cell_value(i,0)]=sheet0.cell_value(i,1)
    print(len(dict222))

    doc = Document()
    SignInfoList = doc.createElement('AtlasList')
    doc.appendChild(SignInfoList)
    xlsfile = r'C:\Users\Administrator\Desktop\大脑解剖2.0.1_0文档.xlsx'
    book = xlrd.open_workbook(xlsfile)
    sheet1 = book.sheet_by_name('Book02文档')
    count = sheet1.nrows
    atlasArray = []
    # 图谱编号对应  type2 类型数组
    nameType2Dict={}
    for i in range(1,count):
        if(sheet1.cell_value(i,0) not in atlasArray):
            atlasArray.append(sheet1.cell_value(i,0))
    print(atlasArray)
    for j in atlasArray:
        t2=type2(j)
        t2.namelist=[]
        for i in range(1, count):
            if(sheet1.cell_value(i,0) == j):
                t2.namelist.append(sheet1.cell_value(i,1))
        nameType2Dict[j]=t2
    print(len(nameType2Dict))
    mainkeys=nameType2Dict.keys()
    # t=nameType2Dict.get('24')
    # print(t.namelist)
    # create 111
    combine=dict(dict111,**dict222)
    print(dict111)
    for i in dict111.keys():
        atlas = doc.createElement('Atlas')
        atlas.setAttribute('AtlasId', i)
        atlas.setAttribute('Chinese', dict111.get(i))
        atlas.setAttribute('DingziName',i)
        atlas.setAttribute('version', '0')
        atlas.setAttribute('PictureName',i)
        atlas.setAttribute('minDis', '0')
        atlas.setAttribute('maxDis', '0')
        atlas.setAttribute('signPositionX', '0')
        atlas.setAttribute('signPositionY', '0')
        atlas.setAttribute('signDistance', '0')
        atlas.setAttribute('signSize', '20')
        atlas.setAttribute('cameraBackXRot', '0')
        atlas.setAttribute('cameraBackYRot', '0')
        atlas.setAttribute('cameraBackZRot', '0')
        atlas.setAttribute('R', '255')
        atlas.setAttribute('G', '0')
        atlas.setAttribute('B', '255')
        atlas.setAttribute('fieldOfView', '10')
        SignInfoList.appendChild(atlas)
        # print(i)
        if(mainkeys.__contains__(i)):
            #解析对应type2 模型p
            t2=nameType2Dict.get(i)
            for j in t2.namelist :
                SignElement = doc.createElement('model')
                SignElement.setAttribute('ModelName', j)
                SignElement.setAttribute('IsTranslucent', '0')
                atlas.appendChild(SignElement)

    doc.appendChild(SignInfoList)
    f=open(r'C:\Users\Administrator\Desktop\AtlasList.xml','w',encoding='utf-8')
    doc.writexml(f,addindent='  ',newl='\n',encoding='utf-8')

# CreateAtlasListxmlType2()

CombineType12()

# 生成对应图谱编号
# CreateAtlasElement('18')