__author__ = 'Leo'
import sys

import pygame
from pygame.locals import *


class Drawing(object):
    screenHeight = 0
    screenWidth = 0
    mousex = 0
    mousey = 0

    def __init__(self):
        video_info = pygame.display.Info()
        self.screenHeight = video_info.current_h
        self.screenWidth = video_info.current_w
        self.surface = pygame.Surface((1920, 1080))

    def get_width(self, surface):
        return surface.get_width()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                self.mousex, self.mousey = event.pos

    def centre(self, window_width, surface_width):
        margin = window_width - surface_width
        return margin

    def getx(self, x):
        return int(round(x * self.screenWidth))

    def gety(self, y):
        return int(round(y * self.screenHeight))

    def getMousexPos(self):
        return self.mousex

    def getMouseyPos(self):
        return self.mousey