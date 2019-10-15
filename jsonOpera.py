#encoding:UTF-8
import json  
import urllib.request
import os

url = "http://api.vesal.cn:8000/vesal-jiepao-prod/v1/app/struct/initMyStruct?token=1&plat=android&fyId=44&version=1&appVersion=3.2.0"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
#loads:json => dict  
json_dict = json.loads(data)
# count =len(json_dict['List'][0]['StructList'])
file_handle = open('D:/MyFile/batworkSpace/file/1.txt','w')
print(len(json_dict['List'][0]['StructList']))
for a in json_dict['List'][0]['StructList']:
    # print('write in ..'+a['ab_path'])
    file_handle.write(a['ab_path']+"\n")
file_handle.close()
#dumps:dict => json 
json_str = json.dumps(json_dict)  