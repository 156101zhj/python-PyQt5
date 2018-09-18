# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pygame


class Background(pygame.sprite.Sprite):

    # 初始化地图

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        # 加载相同张图片资源,做交替实现地图滚动
        self.image1 = pygame.image.load(
            "images/background1.png").convert_alpha()
        self.image2 = pygame.image.load(
            "images/background1.png").convert_alpha()
        # 保存场景对象
        # self.bg_screen = bg_screen
        # 辅助移动地图
        self.y1 = 0
        self.y2 = -self.bg_size[1]

    # 计算地图图片绘制坐标
    def move(self):
        self.y1 = self.y1 + 1
        self.y2 = self.y2 + 1
        if self.y1 >= self.bg_size[1]:
            self.y1 = 0
        if self.y2 >= 0:
            self.y2 = -self.bg_size[1]
        self.blit(self.image1, (0, self.y1))
        self.blit(self.image2, (0, self.y2))

    # 绘制地图的两张图片
