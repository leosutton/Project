__author__ = 'Leo'
import pygame
from Drawing import DrawController


class MenuScreen(DrawController):
    def __init__(self, width, height):

        while True:
            pygame.init()
            self.surface = pygame.display.set_mode((width, height))
            pygame.display.set_caption('Menu')
            self.surface.fill((255, 255, 255))
            pygame.display.update()
            self.draw_menu()

    def draw_menu(self):
        while True:
            self.font = pygame.font.Font(None, 50)
            self.text = self.font.render("Interaction visulisation", 1, (0, 0, 0))
            self.surface.blit(self.text, (0, 0))
            menu items