# 生成模型信息到图谱xml
import xml
from xml.dom.minidom import parse
from xml.dom.minidom import Document
import os
import shutil
import re
import xlwt
import xlrd
# print('梁燕姬')
# 图谱字典
dict = {}
# 图谱名称列表
list = []
# 读取图谱模型文件分类信息
def getNameArray(path):
    index=0
    # 元组内部数量固定
    for root,dirs,files in os.walk(path):
        # 获取到书签中文名字数组
        if(len(dirs) !=0):
            list=dirs
        # for file in files:
            # print(file)
    for root,dirs,files in os.walk(path):
        if (len(files)!=0):
             dict[list[index]]=files
             index += 1
    # print(dict[list[1]])  #获取对应文件夹下的模型文件

# 读取模型xml
def ReadModelInfo():
    getNameArray(r'C:\Users\Administrator\Desktop\bookmarkmodel')

    doc= Document()
    AtlasList = doc.createElement('AtlasList')
    doc.appendChild(AtlasList)

    domTreeOld=xml.dom.minidom.parse(r'C:\Users\Administrator\Desktop\AtlasList.xml')
    collection=domTreeOld.documentElement
    Atlases=collection.getElementsByTagName('Atlas')
    for i in Atlases:
        atlasElement=doc.createElement("Atlas")
        atlasElement.setAttribute('AtlasId', i.getAttribute('AtlasId'))
        atlasElement.setAttribute('PictureName',i.getAttribute('PictureName'))
        atlasElement.setAttribute('Chinese', i.getAttribute('Chinese'))
        atlasElement.setAttribute('TextureName',i.getAttribute('TextureName'))
        atlasElement.setAttribute('DingziName', i.getAttribute('DingziName'))
        atlasElement.setAttribute('minDis',i.getAttribute('minDis'))
        atlasElement.setAttribute('maxDis', i.getAttribute('maxDis'))
        atlasElement.setAttribute('signPositionX',i.getAttribute('signPositionX'))
        atlasElement.setAttribute('signPositionY', i.getAttribute('signPositionY'))
        atlasElement.setAttribute('signDistance', i.getAttribute('signDistance'))
        atlasElement.setAttribute('signSize', i.getAttribute('signSize'))
        atlasElement.setAttribute('cameraBackXRot', i.getAttribute('cameraBackXRot'))
        atlasElement.setAttribute('cameraBackYRot',i.getAttribute('cameraBackYRot'))
        atlasElement.setAttribute('cameraBackZRot',i.getAttribute('cameraBackZRot'))
        AtlasList.appendChild(atlasElement)

        # print(i.getAttribute("Chinese"))
        try:
            tempList=dict[i.getAttribute("Chinese")]
            for j in tempList:
                tempnote=doc.createElement(str(j)[:-4])
                atlasElement.appendChild(tempnote)
        except:
            print(i.getAttribute("Chinese"))
        doc.writexml(open(r'C:\Users\Administrator\Desktop\AtlasList2.xml','w',encoding='utf-8'),addindent='   ',newl='\n',encoding='utf-8')

# 修改文件名字
def ChangeFileName(filepath,outpath):
    list=[]
    outlist=[]
    # 创建输出文件夹
    isExistFile=os.path.exists(outpath)
    print(isExistFile)
    if not isExistFile:
        os.makedirs(outpath)
        print('create seccessed')
    # for files in os.listdir(filepath):
    #     print(files)
        # list=os.path.join(filepath,files)
        # if os.path.isdir(list):
        #     ChangeFileName(list)
        #     filename=os.path.splitext(files)[0]
    # for root,dirs,files in os.walk(filepath):
        # print(files)
        # for file in files:
        #     outlist.append(str(file).maketrans('拷贝',''))
    for root,dirs,files in os.walk(filepath):
        for file in files:
          # print(root+'\\'+file)
          # 操作字符串
          out=str(file).replace('拷贝','',1)
          os.rename(root+'\\'+file,root+'\\'+out)

# copy file to path
def CopyFile(filepath,outpath):
    for root ,dir ,files in os.walk(filepath):
        # print(files)
        for file in files:
            if('拷贝.png'in str(file)):
                # list.append(root+file)
                shutil.copyfile(filepath+'\\'+file,outpath+'\\'+file)
    # print(list)
    # for i in os.listdir(filepath):
    #     print(i)
        # if('拷贝.png'in str(i)):
        #     shutil.copyfile(filepath,outpath)

def ReadSignListInfo():
    doc=Document()
    SingListInfo=doc.createElement('SignListInfo')
    doc.appendChild(SingListInfo)
    # （i，0） （i,1）
    bookAtlasId=xlrd.open_workbook(r'C:\Users\Administrator\Desktop\运动系统图钉文件2.0.1—20180202\文档\运动系统2.0.1文案.xlsx')
    sheetAtlasId=bookAtlasId.sheet_by_name('图谱文档')

    # (i,6)
    bookSign =xlrd.open_workbook(r'C:\Users\Administrator\Desktop\运动系统2.0.1图钉文件增加模型020201.xlsx')
    sheetSign =bookSign.sheet_by_name('图钉文档总文档')



def __main():
    print("开始运行")
    # ReadModelInfo()
    ChangeFileName(r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\Resources\SignTexture',r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\Resources\SignTextureNew')
    # CopyFile(r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\Textures\图谱\SignTextutre',
    #          r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\Resources\SignTexture')
    print("End")

# 当前运行
__main()

# 合成xml  根据图谱中文名字
def CombineXml():
    print("todo")

# 读取表头xml 存储字典
def ReadTopAtlas():
    a=['01','02']
    topAtlas=xml.dom.minidom.parse(r'C:\Users\Administrator\Desktop\AtlasList.xml')
    colle=topAtlas.documentElement
    colles=colle.getElementsByTagName('Atlas')
    for i in colles:
        for j in a:
            if(str(i.getAttribute('Chinese') ==j)):
                print(1)

# 操作文件夹获取文件名字
def getFileName(filePath):
    # for dirs in os.walk(filePath):
    #     dirs   元组  （路径，文件夹名字数组，文件名字数组）（包含后缀）
        # print(dirs)
    # for files in os.walk(filePath):
    #     print(files)

    # 获取所有 .cs 文件的名字
    L=[]
    for root ,dirs,files in os.walk(filePath):
        for file in files:
            if os.path.splitext(file)[1]=='.cs':
                L.append(os.path.join(root,file))
    return L
# print(getFileName(r'C:\Users\Administrator\Desktop\Scripts'))

#
def filelist(path,listname):
    for file in os.listdir(path):
        filepath=os.path.join(path,file)
        if os.path.isdir(filepath):
            filelist(filepath,listname)
        else:
            listname.append(filepath)
listnam=[]
# filelist(r'C:\Users\Administrator\Desktop\Scripts',listnam)
# print(listnam)

# 提取xml信息
def getNameChinese():
    domtree=xml.dom.minidom.parse(r'D:\Unity\UnityProject\MobileLocalAnatomy\Vesal_MobileSystemAnatomy04_MatieralDebug\Assets\StreamingAssets\AllModel.xml')
    collection=domtree.documentElement
    chinese=[]
    pinyin=[]
    models=collection.getElementsByTagName('model')
    for i in models:
        chinese.append(str(i.getAttribute('chinese')))
        pinyin.append(str(i.getAttribute('name')))
    # print(chinese)

    workbook=xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = workbook.add_sheet('test', cell_overwrite_ok=True)
    for i in range(0, len(chinese)):
        sheet.write(i, 0, chinese[i])
    for i in range(0,len(pinyin)):
        sheet.write(i,1,pinyin[i])
    workbook.save(r'C:\Users\Administrator\Desktop\test.xls')
# getNameChinese()

