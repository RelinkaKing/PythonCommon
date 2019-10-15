# -*- coding: utf-8 -*-
import json

def wirteJsonToFile(jsonData,file):
    # Writing JSON data
    with open(file, 'w') as f:
        json.dump(jsonData, f,indent='\t')
def wirteObjToFile(Obj,file):
    # Writing JSON data
    with open(file, 'w') as f:
        json.dump(objToJson(Obj), f,indent='\t')

def readJsonFromFile(file):
    # Reading data back
    with open(file, 'r') as f:
        data = json.load(f)
    return data

def objToJson(Obj):
    json_str = json.dumps(Obj)
    return json_str
def JsonToObj(json_str):
    obj = json.loads(json_str)
    return obj