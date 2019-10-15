# -*- coding:utf-8 -*-
import xlrd
import os
import json
import shutil

def writeToLog(message):
    # with zip_file.open(names, pwd=pwd) as source,open(member, "wb") as target:
    #         shutil.copyfileobj(source, target)
    with open('../log.txt', 'a+',encoding='utf8') as f: #'w+' #'a+'
        f.write(message)
        f.write("\r\n")
    f.flush()
    f.close()
# {
#         "rs_ids": "19,2011,12,13,14,15,16,17,189,10",
#         "rv_ids": "",
#         "sm_name": "DaYuanJi_R",
#         "id": 46,
#         "rw_ids": "15,26,37,48,59,536",
#         "app_id": ""
# }

def createIDList():
        current_path = os.path.dirname(__file__)
        nounList = {}
        workbook = xlrd.open_workbook(current_path+'/MotorAnatomy.xlsx')
        #用索引取第2个sheet 
        booksheet = workbook.sheet_by_index(0)         
        print("总计："+str(booksheet.nrows))
        for i in range(0,booksheet.nrows,1):
                row = booksheet.row_values(i) 
                array=row[1].split(',')
                for muslue in array:
                        if muslue in nounList:
                                _list=nounList[muslue]+','+row[0]
                                nounList[muslue]=_list
                        else:
                                nounList[muslue]=row[0]

        writer = {'msg': 'success', 'code': 0, 'maxVersion': '1','List':[]}
        tmpList = []
        for muslue in nounList:
                temp={'rs_ids':nounList[muslue],'sm_name':muslue}
                tmpList.append(temp)
        writer['List'] = tmpList

        # article = json.dumps(writer, ensure_ascii=False)
        # print(article)
        with open("./my.json", 'w') as f:
                json.dump(writer, f,indent='\t')
        # json_str = json.dumps(datas)
        # with open(jsonFile, 'w') as f:
        #     json.dump(json_str, f,indent='\t')

        

def process():
        current_path = os.path.dirname(__file__)
        nounList = {}
        workbook = xlrd.open_workbook(current_path+'/test.xlsx')
        #用索引取第2个sheet 
        booksheet = workbook.sheet_by_index(1)         
        print("总计："+str(booksheet.nrows))
        tmp = ()
        tmpList = []
        keys = []
        values = []
        for i in range(0,booksheet.nrows,1):
                #读一行数据  
                row = booksheet.row_values(i) 
                nounList[row[1]]=row[0]

        for i in os.listdir(r"D:\UnityWorkSpace\Sport2.0\Assets\jiroudonghua\FBX"):
                print(i)
        if i.replace(".fbx","") in nounList:
                os.rename("./SearchTree/"+i,"./SearchTree/"+nounList[i.replace(".fbx","")]+".fbx")

if __name__ == '__main__':
        createIDList()
    # bubble_descending()  降序
    # alist = [54, 26, 93, 77, 44, 31, 44, 55, 20] 
    # print("原列表为：%s" % alist)
    # bubble_sort(alist)
    # print("新列表为：%s" % alist)

    # 结果如下：
    # 原列表为：[54, 26, 93, 77, 44, 31, 44, 55, 20]
    # 新列表为：[20, 26, 31, 44, 44, 54, 55, 77, 93]