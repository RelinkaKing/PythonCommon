# -*- coding:utf-8 -*-
import xlrd
import os
import json

nounList = []
try:
    workbook = xlrd.open_workbook('./产品数据.xlsx')
    #用索引取第一个sheet 
    booksheet = workbook.sheet_by_index(0)         
    print("总计："+str(booksheet.nrows))
    tmp = ()
    tmpList = []
    keys = []
    values = []
    for i in range(0,booksheet.nrows,1):
        #读一行数据  
        row = booksheet.row_values(i) 
        nounList.append(row[1])
    
except BaseException as e:
    print(e)

for i in os.listdir("./SearchTree"):
    #print(i)
    if i.replace(".xml","") not in nounList:
        os.remove("./SearchTree/"+i)