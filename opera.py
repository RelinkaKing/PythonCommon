# -*- coding:utf-8 -*-
import os
import shutil
import re
os.chdir(".")
#for i in os.listdir('./'):
#    print(i)
preReg = re.compile(r'(.*)李哲微课(.*?)—.*', re.M|re.I)
preReg2 = re.compile(r'(.*) modelId=\"(.*?)\".*', re.M|re.I)
for dirpath,dirnames,filenames in os.walk("."):
    for file in filenames:
            fullpath=os.path.join(dirpath,file)
            #print(fullpath)
            if("ppt_control.xml" in fullpath):
                #print(dirpath)
                tmpList = []
                matchObj = preReg.match(dirpath)
                print(matchObj.group(2))
                with open(fullpath,encoding='utf-8') as f:
                    line = f.readline()
                    while line:
                        if "Model" in line:
                            matchObj = preReg2.match( line)
                            if matchObj.group(2) not in tmpList:
                                print(matchObj.group(2))
                                tmpList.append(matchObj.group(2))
                        line = f.readline()
            