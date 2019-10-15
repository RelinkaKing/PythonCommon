import os
import re

# 操控字符串
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
          first=str(file).find('_',0)
          second=str(file).find(']',0)
          thead=str(file).split(',')[1:]
          print(thead[0])
          out=str(file).replace(','+thead[0],'',1)
          # out=out.replace('_','',1)
          print(out)
          os.rename(root+'\\'+file,root+'\\'+out+'.gif')

ChangeFileName(r'C:\Users\Administrator\Desktop\169gif', r'C:\Users\Administrator\Desktop\169gif')