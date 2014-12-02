__author__ = 'Leo'

import math

import pygame
import numpy as np
import random
from Drawing import Drawing
from Graph import Graph


class GraphDrawrer(Drawing):
    def __init__(self, graph):
        Drawing.__init__(self)
        np.seterr(all='raise')
        self.graph = graph
        self.transitions = []

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
        lens = Lens(SIGMA)
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
        for person in self.graph.people:
            pygame.draw.circle(self.surface, (255, 0, 0), (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                               10, 0)
            box = pygame.Rect(int(self.getx(person.drawx))-5, int(self.gety(person.drawy))-5,10, 10)
            pygame.draw.arc(self.surface, (0,0,0), box, 0, person.views*2*math.pi)
        for connection in self.graph.connections:
            source = (int(self.getx(connection.between[0].drawx)), int(self.gety(connection.between[0].drawy)))
            destination = (int(self.getx(connection.between[1].drawx)), int(self.gety(connection.between[1].drawy)))
            pygame.draw.line(self.surface, (0, 255, 0), source, destination)
        for transition in self.transitions:
            direction = np.array([transition.person_to.draw_x - transition.person_from.draw_x, transition.person_to.draw_y - transition.person_to.draw_y])
            location = np.array([transition.person_from.draw_x, transition.person_from.draw_y]) + direction * transition.step
            pygame.draw.circle(self.surface, (0,0,0), (int(self.getx(location[0])), int(self.gety(location[1]))), 3, 0)
        pygame.display.update()
        self.process_events()
        #if random.random() < 0.1:
        #    self.transitions.append(Transition(random.choice(self.graph.people), random.choice(self.graph.people)))

    def drawLoop(self):
        while True:
            self.force_directed()

    def force_directed(self):
        k = 0.3 * math.sqrt(1.0 / len(self.graph.people))
        t = 0.01
        for i in range (0,10):
            for person in self.graph.people:
                person.displacement = [0, 0]
                for other in self.graph.people:
                    if not (person is other):
                        delta = np.array([person.draw_x - other.draw_x, person.draw_y - other.draw_y])
                        person.displacement += (delta / self.distance(delta)) * self.repulsion(k,
                                                                                               self.distance(
                                                                                                   delta))
            for connection in self.graph.connections:
                delta = np.array([connection.between[0].draw_x - connection.between[1].draw_x,
                                  connection.between[0].draw_y - connection.between[1].draw_y])
                connection.between[0].displacement -= (delta / self.distance(
                    delta)) * self.attraction(k, self.distance(delta))
                connection.between[1].displacement += (delta / self.distance(
                    delta)) * self.attraction(k, self.distance(delta))
            for person in self.graph.people:
                [person.draw_x, person.draw_y] = [person.draw_x, person.draw_y] + (person.displacement / self.distance(
                    person.displacement)) * min(self.distance(person.displacement), t)
                person.draw_x = min(0.95, max(0.05, person.draw_x))
                person.draw_y = min(0.95, max(0.05, person.draw_y))

    def attraction(self, k, x):
        return (x ** 2) / k

    def repulsion(self, k, x):
        if (x == 0):
            return 0.001
        else:
            return (k ** 2) / x

    def distance(self, delta):
        dis = math.sqrt(delta[0] ** 2 + delta[1] ** 2)
        if not dis == 0:
            return math.sqrt(delta[0] ** 2 + delta[1] ** 2)
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