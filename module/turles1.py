'''验证码生成器'''
# import turtle
# import time
# turtle.color('red','yellow')
# turtle.begin_fill()
# for _ in range(50):
#     turtle.forward(200)
#     turtle.left(170)
# turtle.end_fill()
# turtle.mainloop()
import os
import pygame
from pygame.locals import *
from random import *

def yanzhengma():
    pygame.init()
    l = ['r','o','o','t','a',1,2,3,4,5,6,7,8,9,0]
    R = sample(l,4)
    # print(R)
    text = u'%s'%R
    # print(text)
    font = pygame.font.SysFont('Microsoft YaHei',64)
    ftext = font.render(text,True,(65,83,130),(255,255,255))

    pygame.image.save(ftext,'./yanzhengma.png')

    return R
