# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Img
import chardet
import codecs
import urllib
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Max, Min, Count
from django.http import HttpResponse
import json
# Create your views here.
# 图片上传函数

#局部使用
#@csrf_protect
#局部禁用csrf
#@csrf_exempt
def uploadImg(request): 
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.save()
    return render(request, 'ImageUpload/imgupload.html')
def showCurrentScreenCap(request,capid):
    tmp = Img.objects.aggregate(Max('id'))
    #dict
    tmpmax = tmp['id__max']
    if tmpmax != capid:
        capid = tmpmax
    result = get_object_or_404(Img, pk=capid)
    return render(request, 'ImageUpload/currentShow.html', {'capid': tmpmax,'img':result})
def showImg(request):
    # 从数据库中取出所有的图片路径
    imgs = Img.objects.all() 
    # print(type(Img.objects))
    # help(Img.objects)
   
    # results = []
    # #f = codecs.open('d:/1.txt','w','utf-8')
    # for img in imgs:
    #     print(urllib.parse.unquote(img.img_url.url))
    #     results.append(MyImage(urllib.parse.unquote(img.img_url.url)))
    # #    f.write(img.img_url.url)
    context = {
        'imgs' : imgs
    }
    return render(request, 'ImageUpload/showImg.html', context)
def getCurrentimage(request):
    tmp = Img.objects.aggregate(Max('id'))
    #dict
    tmpmax = tmp['id__max']
    result = get_object_or_404(Img, pk=tmpmax)
    
    #parent_path = path.dirname(d)
    imagepath = result.img_url.url
    #image_data = open(imagepath,"rb").read()
    resp = {'imagepath': imagepath}
    return HttpResponse(json.dumps(resp), content_type="application/json")
    #return HttpResponse(image_data,content_type="image/png")

def props(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not callable(value) and not name.startswith('_'):
            pr[name] = value
    return pr

class MyImage():
    def __init__(self, url):
            self.img_url = Img_url(url)
            return 
class Img_url():
    def __init__(self,url):
        self.url = url
        return 