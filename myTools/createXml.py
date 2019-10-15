# -*- coding:utf-8 -*-
import xlrd
import os


print(os.getcwd())

head = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<document>"
print(head)
foot = "</document>"
print(foot)
filePath = "./tmpLib.xml"

f = open(filePath,'w',encoding='utf-8')
f.write(head)
f.write("\n")

try:
    workbook = xlrd.open_workbook('./题库练习题目.xlsx')
    print(workbook.sheet_names())
    #用索引取第一个sheet 
    booksheet = workbook.sheet_by_index(0)         
    print(booksheet.nrows)
    n = 1
    baseId = "1_"
    for i in range(1,52,1):
        question = []
        #读一行数据  
        row = booksheet.row_values(i) 
        question.append("<Question qid=\""+baseId+str(n)+"\">\n")
        n+=1
        question.append("<q>"+row[1]+"</q>\n")
        question.append("<questionType>model</questionType>\n")
        question.append("<modelName>bone</modelName>\n")
        question.append("<highLightName>"+row[ord(row[2])-62]+"</highLightName>\n")
        question.append("<cameraParameter cameraBackPos=\"(0,0,0)\" cameraBackRot=\"(0,0,0)\" cameraDistance=\"-50\" cameraMinDis=\"0\" cameraMaxDis=\"0\"></cameraParameter>\n")
        a = 1
        for x in range(3,8,1):
            if x == ord(row[2])-62 :
                question.append("<right1>"+row[x]+"</right1>\n")
            else:
                question.append("<a"+str(a)+">"+row[x]+"</a"+str(a)+">\n")
                a+=1
        question.append("</Question>\n")
        f.writelines(question)
except BaseException as e:
    print(e)


f.write(foot)
f.flush()
f.close()

