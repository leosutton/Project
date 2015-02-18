__author__ = 'Leo'

import math

import pygame
import numpy as np
import random
from Drawing import Drawing
from Graph import Graph
import threading
from pygame.locals import *
from Recommendation import Recommendation


class GraphDrawrer(Drawing):
    def __init__(self, graph, config, mode='recommendation'):
        Drawing.__init__(self)
        np.seterr(all='raise')
        self.graph = graph
        self.transitions = []
        self.config = config
        self.mode = mode

    def make_frame(self):
        self.force_directed()
        self.draw_graph()
        return self.surface


    def draw_graph(self):
        self.surface.fill((255, 255, 255))
        points = self.graph.people
        mousex = float(self.getMousexPos()) / self.screenWidth
        mousey = float(self.getMouseyPos()) / self.screenHeight
        SIGMA = 0.1
        self.key = 1
        lens = Lens(SIGMA)
        keys=pygame.key.get_pressed()
        if keys[K_z]:
            for person in self.graph.people:
                xdistance = mousex - person.draw_x
                ydistance = mousey - person.draw_y
                distance = math.sqrt(xdistance ** 2 + ydistance ** 2)
                x_multiplier = lens.gaussian(distance) + 1
                y_multiplier = lens.gaussian(distance) + 1
                xposition = person.draw_x - x_multiplier * xdistance / 5
                yposition = person.draw_y - y_multiplier * ydistance / 5
                person.drawx = xposition
                person.drawy = yposition
        else:
            for person in self.graph.people:
                person.drawx = person.draw_x
                person.drawy = person.draw_y
        if keys[K_1]:
            self.key = 1
        if keys[K_2]:
            self.key = 2
        if keys[K_3]:
            self.key = 3
        if keys[K_4]:
            self.key = 4
        if self.config == 0:
            self.width = 1
        else:
            self.width = int(self.config.weight)

        for connection in self.graph.connections:
            if not (connection.between[0] in self.graph.people):
                self.graph.connections.remove(connection)
                continue
            if not (connection.between[1] in self.graph.people):
                self.graph.connections.remove(connection)
                continue
            source = (int(self.getx(connection.between[0].drawx)), int(self.gety(connection.between[0].drawy)))
            destination = (int(self.getx(connection.between[1].drawx)), int(self.gety(connection.between[1].drawy)))
            pygame.draw.line(self.surface, (0, 0, 0), source, destination, self.width)
        for transition in self.transitions:
            direction = np.array([transition.person_to.draw_x - transition.person_from.draw_x,
                                  transition.person_to.draw_y - transition.person_to.draw_y])
            location = np.array(
                [transition.person_from.draw_x, transition.person_from.draw_y]) + direction * transition.step
            pygame.draw.circle(self.surface, (0, 0, 0), (int(self.getx(location[0])), int(self.gety(location[1]))), 3,
                               0)
        for person in self.graph.people:
            if self.mode == "viral":
                if not hasattr(person, "participated") or person.participated == "0":
                    pygame.draw.circle(self.surface, (255, 0, 0), (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                    box = pygame.Rect(int(self.getx(person.drawx)) - 5, int(self.gety(person.drawy)) - 5, 10, 10)
                    pygame.draw.arc(self.surface, (0, 0, 0), box, 0, person.views * 2 * math.pi)
                elif person.participated == "n":
                    pygame.draw.circle(self.surface, (0, 0, 255), (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                    box = pygame.Rect(int(self.getx(person.drawx)) - 5, int(self.gety(person.drawy)) - 5, 10, 10)
                    pygame.draw.arc(self.surface, (0, 0, 0), box, 0, person.views * 2 * math.pi)
                elif person.participated == "e":
                    pygame.draw.circle(self.surface, (0, 255, 255), (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                    box = pygame.Rect(int(self.getx(person.drawx)) - 5, int(self.gety(person.drawy)) - 5, 10, 10)
                    pygame.draw.arc(self.surface, (0, 0, 0), box, 0, person.views * 2 * math.pi)
                elif person.participated == "1":
                    pygame.draw.circle(self.surface, (0, 255, 0), (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                    box = pygame.Rect(int(self.getx(person.drawx)) - 5, int(self.gety(person.drawy)) - 5, 10, 10)
                    pygame.draw.arc(self.surface, (0, 0, 0), box, 0, person.views * 2 * math.pi)
            if self.mode == "influence1" or self.mode == "influence2":
                if person.adopted:
                    pygame.draw.circle(self.surface, (255, 0, 0), (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                    box = pygame.Rect(int(self.getx(person.drawx)) - 5, int(self.gety(person.drawy)) - 5, 10, 10)
                    pygame.draw.arc(self.surface, (0, 0, 0), box, 0, person.views * 2 * math.pi)
                else:
                    pygame.draw.circle(self.surface, (0, 255, 0), (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                    box = pygame.Rect(int(self.getx(person.drawx)) - 5, int(self.gety(person.drawy)) - 5, 10, 10)
                    pygame.draw.arc(self.surface, (0, 0, 0), box, 0, person.views * 2 * math.pi)
            if self.mode == "recommendation":
                item = ""
                opinion = 0
                knows = False
                if self.key == 1:
                    item = "item1"
                elif self.key == 2:
                    item = "item2"
                elif self.key == 3:
                    item = "item3"
                elif self.key == 4:
                    item = "max"
                for rating in person.ratings:
                    if rating.item == item:
                        knows = True
                        opinion = rating.rating
                if knows:
                    pygame.draw.circle(self.surface, (255*opinion, 0,255), (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                    box = pygame.Rect(int(self.getx(person.drawx)) - 5, int(self.gety(person.drawy)) - 5, 10, 10)
                    pygame.draw.arc(self.surface, (0, 0, 0), box, 0, person.views * 2 * math.pi)
                elif item == "item1":
                    pygame.draw.circle(self.surface, (0, min(10*255*person.item1, 255), 0), (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                    box = pygame.Rect(int(self.getx(person.drawx)) - 5, int(self.gety(person.drawy)) - 5, 10, 10)
                    pygame.draw.arc(self.surface, (0, 0, 0), box, 0, person.views * 2 * math.pi)
                elif item == "item2":
                    pygame.draw.circle(self.surface, (0, min(10*255*person.item2, 255), 0), (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                    box = pygame.Rect(int(self.getx(person.drawx)) - 5, int(self.gety(person.drawy)) - 5, 10, 10)
                    pygame.draw.arc(self.surface, (0, 0, 0), box, 0, person.views * 2 * math.pi)
                elif item == "item3":
                    pygame.draw.circle(self.surface, (0, min(10*255*person.item3, 255), 0), (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                    box = pygame.Rect(int(self.getx(person.drawx)) - 5, int(self.gety(person.drawy)) - 5, 10, 10)
                    pygame.draw.arc(self.surface, (0, 0, 0), box, 0, person.views * 2 * math.pi)
                elif item == "max":
                    maximum = max([person.item1, person.item2, person.item3])
                    index = [person.item1, person.item2, person.item3].index(maximum)
                    if index == 0:
                        colour = (255, 0, 0)
                    elif index == 1:
                        colour = (0, 255, 0)
                    elif index == 2:
                        colour = (0, 0, 255)
                    pygame.draw.circle(self.surface, colour, (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                    box = pygame.Rect(int(self.getx(person.drawx)) - 5, int(self.gety(person.drawy)) - 5, 10, 10)
                    pygame.draw.arc(self.surface, (0, 0, 0), box, 0, person.views * 2 * math.pi)
        pygame.display.update()
        self.process_events()

    def displace(self, person, t):
        [person.draw_x, person.draw_y] = [person.draw_x, person.draw_y] + (person.displacement / self.distance(
            person.displacement)) * min(self.distance(person.displacement), t)
        person.draw_x = min(0.95, max(0.05, person.draw_x))
        person.draw_y = min(0.95, max(0.05, person.draw_y))

    def repel(self, k, person):
        person.displacement = [0, 0]
        for other in self.graph.people:
            if not (person is other):
                delta = np.array([person.draw_x - other.draw_x, person.draw_y - other.draw_y])
                person.displacement += (delta / self.distance(delta)) * self.repulsion(k,
                                                                                       self.distance(
                                                                                           delta))
    def attract(self, connection, k):
        if not (connection.between[0] in self.graph.people):
            self.graph.connections.remove(connection)
            return
        if not (connection.between[1] in self.graph.people):
            self.graph.connections.remove(connection)
            return
        delta = np.array([connection.between[0].draw_x - connection.between[1].draw_x,
                          connection.between[0].draw_y - connection.between[1].draw_y])
        connection.between[0].displacement -= (delta / self.distance(
            delta)) * self.attraction(k, self.distance(delta)) * connection.strength
        connection.between[1].displacement += (delta / self.distance(
            delta)) * self.attraction(k, self.distance(delta)) * connection.strength

    def force_directed(self):
        k = 0.5 * math.sqrt(1.0 / len(self.graph.people))
        t = 0.01
        for x in range (0,2):
            def repel(k, person):
                self.repel(k, person)
            def attract(connection, k):
                self.attract(connection, k)
            for person in self.graph.people:
                self.repel(k, person)
            for connection in self.graph.connections:
                self.attract(connection, k)
            for person in self.graph.people:
                self.displace(person, t)

    def attraction(self, k, x):
        return (x ** 2) / (2*k)

    def repulsion(self, k, x):
        if (x == 0):
            return 0.001
        else:
            return (k ** 2) / x

    def distance(self, delta):
        dis = math.sqrt(delta[0] ** 2 + delta[1] ** 2)
        if not dis == 0:
            return dis
        else:
            return 0.0001


class Lens:
    def __init__(self, sigma):
        self.sigma = sigma

    def gaussian(self, distance):
        coefficient = 1.0 / (float(self.sigma) * math.sqrt(2 * math.pi))
        exponential = math.exp(-((float(distance) - float(self.sigma)) ** 2) / (2 * (float(self.sigma) ** 2)))
        return coefficient * exponential


class Transition:
    def __init__(self, person_from, person_to):
        self.person_from = person_from
        self.person_to = person_to
        self.step = 0