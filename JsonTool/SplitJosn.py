# -*- coding: utf-8 -*-

import json
import os

# read not fix length json ,split with first array

article_info = {}
data = json.loads(json.dumps(article_info))

data['article1'] = 'NONE'

article2 = {'title': 'python基础', 'publish_time': '2019-4-1', 'writer': {}}
data['article2'] = article2 

writer = {'name': '李先生', 'sex': '男', 'email': 'xxx@gmail.com'}
writer2 = {'name2': '李先生', 'sex2': '男', 'email2': 'xxx@gmail.com'}
writer.update(writer2)
data['article2']['writer'] = (writer)

article = json.dumps(data, ensure_ascii=False)
print(article)

# tartgetPath=r"C:\Users\Raytine\Desktop\bonedata (2).json"
# outpath="C:/Users/Raytine/Desktop/1/"

# filterColorList=[]
# id_name_dic={}
# if not os.path.exists(outpath):
#     os.mkdir(outpath)
# with open(tartgetPath,'r',encoding='UTF-8') as load_f:
#     filterColorList = json.load(load_f)
#     # 遍历由json数据得到的list
#     for simplefile in filterColorList:
#         filename=simplefile["key"]
#         with open(outpath+filename+".json","w",encoding='UTF-8') as f:
#             json.dump(simplefile,f,ensure_ascii=False,indent=2)
#             print("加载入文件完成...")