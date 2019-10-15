# -*- coding: utf-8 -*-
import random
import os
import time
import datetime
import json
import re
import http.client
import requests 
import zipfile
import lzma
from xml.dom.minidom import Document
from xml.dom.minidom import parse
import xml.dom.minidom
import uuid
import shutil
import hashlib

def readXmlDoc(xmlPath):
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(xmlPath)
    #DOMTree.documentElement
    return DOMTree

def getAllTags(doc,tagName):
    return doc.getElementsByTagName(tagName)


    