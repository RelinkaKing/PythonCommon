# -*- coding: utf-8 -*-
import random
import os
import time
import datetime
import re
import sys, os, pygame
from pygame.locals import *
import win32clipboard
import win32con
from win32api import GetSystemMetrics


imagepath = "img1.png"
pygame.init()# 初始化pygame
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 128)
WHITE = (255, 255, 255)
fontObj = pygame.font.Font('3.ttf', 35)
# 拖拽
drag=0
clock=pygame.time.Clock()
#选择
select=0 
select_rect=pygame.Rect(0,0,0,0)


#获取剪切板内容
def gettext():
    try:
        win32clipboard.OpenClipboard()
        t = win32clipboard.GetClipboardData(win32con.CF_TEXT)
        win32clipboard.CloseClipboard()
    except:
        return None
    return t


#写入剪切板内容
def settext(aString):

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_TEXT, aString.encode('UTF-8'))
    win32clipboard.CloseClipboard()

def showText(screen,data):
    global fontObj,GREEN,BLUE
    # 通过字体文件获得字体对象 
    textSurfaceObj = fontObj.render(data, True, GREEN, BLUE)
    # # 配置要显示的文字 
    #textRectObj = textSurfaceObj.get_rect()
    # # 获得要显示的对象的rect 
    #textRectObj.center = (200, 150)
    # # 设置显示对象的坐标 
    #screen.fill(WHITE)
    # # 设置背景 
    screen.fill((0,0,0), (0,0,1024,50))
    screen.blit(textSurfaceObj, (0,0,1024,50))



w,h=15,15
image=None
resetImage = None
imagerect=None
screenheight = GetSystemMetrics(1)-200
screen = pygame.display.set_mode((screenheight,screenheight+50))

if os.path.isfile(imagepath):
    image = pygame.image.load(imagepath)
    resetImage = image
    screen.blit(image,(0,50,screenheight,screenheight)) 
    imagerect = image.get_rect()
#text = pygame.text.SysFont("宋体",50)
#text_fmt = pygame.text.render("hello",1,(255,255,255))
showText(screen,"Hello")

#height
#width


# 绘制字体


print("hello4")
#screen.blit(text_fmt,(0,0))
while True:
    screen.fill(WHITE,(0,50,screenheight,screenheight))
    screen.blit(image,(0,50,screenheight,screenheight))
    tmpCp=None
    try:
        tmpCp = gettext().decode('UTF-8').replace("\\","/")
    except:
        pass
    if tmpCp and "." in tmpCp and tmpCp != imagepath:
        try:
            if os.path.isfile(tmpCp):
                image = pygame.image.load(tmpCp)
                resetImage = image
                screen.blit(image,(0,50,screenheight,screenheight)) 
                imagepath = tmpCp
        except:
            pass
    for event in pygame.event.get():
        if pygame.mouse.get_pressed() == (0,0,1):
            image = resetImage
            screen.blit(image,(0,50,screenheight,screenheight)) 
            pass
        if pygame.mouse.get_pressed() == (1,0,0):
            #move_ip
            #topleft
            print("press")
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                pass
        if event.type == MOUSEBUTTONDOWN:
            if event.button==1:
                #第一次点击，选择范围，未拖拽
                if select==0:
                    #获取鼠标的位置
                    pos_start = event.pos
                    select=2
   

            try:
                #up
                if event.button == 4:
                    imagerect = image.get_rect()
                    print(imagerect)
                    screen.fill((0,0,0), (0,50,screenheight,screenheight))
                    screen.blit(image[100:300,100:300],(0,50,int(imagerect.width*0.5),int(imagerect.width*0.5)))
                    pass
                #down
                if event.button == 5:
                    imagerect = image.get_rect()
                    screen.fill((0,0,0), (0,50,screenheight,screenheight))
                    screen.blit(image,(0,50,int(imagerect.width*1.1),int(imagerect.width*1.1)))
                    pass
            except BaseException as e:
                print(e)
                pass
            
            #return the X and Y position of the mouse cursor
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            if mouse_x<screenheight and mouse_y<screenheight+50:
                color = screen.get_at(pos)
                showText(screen,"color:"+str(color))
                #settext(str(color[0])+"	"+str(color[1])+"	"+str(color[2]))
                settext(str(color[0])+"\t"+str(color[1])+"\t"+str(color[2]))
        elif event.type==MOUSEBUTTONUP:
            if select==2:
                pos_stop=event.pos
                if pos_stop[0] == pos_start[0] and pos_stop[1] == pos_start[1]:
                    select=0
                else:
                    #得到鼠标的位置框
                    #mouse_pos=pygame.mouse.get_pos()
                    #pos_stop=mouse_pos
                    tmpsPos = (min(pos_start[0],pos_stop[0]),min(pos_start[1],pos_stop[1]))
                    tmpePos = (max(pos_start[0],pos_stop[0]),max(pos_start[1],pos_stop[1]))
                    # if pos_stop[0] <pos_start[0] and pos_stop[1] <pos_start[1]:
                    #     tmpPos = pos_start
                    #     pos_start = pos_stop
                    #     pos_stop=tmpPos
                    pos_start=tmpsPos
                    pos_stop=tmpePos
                    select_rect.left, select_rect.top = pos_start
                    select_rect.width, select_rect.height = pos_stop[0] - pos_start[0], pos_stop[1] - pos_start[1]

                    #获得裁剪的图像，将选好的图片copy出来
                    capture=screen.subsurface(select_rect).copy()
                    #得到选好图片的范围属性
                    #cap_rect=capture.get_rect()
                    image = pygame.transform.scale(capture, (screenheight, screenheight))
                    screen.blit(image,(0,50,screenheight,screenheight))
                    select=0

            # if event.button==1:
            #     # 第一次释放，结束选择
            #     if select==1 and drag==0:
            #         pos_stop=event.pos
            #         select=2
                    
            #     #第二次释放，结束拖拽
            #     if select==2 and drag==1:
            #         drag=2
                
    if  select:
        # #得到鼠标的位置框
        mouse_pos=pygame.mouse.get_pos()
        pos_stop=mouse_pos
        if pos_stop[0] == pos_start[0] and pos_stop[1] == pos_start[1]:
            pass
        else:
            #得到鼠标的位置框
            #mouse_pos=pygame.mouse.get_pos()
            #pos_stop=mouse_pos
            tmpsPos = (min(pos_start[0],pos_stop[0]),min(pos_start[1],pos_stop[1]))
            tmpePos = (max(pos_start[0],pos_stop[0]),max(pos_start[1],pos_stop[1]))
            pos_start=tmpsPos
            pos_stop=tmpePos
            select_rect.left, select_rect.top = pos_start
            select_rect.width, select_rect.height = pos_stop[0] - pos_start[0], pos_stop[1] - pos_start[1]
            #画矩形框 第一个元素是绘制那个面上，第二个是颜色，第三个是绘制矩形的范围，第四个是一个像素点的方框
            pygame.draw.rect(screen,(0,0,0),select_rect,1)
            # 拖拽剪裁的图像
    pygame.display.flip()

