import os

# 改变打包后的 ab  资源包
def ChangeNameToTarget(namesPath):
    # 从源路径获取文件名数组
    # namesPath=r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\图钉\map'
    for root, dirs, files in os.walk(namesPath):
        list = files
    outlist=[]
    lowerList=[]
    for i in list:
        if '.meta' not in i :
            outlist.append(i)
    for i in range(0,len(outlist)):
        lowerList.append(str(outlist[i]).lower())

    # 去除  jpg 后缀
    noOutList=[]
    for j in outlist:
        noOutList.append(str(j).replace('.jpg','',1))
    noLowerList=[]

    for i in lowerList:
        noLowerList.append(str(i).replace('.jpg','',1))
    print('lowerList',noLowerList)
    print('outlist',noOutList)
    # 移动目标文件到新文件夹，并修改名字,添加后缀‘.assetbundle’
    resourcePath=r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\StreamingAssets'
    # if not os.path.exists(targetPath):
    #     os.makedirs(targetPath)
    for root,dirs,files  in os.walk(resourcePath):
        # print(files)
        for file in files:
            if 'meta' not in file and 'manifest' not in file:
                for i in range(0,len(noLowerList)):
                    # print('file',file)
                    # print('nolowerlist',noLowerList[i])
                    if str(file) == noLowerList[i]:
                        print(1)
                        os.rename(resourcePath+'\\'+file,resourcePath+'\\encryptionAB\\'+noOutList[i]+'.assetbundle')

def ChangeSignNameToTarget(namesPath):
    # 从源路径获取文件名数组
    # namesPath=r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\图钉\map'
    for root, dirs, files in os.walk(namesPath):
        list = files
    outlist=[]
    for i in list:
        if '.meta' not in i :
            outlist.append(i)
    print(outlist)
    # 去除  jpg 后缀
    noOutList=[]
    for j in outlist:
        noOutList.append(str(j).replace('.prefab','',1))
    noLowerList=[]


    print('lowerList',noLowerList)
    print('outlist',noOutList)
    # 移动目标文件到新文件夹，并修改名字,添加后缀‘.assetbundle’
    resourcePath=r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\StreamingAssets'
    # if not os.path.exists(targetPath):
    #     os.makedirs(targetPath)
    # for root,dirs,files  in os.walk(resourcePath):
        # print(files)
        # for file in files:
        #     if 'meta' not in file and 'manifest' not in file:
        #         for i in range(0,len(noLowerList)):
        #             if str(file) == noLowerList[i]:
        #                 print(1)
        #                 os.rename(resourcePath+'\\'+file,resourcePath+'\\encryptionAB\\'+noOutList[i]+'.assetbundle')

def ModifyAssetBundleName():
    outPath=r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\StreamingAssets'
    prefabPath=r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\Prefab'
    texturePath=r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\图钉\map'

    outlist=[]
    lowerList=[]
    #贴图原名称，  小些后的名称
    for root, dirs, files in os.walk(texturePath):
        list = files
    for i in list:
        if '.meta' not in i :
            outlist.append(i)
    for i in range(0,len(outlist)):
        lowerList.append(str(outlist[i]).lower())
    noOutList = []
    for j in outlist:
        noOutList.append(str(j).replace('.jpg', '', 1))
    noLowerList = []

    for i in lowerList:
        noLowerList.append(str(i).replace('.jpg', '', 1))
    print('lowerList', noLowerList)
    print('outlist', noOutList)

    for root,dirs,files in os.walk(outPath):
        for file in files:
            if len(str(file))==2:
                # print(outPath+'\\'+file+'.assetbundle')
                os.rename(outPath+'\\'+file,outPath+'\\'+file+'.assetbundle')
            if 'meta' not in file and 'manifest' not in file:
                for i in range(0,len(noLowerList)):
                    if str(file) == noLowerList[i]:
                        # print(outPath+'\\'+file)
                        # print(outPath+noOutList[i]+'.assetbundle')
                        os.rename(outPath+'\\'+file,outPath+'\\'+noOutList[i]+'.assetbundle')
    #调用加密程序，弹出cmd 窗口


def ModifyPrefabName():
    outPath=r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\StreamingAssets'
    prefabPath=r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\Prefab'
    texturePath=r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\图钉\map'
    for root, dirs, files in os.walk(outPath):
        for file in files:
            if len(str(file)) == 2:
                # print(outPath+'\\'+file+'.assetbundle')
                os.rename(outPath + '\\' + file, outPath + '\\' + file + '.assetbundle')


# ModifyAssetBundleName()
ModifyPrefabName()
# ChangeNameToTarget(r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\图钉\map')
# ChangeSignNameToTarget(r'D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\Prefab')