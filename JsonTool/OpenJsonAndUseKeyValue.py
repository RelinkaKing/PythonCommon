import json
import os
import shutil

tartgetPath="./"

filterColorList=[]
config_dict={}
id_name_dic={}
img_path=r"C:\Users\Raytine\Desktop\StreamingAssets\fix_bookmark_img"
# with open("./json/1.json",'r',encoding='UTF-8') as load_f:
with open(r"D:\MyFile\PythonWorkSpaces\JsonTool\json\1.json",'r',encoding='UTF-8') as load_f:
    config_dict = json.load(load_f)
    # 遍历由json数据得到的list
    for id_name in config_dict["id_name"]:
        # if(key in dic.keys())
        source=img_path+"/"+id_name["name"]+".jpg"
        target= img_path+"/"+id_name["id"]+".jpg"
        if(os.path.exists(source)):
            os.rename(source,target) 
            id_name_dic[id_name["name"]]=id_name["id"]
        else:
            shutil.copyfile(img_path+"/"+id_name_dic[id_name["name"]]+".jpg",target)