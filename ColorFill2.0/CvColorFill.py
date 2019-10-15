# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
import PIL.Image as Image
import matplotlib.pylab as plt
import scipy.misc
import random
import os
from PIL import ImageFont,ImageDraw
from xml.dom.minidom import Document
import datetime
import json
import re
import xlwt
from xlwt import Workbook
class CvColorFill:
    #tuplePat = re.compile(r'\(([0-9]*),(\s*[0-9]*),(\s*[0-9]*)\)', re.M|re.I)
    totalCount=0
    
    #colorPosDic = {}
    tmpColorPosDic = {}
    #使用自定义的字体，第二个参数表示字符大小
    font = ImageFont.truetype("3.ttf",50)
    randomColorList = []
    
    StartEndColor=[(237,58,99),(91,109,239)]
    isOutPutEveryPointImg = True
    targetPath=""
    outPutPngLevel = 3
    def __init__(self,basePath):
        self.targetPath = basePath+"\\output"
        self.mkdir(self.targetPath)
        self.initConfig()
        return
    
    def initConfig(self):
        if os.path.exists(self.targetPath+"\\config.json"):
            self.readConfig(self.targetPath+"\\config.json")
        else:
            self.writeConfig(self.targetPath+"\\config.json")
        return
    def getTupleFromStr(self,tstr):
        #t = re.sub("\D", ",",tstr).split(',')
        return tuple(int(x) for x in re.findall(r"\d+",tstr))
    def readConfig(self,path):
        with open(path,'r') as load_f:
            config_dict = json.load(load_f)
            print(config_dict)
            getListFromDic = lambda tmpDic : [self.getTupleFromStr(tmpDic[key]) for key in tmpDic]
            config_dict["FilterColor"] = getListFromDic(config_dict["FilterColor"])
            config_dict["StartEndColor"] = getListFromDic(config_dict["StartEndColor"])
            
            tffPath = self.getPath(self.targetPath)+config_dict["font"]
            if not os.path.exists(tffPath):
                print("tff not exists:"+tffPath)
                tffPath = None
                self.font = None
            else:
                self.font = ImageFont.truetype(font=tffPath,size = config_dict["fontSize"])
            self.StartEndColor = config_dict["StartEndColor"]
            self.randomColorList = config_dict["FilterColor"]
            self.isOutPutEveryPointImg = config_dict["isOutPutEveryPointImg"]
            self.outPutPngLevel = config_dict["outPutPngLevel"]
        return
    def writeConfig(self,path):
        self.randomColorList.append((91,109,239))
        self.randomColorList.append((237,58,99))
        self.randomColorList.append((255,255,255))
        self.randomColorList.append((0,0,0))
        self.randomColorList.append((255,0,255))
        self.randomColorList.append((255,255,0))
        
        self.StartEndColor=[(237,58,99),(91,109,239)]
        
        getKeys = lambda tmpList: [x for x in range(1,len(tmpList)+1,1)]
        itemToString = lambda tmpList: [str(x) for x in tmpList]
        config_dict = {"font":"3.ttf","fontSize":50,"outPutPngLevel":3,"isOutPutEveryPointImg":True,"StartEndColor":dict(zip(getKeys(self.StartEndColor),itemToString(self.StartEndColor))),
            "FilterColor":dict(zip(getKeys(self.randomColorList),itemToString(self.randomColorList)))}
        with open(path,"w") as f:
            json.dump(config_dict,f,indent="\t")
        return
    def getRandomColor(self):
        randomColor = lambda:(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        tmpColro = randomColor()
        while tmpColro in self.randomColorList:
            tmpColro = randomColor()
        self.randomColorList.append(tmpColro)
        
        return tmpColro
    def run(self):
            
            print(self.targetPath)
            if os.path.exists(self.targetPath):            
                files = []
                fileCount = 1
                for imgName in os.listdir(self.targetPath):
                    if imgName.lower().endswith(".png"):
                        files.append(imgName)
                #创建输出文件夹
                resultPath = self.targetPath +"\\"+datetime.datetime.now().strftime('%Y_%m%d_%H%M%S')
                self.mkdir(resultPath)

                for imgName in files:
                    currentImgPath = self.targetPath+"\\"+imgName
                    currentImgOutPutPath = resultPath+"\\"+self.getFileName(currentImgPath)
                    self.mkdir(currentImgOutPutPath)
                    currentResutImgPath = currentImgOutPutPath+"\\result_"+imgName
                    try:
                        print("progress: %4d  / %4d  -  %s" % (fileCount,len(files),imgName))
                        fileCount = fileCount + 1
                        self.fillWhiteArea(currentImgPath,currentResutImgPath)
                        print("refresh totalCount:"+str(self.totalCount))
                        print("drawNumberToImg")
                        self.drawNumberToImg(currentImgPath,currentResutImgPath)
                        if self.isOutPutEveryPointImg:
                            print("drawPoints")
                            self.drawPoints(currentImgPath,currentImgOutPutPath+"\\Points\\")
                        print("writeToXml")
                        self.writeToXml(currentImgOutPutPath,self.getFileName(currentImgPath))
                        print("writeToExcel")
                        self.writeToExcel(currentImgOutPutPath,self.getFileName(currentImgPath))
                        self.totalCount=self.totalCount+len(self.tmpColorPosDic)
                        self.tmpColorPosDic={}
                        print("refresh totalCount:"+str(self.totalCount))
                    except BaseException as e:
                        print(e)
                        print(e.__traceback__)
            else:
                print("dir not exists!")
            input("done!")
    def drawNumber(self,image,xy,text,color):
        xy = (xy[1],xy[0])
        #获得文字的offset位置
        offsetx,offsety=self.font.getoffset(text)
        width,height=self.font.getsize(text)
        #生成空白图像
        #im = Image.new("RGB",(50,50))　　　　　　
        draw = ImageDraw.Draw(image)
        #draw.rectangle([xy[0],xy[1],width,height],fill = (0,255,0))
        draw.text((xy[0]-offsetx-5,xy[1]-offsety-5), text=text, font=self.font,fill=color)  
        #im=np.array(im)
        #cv.rectangle(im,xy,wh,(255,255,255),1)
    def writeToExcel(self,outputPath,name):
        count = self.totalCount
        book = Workbook(encoding='utf-8')
        sheet1 = book.add_sheet(name,cell_overwrite_ok=True)
        sheet1.write(0,0,"Id")
        sheet1.write(0,1,"Color(rgb)")
        sheet1.write(0,2,"Pos")
        sheet1.write(0,3,"ColorBlock")
        tmpPngPath = outputPath+"\\tmpcc.bmp"
        rowCount = 1
        for xy in self.tmpColorPosDic:
            tmpColor = self.tmpColorPosDic[xy]
            tmpColor = (tmpColor[2],tmpColor[1],tmpColor[0])
            im = Image.new("RGB",(50,20),tmpColor)
            im.save(tmpPngPath,"bmp")
            sheet1.write(rowCount,0,str(count))
            sheet1.write(rowCount,1,str(tmpColor))
            
            sheet1.write(rowCount,2,str((xy[1],xy[0])))
            sheet1.insert_bitmap(tmpPngPath,rowCount,3)
            count = count+1
            rowCount= rowCount+1
        os.remove(tmpPngPath)
        # 保存Excel book.save('path/文件名称.xls')
        book.save(outputPath+"\\"+ name+'_result.xls')
        return
    def writeToXml(self,outputPath,name):
        doc = Document()
        orderlist = doc.createElement('orderlist')
        doc.appendChild(orderlist)
        count = self.totalCount
        for xy in self.tmpColorPosDic:
            order = doc.createElement('order')
            order.setAttribute("id",str(count))
            count = count +1
            order.setAttribute("xy",str((xy[1],xy[0])))
            tmpColor = self.tmpColorPosDic[xy]
            tmpColor = (tmpColor[2],tmpColor[1],tmpColor[0])
            order.setAttribute("color",str(tmpColor))
            orderlist.appendChild(order)
        with open(outputPath+"\\"+name+"_resulut.xml", 'wb') as f:
            f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))

    def fill_color_demo(self,image,xy,tartgetColor = None):
        """
        漫水填充
        """
        #warning: cv xy 颠倒

        #复制图片
        #copyImg=image.copy()
        copyImg=image
        #获取图片的高和宽
        h,w =image.shape[:2]
    
        #创建一个h+2,w+2的遮罩层，
        #这里需要注意，OpenCV的默认规定，
        # 遮罩层的shape必须是h+2，w+2并且必须是单通道8位，具体原因我也不是很清楚。
        mask=np.zeros([h+2,w+2],np.uint8)
        #mask[1:h+1,1:w+1] = image[:,:,0]
        #这里执行漫水填充，参数代表：
        #copyImg：要填充的图片
        #mask：遮罩层
        #(30,30)：开始填充的位置（开始的种子点）
        #(0,255,255)：填充的值，这里填充成黄色
        #(100,100,100)：开始的种子点与整个图像的像素值的最大的负差值
        #(50,50,50)：开始的种子点与整个图像的像素值的最大的正差值
        #cv.FLOODFILL_FIXED_RANGE：处理图像的方法，一般处理彩色图象用这个方法
        #FLOODFILL_MASK_ONLY
        yx = (xy[1],xy[0])
        if tartgetColor:
            cv.floodFill(copyImg,mask,yx,tartgetColor,(50,50,50), (100,100,100),cv.FLOODFILL_FIXED_RANGE)    
        else:
            tmpColor = self.getRandomColor()
            #self.totalCount = self.totalCount+1
            self.tmpColorPosDic[xy] = tmpColor
            cv.floodFill(copyImg,mask,yx,tmpColor,(50,50,50), (100,100,100),cv.FLOODFILL_FIXED_RANGE)

        return copyImg
        

    def fillWhiteArea(self,inputPath,outPath):
        image = cv.imread(inputPath)
        lastPosint = []
        w,h =image.shape[:2]
        print(w,h)
        for i in range(0,w,1):
            for j in range(0,h,1):
                transTuple = lambda x : (x[2],x[1],x[0])
                if transTuple(tuple(image[i,j])) in self.StartEndColor:
                    #print((i,j))
                    if (i,j) in lastPosint:
                        continue
                    lastPosint.append((i,j))
                    self.fill_color_demo(image,(i,j))
                    #cv.imwrite(path,image,[int(cv.IMWRITE_PNG_COMPRESSION),3])
        
        cv.imwrite(outPath,image,[int(cv.IMWRITE_PNG_COMPRESSION),self.outPutPngLevel])

    def drawPoints(self,sourcePath,savepath):
        #每个色块保存一张图
        im = cv.imread(sourcePath)
        count = self.totalCount
        self.mkdir(savepath)
        for xy in self.tmpColorPosDic:
            print("%d / %d" % (count-self.totalCount+1,len(self.tmpColorPosDic)) )
            copyImg=im.copy()
            self.fill_color_demo(copyImg,xy,self.tmpColorPosDic[xy])
            cv.imwrite(savepath+str(count)+".png",copyImg,[int(cv.IMWRITE_PNG_COMPRESSION),self.outPutPngLevel])
            target= Image.open(savepath+str(count)+".png")
            self.drawNumber(target,xy,str(count),(0,255,0))
            target.save(savepath+str(count)+".png", "png")
            count = count+1
        return 

    

    def drawNumberToImg(self,sourceImg,resultImg):
        output = self.getPath(resultImg)
        target = Image.open(resultImg)
        target.save(output+"source.png", "png")
        count = self.totalCount

        for xy in self.tmpColorPosDic:
            self.drawNumber(target,xy,str(count),(0,255,0))
            count = count+1
        target.save(output+"result_with_number.png", "png")


        target = Image.open(sourceImg)
        count = self.totalCount
        for xy in self.tmpColorPosDic:
            self.drawNumber(target,xy,str(count),self.tmpColorPosDic[xy])
            count = count+1
        target.save(output+"source_with_number.png", "png")
    


    def getPath(self,filePath):
        return os.path.dirname(filePath)+"\\"
    def getFileName(self,filePath):
        fileName = os.path.split(filePath)[1]
        fileName = os.path.splitext(fileName)[0]
        return fileName
    def getExten(self,filePath):
        return os.path.splitext(filePath)[1]
    def mkdir(self,path):
        if not os.path.exists(path):
            os.makedirs(path)

if __name__ == '__main__':
    
    cvColorFill = CvColorFill(os.getcwd())
    cvColorFill.run()

