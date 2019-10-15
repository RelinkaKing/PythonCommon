import math


class TestClass:
    def Fun(self):
            a=int(input("a"))
            disc=math.sqrt(a)
dq={'a':32,'b':325}
print(dq['b'])
c="tom"
print(c)
print (math.cos(30))
"""
#print("this dir elem is -10.3f"%dq['a'])
print(type(c))
def PrintName(name,strName):
    print(name)
PrintName(12,15)

from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
obj=BeautifulSoup(html,"html.parser")
#格式定义   src   ：  ./pages_files/img*.jpg
images=obj.findAll("img",{"src":re.compile("\.\/page3_files\/img.*\.jpg")})
for image in images:
    print(image['src'])

tags=obj.findAll(lambda parms:len(parms.attrs)==2)
for tag in tags:
    print(tag)
    """
f=lambda a,b,c:a+b+c
print (lambda x,y:x*y,range(1,10))

def action(x):
    a=lambda y:x+y
    return a(3)
b=lambda x:lambda y:x+y
actionCopy=b(3)
print(actionCopy(2)) #2+3
print((b(2))(3)) #2+2
print(action(2))

v=77
c=repr(v)
b=float(v)
print(type(c))
print(type(v))
print(type(b))
stringnam="www.vesal.cn"
print(set(stringnam))
print(list(stringnam))
print(tuple(stringnam))
'列表和元组的容器嵌套使用'
listTuple=[('a',3),('b',5),('c',5)]
print(listTuple)
print(dict(listTuple))      #'字典'

print(bin(0xAB))#进制转换
print(32>>2)#移位
print(~101)#按位取反
print(8**8)#幂
print(math.pow(8,8))#math 求幂
print(('a',3) in listTuple )#判断  in 关键字用法
print(listTuple [('a',3):])#