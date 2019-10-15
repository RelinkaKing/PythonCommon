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
from PIL import Image
from io import BytesIO



def getResponse(host,request,method="GET",port=80,timeout=10,enableTimeSuffix = True,headers = None,returnJson = True,encode="utf-8"):
    conn = http.client.HTTPConnection(host, port=port, timeout=timeout)
    if not headers:
        headers = {
            'Cache-Control': "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
            }
    if enableTimeSuffix:
        request = request + "&Timestamp="+str(int(time.time()))
    conn.request(method,request,headers=headers)
    # 得到返回的 http response
    r1 = conn.getresponse()
    # HTTP 状态码
    print(r1.status,r1.reason)
    # HTTP 头部
    print(r1.getheaders())
    # body 部分
    response=""
    if returnJson:
        response = json.loads(r1.read().decode(encode)) 
    else:
        response = r1.read().decode(encode)
    conn.close()
    return response

def getJson(url):
    #r = requests.get(url, auth=('user', 'pass'))
    r = requests.get(url)
    #r.status_code,
    return r.json()

def getImage(url,file,isOverWrite = True):
    r = requests.get(url, stream=True)
    i = Image.open(BytesIO(r.content))
    i.show()

def getFile(url,file,isOverWrite = True):
    r = requests.get(url, stream=True)
    if os.path.isfile(file):
        if isOverWrite:
            os.remove(file)
        else:
            return
    with open(file, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
            fd.flush()
    r.close()