import math
import sys

import pygame
from pygame.constants import QUIT, MOUSEMOTION

from MainController import loop, surface, WINDOWWIDTH, WINDOWHEIGHT, people, gaussian, SIGMA, get_pos, rectangle, \
    can_see


__author__ = 'Leo'


class Controller(object):
    def __init__(self):
        pass

    def control(self):
        while loop:
            surface.fill((255, 255, 255))

            global mousex
            global mousey

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEMOTION:
                    mousex, mousey = event.pos
                    mousex = float(mousex) / float(WINDOWWIDTH)
                    mousey = float(mousey) / float(WINDOWHEIGHT)

                    # for point in people:
                    # point.direction = point.direction + ((random.random() -0.5)*10)
                    # point.x = math.sin(math.radians(point.direction))+point.x
                    # point.y = math.cos(math.radians(point.direction))+point.y

            current_positions = {}

            for point in people:
                x_distance = mousex - point.x
                y_distance = mousey - point.y
                distance = math.sqrt(x_distance ** 2 + y_distance ** 2)
                x_multiplier = gaussian(0, SIGMA, distance) + 1
                y_multiplier = gaussian(0, SIGMA, distance) + 1
                xposition = point.x - x_multiplier * x_distance / 5
                yposition = point.y - y_multiplier * y_distance / 5
                current_positions[point] = (xposition, yposition, point.direction)

            for point in current_positions.keys():
                position = current_positions[point]
                pygame.draw.circle(surface, (255, 0, 0), get_pos(position[0], position[1]), 10, 0)
                indicator = pygame.transform.rotate(rectangle, point.direction)
                surface.blit(indicator, get_pos(position[0], position[1]))
                visible = can_see(position[0], position[1], position[2])
                # for visiblepoint in visible:
                # pygame.draw.line(surface, (0,0,255), get_pos(position[0], position[1]), get_pos(current_positions[visiblepoint][0], current_positions[visiblepoint][1]))

            pygame.display.update()
            pygame.time.Clock().tick(1)