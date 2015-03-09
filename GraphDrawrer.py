__author__ = 'Leo'

import math

import pygame
import numpy as np
from pygame.locals import *
from Drawing import Drawing


class GraphDrawrer(Drawing):
    def __init__(self, people, main, influence, ad, recommendation, graph, env, res, current = 0):
        Drawing.__init__(self, res)
        self.graph = people
        self.mainConfig = main
        self.influenceConfig = influence
        self.adConfig = ad
        self.recommendationConfig = recommendation
        self.graphConfig = graph
        self.envConfig = env
        self.transitions = []
        self.go = True
        self.current = current

    def drawConnections(self):
        for connection in self.graph.connections:
            if not (connection.between[0] in self.graph.people):
                self.graph.connections.remove(connection)
                continue
            if not (connection.between[1] in self.graph.people):
                self.graph.connections.remove(connection)
                continue
            source = (int(self.getx(connection.between[0].drawx)), int(self.gety(connection.between[0].drawy)))
            destination = (int(self.getx(connection.between[1].drawx)), int(self.gety(connection.between[1].drawy)))
            pygame.draw.line(self.surface, (0, 0, 0), source, destination, int(self.graphConfig.weight))
        for transition in self.transitions:
            direction = np.array([transition.person_to.draw_x - transition.person_from.draw_x,
                                  transition.person_to.draw_y - transition.person_to.draw_y])
            location = np.array(
                [transition.person_from.draw_x, transition.person_from.draw_y]) + direction * transition.step
            pygame.draw.circle(self.surface, (0, 0, 0), (int(self.getx(location[0])), int(self.gety(location[1]))), 3,
                               0)

    def drawPeople(self, current):
        for person in self.graph.people:
            if self.mainConfig.advert:
                if not hasattr(person, "status") or person.status[current] == "0":
                    pygame.draw.circle(self.surface, (255, 0, 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                elif person.status[current] == "n":
                    pygame.draw.circle(self.surface, (0, 0, 255),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                elif person.status[current] == "e":
                    pygame.draw.circle(self.surface, (0, 255, 255),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                elif person.status[current] == "1":
                    pygame.draw.circle(self.surface, (0, 255, 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                else:
                    print("person not drawn")
            if self.mainConfig.influence:
                if person.adopted:
                    pygame.draw.circle(self.surface, (255, 0, 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                else:
                    pygame.draw.circle(self.surface, (0, 255, 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
            if self.mainConfig.recommendation:
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
                    pygame.draw.circle(self.surface, (255 * opinion, 0, 255),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                elif item == "item1":
                    pygame.draw.circle(self.surface, (0, min(10 * 255 * person.item1, 255), 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                elif item == "item2":
                    pygame.draw.circle(self.surface, (0, min(10 * 255 * person.item2, 255), 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                elif item == "item3":
                    pygame.draw.circle(self.surface, (0, min(10 * 255 * person.item3, 255), 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                elif item == "max":
                    maximum = max([person.item1, person.item2, person.item3])
                    index = [person.item1, person.item2, person.item3].index(maximum)
                    if index == 0:
                        colour = (255, 0, 0)
                    elif index == 1:
                        colour = (0, 255, 0)
                    elif index == 2:
                        colour = (0, 0, 255)
                    pygame.draw.circle(self.surface, colour,
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       10, 0)
                    box = pygame.Rect(int(self.getx(person.drawx)) - 5, int(self.gety(person.drawy)) - 5, 10, 10)
                    pygame.draw.arc(self.surface, (0, 0, 0), box, 0, person.views * 2 * math.pi)

    def make_frame(self, layout = False, current = 0):
        self.surface.fill((255, 255, 255))
        mousex = float(self.getMousexPos()) / self.screenWidth
        mousey = float(self.getMouseyPos()) / self.screenHeight
        sigma = 0.1
        self.key = 1
        lens = Lens(sigma)
        keys = pygame.key.get_pressed()
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
        if keys[K_ESCAPE]:
            self.go = False

        self.drawConnections()
        self.drawPeople(current)

        if layout:
            font = pygame.font.Font(None, 36)
            text = font.render("Laying out", 1, (255, 0, 0, ))
            self.surface.blit(text, (0,0))
        self.process_events()
        return self.surface


class Layout(object):
    def __init__(self, graph):
        self.graph = graph

    def displace(self, person, t):
        person.draw_x = person.draw_x + (person.displacement[0] / self.distance(person.displacement)) * min(
            self.distance(person.displacement), t)
        person.draw_y = person.draw_y + (person.displacement[1] / self.distance(person.displacement)) * min(
            self.distance(person.displacement), t)
        person.draw_x = min(0.95, max(0.05, person.draw_x))
        person.draw_y = min(0.95, max(0.05, person.draw_y))

    def repel(self, k, person):
        person.displacement = [0, 0]
        for other in self.graph.people:
            if not (person is other):
                delta = [person.draw_x - other.draw_x, person.draw_y - other.draw_y]
                distance = self.distance(delta)
                difference = (1 / distance) * self.repulsion(k, distance)
                person.displacement[0] += delta[0] * difference
                person.displacement[1] += delta[1] * difference

    def attract(self, connection, k):
        delta = [connection.between[0].draw_x - connection.between[1].draw_x,
                 connection.between[0].draw_y - connection.between[1].draw_y]
        distance = self.distance(delta)
        difference = (1 / distance) * self.attraction(k, distance)
        connection.between[0].displacement[0] -= delta[0] * difference
        connection.between[0].displacement[1] -= delta[1] * difference
        connection.between[1].displacement[0] += delta[0] * difference
        connection.between[1].displacement[1] += delta[1] * difference

    def force_directed(self):
        k = 0.7 * math.sqrt(1.0 / len(self.graph.people))
        t = 0.05
        for x in range(0, 2):
            for person in self.graph.people:
                self.repel(k, person)
            for connection in self.graph.connections:
                self.attract(connection, k)
            for person in self.graph.people:
                self.displace(person, t)

    def attraction(self, k, x):
        return (x ** 2) / (k * 2)

    def repulsion(self, k, x):
        return (k ** 2) / x

    def distance(self, delta):
        return math.sqrt(delta[0] ** 2 + delta[1] ** 2) + 0.001


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