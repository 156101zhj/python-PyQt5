# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pygame
import time
import random
from pygame.locals import *


class HongZha:
    '''轰炸机类'''

    def __init__(self, screen_temp):
        self.x = -30
        self.y = -150
        self.screen = screen_temp
        self.image = pygame.image.load("images/hongzhaji.png")
        self.direction = "down"

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, move_hz):
        # self.y = move_hz
        # self.y += 5
        if self.direction == "down":
            self.y += 3

        elif self.y < 0:
            self.direction = "down"
