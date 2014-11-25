__author__ = 'Leo'
import pygame
from MenuScreen import MenuScreen
from pygame.locals import *
import sys


class DrawController:
    screenHeight = 0
    screenWidth = 0
    mousex = 0
    mousey = 0

    def __init__(self):
        pygame.init()
        video_info = pygame.display.Info()
        self.screenHeight = video_info.current_h
        self.screenWidth = video_info.current_w

    def menu_screen(self):
        menu = MenuScreen(self.screenHeight, self.screenWidth)

    def get_width(self, surface):
        return surface.get_width()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos