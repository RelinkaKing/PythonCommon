# -*- coding: utf-8 -*-

import random
import os
import time
import datetime
import json
import re
import http.client
import requests 
import FileUtil


print()
#http://
conn = http.client.HTTPConnection('api.vesal.cn', port=8000, timeout=10)

headers = {
    'Cache-Control': "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
    }
conn.request("GET","/vesal-jiepao-prod/v1/app/struct/initMyStruct?token=1&plat=android&fyId=2&version=1&Timestamp="+str(int(time.time())),headers=headers)

# 得到返回的 http response
r1 = conn.getresponse()
# HTTP 状态码
print(r1.status,r1.reason)
# HTTP 头部
print(r1.getheaders())
# body 部分
response = json.loads(r1.read().decode("utf-8")) 
conn.close()
#print(response["List"])
#测验练习
#微课课程
for x in response["List"]:
    if x["dict_name"] == "测验练习":
        for Struct in x["StructList"]:
            print(Struct["app_version"])
            ab_path = Struct["ab_path"]
            print(ab_path)
            #FileUtil.downLoadFile(ab_path,"./download/"+FileUtil.getFileName(ab_path))
#print(data.decode("utf-8"))
