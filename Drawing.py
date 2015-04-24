__author__ = 'Leo'
import sys

import pygame
from pygame.locals import *


class Drawing(object):
    screenHeight = 0
    screenWidth = 0
    mousex = 0
    mousey = 0

    def __init__(self, res):
        pygame.init()
        video_info = pygame.display.Info()
        self.screenHeight = video_info.current_h
        self.screenWidth = video_info.current_w
        self.surface = pygame.Surface(res)
        self.res = res
        self.events = []

    def get_width(self, surface):
        return surface.get_width()

    def process_events(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                self.mousex, self.mousey = event.pos

    def centre(self, window_width, surface_width):
        margin = window_width - surface_width
        return margin

    def getx(self, x):
        return int(x * self.res[0])

    def gety(self, y):
        return int(y * self.res[1])

    def getMousexPos(self):
        return self.mousex

    def getMouseyPos(self):
        return self.mousey