# -*- coding: utf-8 -*-
import random
import os
from xml.dom.minidom import Document
import datetime
import json
import re
import xlrd


if __name__ == '__main__':
    datas={}
    workPath = "D:/pythonWorkSpaces/pythonlib/MyPythonLib/Util/datas/新旧标注对照表格.xlsx"
    book = xlrd.open_workbook(workPath)
    table = book.sheet_by_index(0)
    tittle = table.row_values(1)
    for i in range(2,table.nrows,1):
        item={}
        row = table.row_values(i) 
        count=0
        for x in tittle:
            if count<4:
                item[x+"_new"] = row[count]
            else:
                item[x+"_old"] = row[count]
            count+=1
        datas[i] = item

        # datas
        # print(row)
    jsonFile = "D:/pythonWorkSpaces/pythonlib/MyPythonLib/Util/datas/result.json"
    with open(jsonFile, 'w') as f:
        json.dump(datas, f,indent='\t',ensure_ascii=False)
    # json_str = json.dumps(datas)
    # with open(jsonFile, 'w') as f:
    #     json.dump(json_str, f,indent='\t')
