# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'ImageUpload'
urlpatterns = [
    path('uploadImg/', uploadImg,name="uploadImg"),
    path('showImg/', showImg),
    path('<int:capid>/',showCurrentScreenCap,name="showcap"),
    path('currentcap',getCurrentimage,name="currentcap"),
]