import pygame
import sys
from pygame.locals import *
pygame.init()
 
size=width,height=800,600
 
 
bg=(255,255,255)
clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)
 
 
pygame.display.set_caption('suguoliang')
turtle=pygame.image.load('img1.png')
position=turtle.get_rect()
position.center = width // 2, height // 2
#选择
select=0 
select_rect=pygame.Rect(0,0,0,0)
# 拖拽
drag=0
 
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        elif event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                #第一次点击，选择范围，未拖拽
                if select==0 and drag==0:
                    #获取鼠标的位置
                    pos_start = event.pos
                    select=1
 
                #第二次点击，推拽图像，    
                elif select==2 and drag==0:
                    #获得裁剪的图像，将选好的图片copy出来
                    capture=screen.subsurface(select_rect).copy()
                    #得到选好图片的范围属性
                    cap_rect=capture.get_rect()
                    drag=1
 
                #第三次点击，初始化    
                elif select==2 and drag==2:
                    select=0
                    drag=0
 
 
        elif event.type==MOUSEBUTTONUP:
            if event.button==1:
                # 第一次释放，结束选择
                if select==1 and drag==0:
                    pos_stop=event.pos
                    select=2
                    
                #第二次释放，结束拖拽
                if select==2 and drag==1:
                    drag=2
                    
                            
 
    screen.fill(bg)
    screen.blit(turtle,position)
 
    
    if  select:
        #得到鼠标的位置框
        mouse_pos=pygame.mouse.get_pos()
        if select==1:
            pos_stop=mouse_pos
        select_rect.left, select_rect.top = pos_start
        select_rect.width, select_rect.height = pos_stop[0] - pos_start[0], pos_stop[1] - pos_start[1]
        #画矩形框 第一个元素是绘制那个面上，第二个是颜色，第三个是绘制矩形的范围，第四个是一个像素点的方框
        pygame.draw.rect(screen,(0,0,0),select_rect,1)
        # 拖拽剪裁的图像
    if drag:
        if drag==1:
            #使鼠标的位置位于矩形的中间
           cap_rect.center=mouse_pos
        screen.blit(capture,cap_rect)
    
    pygame.display.flip()