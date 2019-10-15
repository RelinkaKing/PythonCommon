# -*- conding:utf-8 -*-
import re
import sys
import time
import uuid
from datetime import datetime

import requests
from bs4 import BeautifulSoup

import pymssql
userType =input('输入账号类型（0：手机，1：邮箱）：\n').strip()

#conn = pymssql.connect(host='localhost\SQLEXPRESS',database='Ruanyi_VesalDB',user='sa',password='sqlserver')
conn = pymssql.connect(host='118.190.91.154',database='Ruanyi_VesalDB',user='sa',password='RykjVesal5188')
cur = conn.cursor()
if userType == "1":
    email = input('输入需要修改的邮箱：\n').strip()
    print('正在查询'+str(email)+'用户信息·····')
    cur.execute("SELECT COUNT(1) FROM  [Ruanyi_VesalDB].[dbo].[Ry_Vip_Member] where [MemberEmail] = '%s'" % email)
if userType == "0":
    phoneNumber = input('输入需要修改的手机号：\n').strip()
    if len(str(phoneNumber)) != len(str(13572994164)):
        print(phoneNumber+"手机号长度不正确！")
        sys.exit()
    print('正在查询'+str(phoneNumber)+'用户信息·····')
    cur.execute("SELECT COUNT(1) FROM  [Ruanyi_VesalDB].[dbo].[Ry_Vip_Member] where [MemberTel] = '%s'" % phoneNumber)

#[MemberEmail]
#18313053781
#13572994164
#18092058670
# [Ruanyi_VesalDB].[dbo].[Ry_Vip_Member]
#[Ruanyi_VesalDB].[dbo].[Ry_Store_Order]
num = cur.fetchall()
if userType == "1":
    print('检测 %s 用户信息记录：%d 条' % (str(email),num[0][0]))
if userType == "0":
    print('检测 %s 用户信息记录：%d 条' % (str(phoneNumber),num[0][0]))

if num[0][0] != 1:
    print("用户信息查询不正确！")
    sys.exit()

if userType == "1":
    print('检测 %s 用户信息记录：%d 条' % (str(email),num[0][0]))
    cur.execute("SELECT [MemberId],[MemberName],[MemberTel],[AddTime] FROM [Ruanyi_VesalDB].[dbo].[Ry_Vip_Member] where [MemberEmail] = '%s'" % email)
if userType == "0":
    print('检测 %s 用户信息记录：%d 条' % (str(phoneNumber),num[0][0]))
    cur.execute("SELECT [MemberId],[MemberName],[MemberTel],[AddTime] FROM [Ruanyi_VesalDB].[dbo].[Ry_Vip_Member] where [MemberTel] = '%s'" % phoneNumber)
    
memInfo = cur.fetchall()
#[('96FBBA30-A1BC-4BD3-A463-B82DC967FD70', '187107', '13572994164', datetime.datetime(2017, 9, 21, 8, 45, 51, 867000))]
#print(memInfo)

pattern = r'\[|\]'
#tuple 转list
list1 = memInfo[0]
list1 = list(list1)
list1[3] = str(list1[3])
#登陆码赋值
MemberId = list1[0]
if len(MemberId) != len('96FBBA30-A1BC-4BD3-A463-B82DC967FD70'):
    print("用户MemberId查询不正确！")
    sys.exit()
print("MemberId:%s" % MemberId)
#分组组合字典
list2 = re.sub(pattern,'','[MemberId],[MemberName],[MemberTel],[AddTime]').split(',')
z = zip(list2,list1)
print("=====================用户信息=============================")
print(*(str(l)+"\n" for l in z))
print("=========================================================")


cur.execute("SELECT [OrderId],[OrderNo],[MemberId],[ConsumeRuleId],[PaymentType],[ThirdPartyOrderNo],[OrderTotal],[ActualTotal],[OrderState],[Remark],[CreateTime],[PaymentTime],[FinishTime],[MemberIsDel],[AddTime] FROM [Ruanyi_VesalDB].[dbo].[Ry_Store_Order] where [MemberId] = '%s'" % MemberId)
memInfo = cur.fetchall()
list2 = re.sub(pattern,'','[OrderId],[OrderNo],[MemberId],[ConsumeRuleId],[PaymentType],[ThirdPartyOrderNo],[OrderTotal],[ActualTotal],[OrderState],[Remark],[CreateTime],[PaymentTime],[FinishTime],[MemberIsDel],[AddTime]').split(',')
#tuple 转list
print("=====================用户购买信息=============================")
for tmpList in memInfo:
    list1 = tmpList
    list1 = list(list1)
    list1[3] = str(list1[3])
    z = zip(list2,list1)
    print(*(str(l)+"\n" for l in z))
print("=============================================================")

cur.execute("SELECT [StructId] from [Ruanyi_VesalDB].[dbo].[Ry_Store_OrderDetails] group by [StructId]")
StructIds = []
for tmpId in cur.fetchall():
    StructIds.append(tmpId[0])

print("===========================所有收费项目==============================")
print(StructIds)
print("=============================================================")
print("========================已购买项目============================")
cur.execute("SELECT [StructId] FROM [Ruanyi_VesalDB].[dbo].[Ry_Vip_MemberBuyDurstion] where [MemberId] like '%s'" % MemberId)
boughtList = []
for tmpLine in cur.fetchall():
    tmpLine = list(tmpLine)
    boughtList.append(tmpLine[0])
print(boughtList)
# print("------------------------MemberBuyDurstion-----------------------------------")
# cur.execute("SELECT * FROM [Ruanyi_VesalDB].[dbo].[Ry_Vip_MemberBuyDurstion] where [MemberId] like '%s'" % MemberId)
# for tmpLine in cur.fetchall():
#     tmpLine = list(tmpLine)
#     for i in range(0,len(tmpLine),1):
#         if type(tmpLine[i]) is datetime:
#             tmpLine[i] = str(tmpLine[i])
#     print(str(tmpLine))
# conn.close()
# sys.exit()

print("=============================================================")
tmpOid = time.strftime('%Y%m%d-%H%M-%S-', time.localtime()) + str(uuid.uuid4())[0:10]
print(tmpOid)
for stid in StructIds :
    #心
    #if stid != "C90000BA-26F7-48B5-83B7-424B75B014B8":
    #    continue
    #头部
    if stid != "6D77A8FE-EE24-4B54-81C6-EB448B9F69E1":
       continue
    #运动pro
    #if stid != "6A0EBC37-FB52-44D6-BF47-596EA5B6F16A":
    #    continue
    if stid in boughtList:
        continue
    tmpOdId = time.strftime('%Y%m%d-%H%M-%S-', time.localtime()) + str(uuid.uuid4())[0:10]
    cur.execute("INSERT [Ruanyi_VesalDB].[dbo].[Ry_Store_OrderDetails] ([OrderDetailsId],[OrderId],[StructId],[BuyNumber],[UnitPrice],[TotalAmount]) VALUES ('%s','%s','%s','%d','%d','%d')" % (tmpOdId,tmpOid,stid,1,1,1))
for stid in StructIds:
    #if stid != "C90000BA-26F7-48B5-83B7-424B75B014B8":
    #    continue
    if stid != "6D77A8FE-EE24-4B54-81C6-EB448B9F69E1":
        continue
    #if stid != "6A0EBC37-FB52-44D6-BF47-596EA5B6F16A":
    #    continue
    if stid in boughtList:
        continue
    tmpBuyId = time.strftime('%Y%m%d-%H%M-%S-', time.localtime()) + str(uuid.uuid4())[0:10]
    cur.execute("INSERT [Ruanyi_VesalDB].[dbo].[Ry_Vip_MemberBuyDurstion] Values('%s','%s','%s',dateadd(yy,-1,getdate()),dateadd(yy,+1,getdate()),getdate())" % (tmpBuyId,MemberId,stid))


strTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
cur.execute("INSERT [Ruanyi_VesalDB].[dbo].[Ry_Store_Order] ([OrderId],[OrderNo],[ThirdPartyOrderNo],[MemberId],[PaymentType],[OrderTotal],[ActualTotal],[OrderState],[MemberIsDel],[CreateTime],[PaymentTime],[FinishTime],[AddTime]) VALUES ('%s','%s','%s','%s','%d','%d','%d','%d','%d',getdate(), getdate(),getdate(),getdate())" % (tmpOid,'Android2018031323402711191','Android2018031323402711191',MemberId,1,1,1,2,1))
#提交
conn.commit()

print("=====================新插入订单=============================")
cur.execute("SELECT * from [Ruanyi_VesalDB].[dbo].[Ry_Store_Order] where [OrderId] like '%s'" % tmpOid)
print(cur.fetchall())
print("------------------------OrderDetails------------------------------------")
cur.execute("SELECT * from [Ruanyi_VesalDB].[dbo].[Ry_Store_OrderDetails] where [OrderId] like '%s'" % tmpOid)
for tmpLine in cur.fetchall():
    tmpLine = list(tmpLine)
    for i in range(0,len(tmpLine),1):
        if type(tmpLine[i]) is datetime:
            tmpLine[i] = str(tmpLine[i])
    print(str(tmpLine))
print("------------------------MemberBuyDurstion-----------------------------------")
cur.execute("SELECT * FROM [Ruanyi_VesalDB].[dbo].[Ry_Vip_MemberBuyDurstion] where [MemberId] like '%s'" % MemberId)
for tmpLine in cur.fetchall():
    tmpLine = list(tmpLine)
    for i in range(0,len(tmpLine),1):
        if type(tmpLine[i]) is datetime:
            tmpLine[i] = str(tmpLine[i])
    print(str(tmpLine))
#dateadd(yy,1,dt)
print("===========================================================")
print("===========================结果验证MemberBuyDurstion是否有重复项目========================")
cur.execute("SELECT [MemberId],[StructId],count([StructId]) as num FROM [Ruanyi_VesalDB].[dbo].[Ry_Vip_MemberBuyDurstion] GROUP BY [MemberId],[StructId] having count([StructId]) > 1 order by num desc")
print(len(cur.fetchall()))
print("=====================================================================")
conn.close()
# SELECT TOP (1000) [OrderDetailsId]
#       ,[OrderId]
#       ,[StructId]
#       ,[UnitPrice]
#       ,[BuyNumber]
#       ,[TotalAmount]
#       ,[AddTime]
#   FROM [Ruanyi_VesalDB].[dbo].[Ry_Store_OrderDetails]
#   where [OrderId] like '20180417-0927-02-f180cc10-1'

# SELECT TOP (1000) [OrderId]
#       ,[OrderNo]
#       ,[MemberId]
#       ,[ConsumeRuleId]
#       ,[PaymentType]
#       ,[ThirdPartyOrderNo]
#       ,[OrderTotal]
#       ,[ActualTotal]
#       ,[OrderState]
#       ,[Remark]
#       ,[CreateTime]
#       ,[PaymentTime]
#       ,[FinishTime]
#       ,[MemberIsDel]
#       ,[AddTime]
#   FROM [Ruanyi_VesalDB].[dbo].[Ry_Store_Order]
#   where [OrderId] like '20180417-0925-12-ced163b2-1'

# SELECT TOP (1000) [BuyDurstionId]
#       ,[MemberId]
#       ,[StructId]
#       ,[StartTime]
#       ,[EndTime]
#       ,[UpdateTime]
#   FROM [Ruanyi_VesalDB].[dbo].[Ry_Vip_MemberBuyDurstion]
#   where [MemberId] = '2B2BD02C-02B9-4E49-97AD-C101EF84EB6D'