# -*- coding: utf-8 -*-
import random
import os
from xml.dom.minidom import Document
import datetime
import json
import re
import xlrd


# workPath = "D:/pythonWorkSpaces/pythonlib/MyPythonLib/Util/datas/excelCompare"
# os.chdir(workPath)
if __name__ == '__main__':
    usedColor = []
    for i in os.listdir("./"):
        #print(i)
        if "result" in i and ".xls" in i:
            book = xlrd.open_workbook(i)
            while not book.sheet_loaded(0):
                pass
            table = book.sheet_by_index(0)

            for x in table.col(1,start_rowx=1):
                
                usedColor.append(tuple(int(x) for x in re.findall(r"\d+",x.value)))
                #print(x.value)

    usedColor.append((0,0,0))
    for i in os.listdir("./"):
        #print(i)
        if "result" in i and ".xls" in i:
            pass
        elif ".xls" in i:
            book = xlrd.open_workbook(i)
            table = book.sheet_by_index(0)
            usedColor2 = []
            usedColor3 = []
            #usedColor2.append((0,0,0))
            for i in range(2,table.nrows,1):
                row = table.row_values(i) 
                try:
                    start = (int(row[3]),int(row[4]),int(row[5]))

                    # if start not in usedColor2:
                    #     usedColor2.append(start)
                    # elif start != (0,0,0):
                    #     print(i-1,row[0],"start repeat:",start)    
                    #     usedColor3.append(start)

                    if start not in usedColor:
                        print(i-1,row[0],"start",start)
                except:
                    pass

                try:
                    start = (int(row[6]),int(row[7]),int(row[8]))
                    # if start not in usedColor2:
                    #     usedColor2.append(start)
                    # elif start != (0,0,0):
                    #     print(i-1,row[0],"start repeat:",start)
                    #     usedColor3.append(start)  

                    if start not in usedColor:
                        print(i-1,row[0],"end",start)
                except:
                    pass
            print("======================down============================")
    input("enter any key to quit!")
    # print(usedColor3)
    # usedColor = usedColor3
    # usedColorDic = {}
    # for i in range(2,table.nrows,1):
    #     row = table.row_values(i) 
    #     try:
    #         start = (int(row[3]),int(row[4]),int(row[5])) 
    #         if start in usedColor:
    #             if start not in usedColorDic:
    #                 usedColorDic[start] = []
    #             usedColorDic[start].append(row[0])
    #             print(i-1,row[0],"rrrrr",start)
    #     except:
    #         pass

    #     try:
    #         start = (int(row[6]),int(row[7]),int(row[8]))
    #         if start in usedColor:
    #             if start not in usedColorDic:
    #                 usedColorDic[start] = []
    #             usedColorDic[start].append(row[0])
    #             print(i-1,row[0],"rrrrr",start)
    #         #     print(i-1,row[0],"end",start)
    #     except:
    #         pass
    # print(usedColorDic)
    # for key in usedColorDic:
    #     print(key)
    #     print(usedColorDic[key])