import urllib.request
import re


def getHtml(url):
    html=urllib.request.urlopen(url).read()
    return html


# def getImg(html):
#     r=r'"thumbURL":"(https://img.+?\.jpg)"' #定义正则
#     imglist=re.findall(r,html)
#     return imglist

# html=str(getHtml("http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%A3%81%E7%BA%B8&ct=201326592&lm=-1&v=flip"))
# print("https://baike.baidu.com/item/%E4%B9%9D%E9%98%B3%E7%A5%9E%E5%8A%9F/1782?fr=aladdin")
# print(getImg(html))


# import re
# import urllib.request
# def getHtml(url):
#   html=urllib.request.urlopen(url).read()
#   return html
def getImg(html):
  r=r'"thumbURL":"(http://img.+?\.jpg)"' #定义正则
  imglist=re.findall(r,html)
  return imglist
html=str(getHtml("http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%A3%81%E7%BA%B8&ct=201326592&lm=-1&v=flip"))
print(getImg(html))
