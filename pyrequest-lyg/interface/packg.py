import pygame
import sys
from pygame.locals import *

#初始化pygame
pygame.init()

size = width, height = 600,400
speed = [-2,1]
bg = (255,255,255)

clock = pygame.time.Clock()

fullscreen = False

#创建窗口大小
screen = pygame.display.set_mode(size,RESIZABLE)

#设置窗口标题
pygame.display.set_caption("初次见面")

#加载图片
odog = pygame.image.load("dog.png")
dog = odog

#设置放大缩小比例
ratio = 1.0

#获得图像位置矩形
odog_rect = odog.get_rect()
position = dog_rect = odog_rect

l_head = odog
r_head = pygame.transform.flip(odog,True,False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-1,0]
                odog = l_head
            if event.key == K_RIGHT:
                speed = [1, 0]
                odog = r_head
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0,1]
            #全屏（F11）
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((1920,1080),FULLSCREEN | HWSURFACE)
                    width,height = 1920,1080
                else:
                    screen = pygame.display.set_mode(size)
        if event.type == VIDEORESIZE:
            size = event.size
            width,height = size
            print(size)
            screen = pygame.display.set_mode(size, RESIZABLE)

    #移动图片
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        #翻转图像
        odog = pygame.transform.flip(odog,True,False)
        #反向移动
        speed[0] = -speed[0]
    if position.top <0 or position.bottom > height:
        speed[1] = -speed[1]
    #填充背景
    screen.fill(bg)
    #更新图像
    screen.blit(odog,position)
    #更新界面
    pygame.display.flip()
    #延迟10ms
    #pygame.time.delay(10)
    clock.tick(100) #clock.tick 控制帧率