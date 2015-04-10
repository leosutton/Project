__author__ = 'leo'

import pygame
import math

pygame.init()
surface = pygame.display.set_mode((200,200))


if False:
    while True:
        surface.fill((255, 255, 255))

        pygame.draw.circle(surface, (255,0,0), (20,100), 10)
        pygame.draw.circle(surface, (100, 100, 0), (50, 100), 10)
        pygame.draw.circle(surface, (0,0,255), (50, 100), 15, 5)
        pygame.draw.arc(surface, (0, 100, 100), ((80, 90), (20, 20)), math.pi*0.5, math.pi*2, 10)
        pygame.draw.rect(surface, (0,255,0), ((110, 90), (20,20)), 1)
        pygame.draw.line(surface, (0,0,0), (110, 90), (130, 110))

        pygame.display.update()


if True:
    while True:
        surface.fill((255,255,255))

        pygame.draw.line(surface, (0,0,0), (20, 50), (20, 150))
        pygame.draw.line(surface, (0,0,0), (40, 50), (40, 150), 5)
        pygame.draw.line(surface, (0,0, 255), (60, 50), (60, 150))

        surface = pygame.transform.rotate(surface, 270)

        pygame.display.update()