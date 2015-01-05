__author__ = 'Leo'
<<<<<<< HEAD
<<<<<<< HEAD
from tkinter

root = Tk()
=======
import Tkinter
from Tkinter import *

root = Tk()
>>>>>>> origin/master
=======
import pygame

from Drawing import Drawing


class MenuScreen(Drawing):
    menu_items = []

    def __init__(self):
        Drawing.__init__(self)
        while True:
            pygame.display.set_caption('Menu')
            self.surface.fill((255, 255, 255))
            text = self.menu()
            self.surface.blit(text, (0, 0))
            pygame.display.update()
            Drawing.process_events(self)

    def menu_item(self, y, text):
        font = pygame.font.Font(None, 10)
        text = font.render("Interaction visulisation", 1, (0, 0, 0))
        centre = Drawing.centre(self, Drawing.screenWidth, Drawing.screenHeight)
        return text
>>>>>>> parent of f983d40... Addint Tkinter
