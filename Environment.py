__author__ = 'Leo'

import pygame
import math
import random
from pygame.locals import *
from GraphDrawrer import GraphDrawrer

from Drawing import Drawing


class Environment(Drawing):
    def __init__(self, graph):
        Drawing.__init__(self)
        self.graph = graph

    def make_frame(self):
        self.draw(self.graph)
        self.move(self.graph)
        return self.surface


    def draw(self, graph):
        self.surface.fill((255,255,255))
        for person in self.graph.people:
            pygame.draw.circle(self.surface, (255, 0, 0),
                               (int(self.getx(person.env_x)), int(self.gety(person.env_y))), 10, 0)
            diameter = 100
            show = self.keycheck()
            if show == True:
                box = pygame.Rect(self.getx(person.env_x) - diameter/2.0, self.gety(person.env_y) - diameter/2.0, diameter, diameter)
                halfbox = pygame.Rect(self.getx(person.env_x) - diameter/4.0, self.gety(person.env_y) - diameter/4.0, diameter/2.0, diameter/2.0)
                pygame.draw.arc(self.surface, (0,255,0), halfbox, person.direction - math.pi/4, person.direction + math.pi/4, diameter/4)
                pygame.draw.arc(self.surface, (0,0,0), box, person.direction - math.pi/4, person.direction + math.pi/4)
        pygame.display.update()
        self.process_events()

    def draw_angle(self, x):
        return (math.pi * 2) - x

    def move(self, graph):
        for person in self.graph.people:
            x = math.cos(person.direction)
            y = -math.sin(person.direction)
            amount = random.random()/100
            person.env_x = min(0.95, max(0.05, person.env_x + x*amount))
            person.env_y = min(0.95, max(0.05, person.env_y + y*amount))
            if hasattr(person, 'turn'):
                if person.turn == 'l':
                    if random.random() < 0.005:
                        person.turn = 'r'
                    person.direction = person.direction + random.random()/100
                if person.turn == 'r':
                    if random.random() < 0.005:
                        person.turn = 'l'
                    person.direction = person.direction - random.random()/30
            elif random.random() > 0.5:
                person.turn = 'l'
            else:
                person.turn = 'r'
            if self.see(50, person):
                pygame.draw.circle(self.surface, (0,0,255), (int(self.getx(person.env_x)), int(self.gety(person.env_y))), 10, 0)
            pygame.display.update()

    def keycheck(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] == True:
            return True
        else:
            return False

    def see(self, d, person):
        for other in self.graph.people:
            if not(other is person):
                distance = math.sqrt((person.env_x - other.env_x)**2 + (person.env_y - other.env_y)**2)
                if distance < d and not(person.env_y - other.env_y) == 0:
                    angle = math.atan((person.env_x - other.env_x)/(person.env_y - other.env_y))
                    if person.direction-math.pi/4 < angle < person.direction+math.pi/4:
                        return True
            return False