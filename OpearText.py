#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xxx

import os

def writeToLog(message):
    # with zip_file.open(names, pwd=pwd) as source,open(member, "wb") as target:
    #         shutil.copyfileobj(source, target)
    with open('../log.txt', 'a+',encoding='utf8') as f: #'w+' #'a+'
        f.write(message)
        f.write("\r\n")
    f.flush()
    f.close()

def readTxt(path):
    file = open('./modelsV2.txt')
    file.close()
    while 1:
        line=file.readline()
        if not line:
            break
        print(line)
# 切换工作路径
def path_opera():
    # 查看当前工作目录
    print(os.getcwd())
    # 如果路径不存在
    if not os.path.exists(tffPath):
        os.makedirs(targetPath)
    # 修改当前工作目录到
    os.chdir(".")
    file = open(r'C:\Users\Relinka\Desktop\models.xml', 'w', encoding='utf-8')
    while 1:
        line = file.readline()
        line,_ =p.subn("",line)
        line = line.replace("\"","").strip('\n')
        line = str.lower(line)
        if line == "" or (not line) or (line in exitsList):
            continue

# 冒泡排序降序
def bubble_descending():
    lists=[54, 26, 93, 77, 44, 31, 44, 55, 20]
    n=len(lists)
    for j in range(n-1):
        print(j)
        for i in range(0,n-1-j):
            if lists[i]<lists[i+1]:
                lists[i],lists[i+1]=lists[i+1],lists[i]
    print("lists：%s" %lists)
    print(lists)
# 升序
def bubble_sort(alist):
    # 结算列表的长度
    n = len(alist)
    # 外层循环控制从头走到尾的次数
    for j in range(n - 1):
        # 用一个count记录一共交换的次数，可以排除已经是排好的序列
        count = 0
        # 内层循环控制走一次的过程
        for i in range(0, n - 1 - j):
            # 如果前一个元素大于后一个元素，则交换两个元素（升序）
            if alist[i] > alist[i + 1]:
                # 交换元素
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                # 记录交换的次数
                count += 1
        # count == 0 代表没有交换，序列已经有序
        if 0 == count:
            break

# if __name__ == '__main__':
    # bubble_descending()  降序
    # alist = [54, 26, 93, 77, 44, 31, 44, 55, 20] 
    # print("原列表为：%s" % alist)
    # bubble_sort(alist)
    # print("新列表为：%s" % alist)

    # 结果如下：
    # 原列表为：[54, 26, 93, 77, 44, 31, 44, 55, 20]
    # 新列表为：[20, 26, 31, 44, 44, 54, 55, 77, 93]