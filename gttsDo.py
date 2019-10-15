# -*- coding:utf-8 -*-
from gtts import gTTS

#import os
#os.getcwd()
#os.listdir('.')
#os.path.join(os.getcwd(),os.listdir('.')[1])
#linelist=[l.strip('\n') for l in file.readlines()]
file = open('./target.txt')
i = 1
result =""
while 1:
    line = file.readline()
    if not line:
        break
    print(line.strip('\n'))
    print(len(line))
    result+=line
    i+=1
#result 生成文章
tts = gTTS(text=result, lang='en')
#tts.save('audio'+str(i)+'.mp3')
tts.save('artical2.mp3')
file.close()
#%hist -f gttsDo.py