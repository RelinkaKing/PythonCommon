# -*- conding:utf-8 -*-
import re
import sys
import time
import uuid
from datetime import datetime
import pymysql

# 打开数据库连接
db = pymysql.connect("vesal", "root", "Vesal_oj123", "oj",charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)
cursor.execute("desc o_subject;")
for data in cursor.fetchall():
    print(data)

# SQL 查询语句
sql = "SELECT id,option_a,option_b,option_c,option_d,option_e,subject FROM o_subject"
try:
    tmpList = []
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        oid = row[0]
        a = row[1].strip()
        b = row[2].strip()
        c = row[3].strip()
        d = row[4].strip()
        e = row[5].strip()
        sub = row[6]
        if a==b or a==c or a==d or a==e or b==c or b==d or b==e or c==d or c==e or d==e:
            print("id:%d  \r\n\tqueation:%s \r\n\t-A- %s \r\n\t-B- %s \r\n\t-C- %s \r\n\t-D- %s \r\n\t-E- %s " % (oid, sub,a, b, c, d, e))
    # 打印结果
except:
    print ("Error: unable to fetch data")
# 关闭数据库连接
db.close()
