# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import *
import pygame


class Screen(pygame.sprite.Sprite):

    def __init__(self, position, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.width, self.height = bg_size[0], bg_size[1]

        # 设置子弹对象
        self.image = pygame.image.load('images/image_1.jpg').convert_alpha()
        self.images = []
        self.images.extend([
            pygame.image.load('images/image_2.jpg').convert_alpha(),
            pygame.image.load('images/image_3.jpg').convert_alpha(),
            pygame.image.load('images/image_4.jpg').convert_alpha(),
            pygame.image.load('images/image_5.jpg').convert_alpha()

        ])

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.speed = 1
        self.action = False

    def move(self):
        self.rect.top += self.speed

        if self.rect.bottom > self.height:
            self.action = True


# class Ground(pygame.sprite.Sprite):

#     def __init__(self, bg_size):
#         pygame.sprite.Sprite.__init__(self)

#         self.image = pygame.image.load(
#             'images/img_cloud_1.png').convert_alpha()
#         self.images = pygame.image.load(
#             'images/img_cloud_2.png').convert_alpha()
#         self.image_s = choice([self.image, self.images])
#         self.image_rect = self.image_s.get_rect()
#         self.width, self.height = bg_size[0], bg_size[1]
#         self.image_rect.left, self.image_rect.bottom = choice([(self.width - self.image_rect.width // 2), (0 - self.image_rect.width // 2)]),\
#             randint(-50, -10)
#         self.speed = 1

#     def move(self):
#         if self.image_rect.top < self.height:
#             self.image_rect.top += 1
#         else:
#             self.reset()

#     def reset(self):

#         self.image_s = choice([self.image, self.images])
#         self.image_rect = self.image_s.get_rect()
#         self.image_rect.left, self.image_rect.bottom = randint(0 - self.image_rect.width // 2, self.width - self.image_rect.width // 2),\
#             randint(-50, -10)
