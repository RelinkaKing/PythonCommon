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

def vectorStr2List(data):
    data = data.replace("(","").replace(")","")
    tmpResult = []
    for number in data.split(","):
        tmpResult.append(float(number))
    return tmpResult
def vector2Str(data):
    return str(tuple(data))