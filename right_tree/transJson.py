#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json, pickle

data = {'k1':123, 'k2':'hello'}

## json
# json.dumps 将数据通过特殊的形式转换为所有程序都识别的字符串
j_str = json.dumps(data)
print(j_str)        #{"k2": "hello", "k1": 123}
print(type(j_str))
# json.loads 读取json.dumps特殊处理后的数据并返回该对象
j_str_loads = json.loads(j_str)
print(j_str_loads["k2"])      #{'k2': 'hello', 'k1': 123}

# json.dump 将数据通过特殊的形式转换为所有程序都识别的字符串，并写入文件
with open('file.json', 'w') as fp:
    json.dump(data, fp,indent=4)

with open('file.json', 'r') as fp:
    data_j_load = json.load(fp)
print(data_j_load)      #{'k2': 'hello', 'k1': 123}


## pickle
# pickle.dumps将数据通过特殊的形式转换成只有python语言能识别的字符串
p_str = pickle.dumps(data)
print(p_str)       #b'\x80\x03}q\x00(X\x02\x00\x00\x00k2q\x01X\x05\x00\x00\x00helloq\x02X\x02\x00\x00\x00k1q\x03K{u.'

# pickle.loads 读取pickle.dumps特殊处理后的数据并返回该对象
p_loads = pickle.loads(p_str)
print(p_loads)      #{'k2': 'hello', 'k1': 123}

# pickle.dump将数据通过特殊的形式转换成只有python语言识别的字符串，并写入文件
with open('file.pickle', 'wb') as fp:
    pickle.dump(data, fp)

# pickle.loads 从文件中读取pickle.dumps特殊处理后的数据并返回该对象
with open('file.pickle', 'rb') as fp:
    data_p_load = pickle.load(fp)
print(data_p_load)        #{'k2': 'hello', 'k1': 123}