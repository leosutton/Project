__author__ = 'Leo'

import math

import pygame
import numpy as np
from pygame.locals import *
from Drawing import Drawing


class GraphDrawrer(Drawing):
    def __init__(self, people, main, influence, ad, recommendation, graph, env, res = (1920,1080), current = 0):
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
        self.key = 1

    def drawLabel(self, person, x, y):
        font = pygame.font.Font(None, 20)
        text1 = font.render("Name: " + str(person.name), 1, (0,0,0))
        text2 = font.render("Sex: " + str(person.sex), 1, (0,0,0))
        topsize = text1.get_size()
        label = pygame.Surface((topsize[0], topsize[1]*2))
        label.fill((200, 200, 200))
        #label.set_colorkey((250, 250, 250))
        label.blit(text1, (0,0))
        label.blit(text2, (0, topsize[1]))
        self.surface.blit(label, (x,y))

    def drawConnections(self):
        for connection in self.graph.connections:
            if not connection.between[0] in self.graph.people:
                self.graph.connections.remove(connection)
                break
            if not connection.between[1] in self.graph.people:
                self.graph.connections.remove(connection)
                break
            source = (int(self.getx(connection.between[0].drawx)), int(self.gety(connection.between[0].drawy)))
            destination = (int(self.getx(connection.between[1].drawx)), int(self.gety(connection.between[1].drawy)))
            if self.mainConfig.social:
                pygame.draw.line(self.surface, (0, 0, 0), source, destination, 1)
            else:
                pygame.draw.line(self.surface, (0, 0, 0), source, destination, int(self.graphConfig.weight))
        thumb = pygame.image.load("ThumbsUp.png")
        thumb = pygame.transform.scale(thumb, (20,20))
        for transition in self.transitions:
            direction = np.array([transition.person_to.x - transition.person_from.x,
                                  transition.person_to.y - transition.person_from.y])
            location = np.array(
                [transition.person_from.x, transition.person_from.y]) + direction * transition.step/60
#            pygame.draw.circle(self.surface, (0, 0, 255), (int(self.getx(location[0])), int(self.gety(location[1]))), 3)
            self.surface.blit(thumb, (int(self.getx(location[0]) - 10), int(self.gety(location[1]) - 10)))
            transition.step += 1
            if transition.step > 59:
                self.transitions.pop(self.transitions.index(transition))


    def drawPeople(self, current):
        for person in self.graph.people:
            if self.mainConfig.advert:
                if not hasattr(person, "status") or person.status[current] == "0":
                    self.people.append(pygame.draw.circle(self.surface, (255, 0, 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       3, 0))
                elif person.status[current] == "n":
                    self.people.append(pygame.draw.circle(self.surface, (0, 0, 255),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       3, 0))
                elif person.status[current] == "e":
                    self.people.append(pygame.draw.circle(self.surface, (0, 255, 255),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       3, 0))
                elif person.status[current] == "1":
                    self.people.append(pygame.draw.circle(self.surface, (0, 255, 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       3, 0))
                # else:
                #     print("person not drawn")
            if self.mainConfig.influence:
                if person.adopted:
                    pygame.draw.circle(self.surface, (255, 0, 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       6, 3)
                else:
                    pygame.draw.circle(self.surface, (0, 255, 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       6, 3)
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
                                       9, 3)
                elif item == "item1":
                    pygame.draw.circle(self.surface, (0, min(10 * 255 * person.item1, 255), 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       9, 3)
                elif item == "item2":
                    pygame.draw.circle(self.surface, (0, min(10 * 255 * person.item2, 255), 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       9, 3)
                elif item == "item3":
                    pygame.draw.circle(self.surface, (0, min(10 * 255 * person.item3, 255), 0),
                                       (int(self.getx(person.drawx)), int(self.gety(person.drawy))),
                                       9, 3)
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
                                       9, 3)
                    box = pygame.Rect(int(self.getx(person.drawx)) - 5, int(self.gety(person.drawy)) - 5, 10, 10)
                    pygame.draw.arc(self.surface, (0, 0, 0), box, 0, person.views * 2 * math.pi)
            if not self.mainConfig.advert and not self.mainConfig.influence and not self.mainConfig.recommendation and not self.mainConfig.social:
                if person.selected:
                    self.people.append(pygame.draw.circle(self.surface, (255, 0, 0), (int(self.getx(person.drawx)), int(self.gety(person.drawy))), 10, 0))
                else:
                    self.people.append(pygame.draw.circle(self.surface, (0, 255, 0), (int(self.getx(person.drawx)), int(self.gety(person.drawy))), 10, 0))

            if self.graphConfig.circle == "Views":
                pygame.draw.arc(self.surface, (0,0,0), (self.getx(person.drawx)-5, self.gety(person.drawy)-5, 10, 10), 0, 2*math.pi*person.views)


    def make_frame(self, layout = False, current = 0):
        self.people = []
        self.surface.fill((255, 255, 255))
        mousex = float(self.getMousexPos()) / self.screenWidth
        mousey = float(self.getMouseyPos()) / self.screenHeight
        sigma = 0.1
        lens = Lens(sigma)
        keys = pygame.key.get_pressed()
        if keys[K_z]:
            for person in self.graph.people:
                xdistance = mousex - person.x
                ydistance = mousey - person.y
                distance = math.sqrt(xdistance ** 2 + ydistance ** 2)
                x_multiplier = lens.gaussian(distance) + 1
                y_multiplier = lens.gaussian(distance) + 1
                xposition = person.x - x_multiplier * xdistance / 5
                yposition = person.y - y_multiplier * ydistance / 5
                person.drawx = xposition
                person.drawy = yposition
        else:
            for person in self.graph.people:
                person.drawx = person.x
                person.drawy = person.y
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

        if keys[K_l]:
            for person in self.people:
                if person.collidepoint((self.mousex, self.mousey)):
                    index = self.people.index(person)
                    self.drawLabel(self.graph.people[index], self.mousex, self.mousey)
                    break

        self.process_events()

        for event in self.events:
            if event.type == pygame.MOUSEBUTTONUP:
                for person in self.people:
                    if person.collidepoint((self.mousex, self.mousey)):
                        print("Collided with " + str(person))
                        if self.graph.people[self.people.index(person)].selected:
                            self.graph.people[self.people.index(person)].selected = False
                            print("person deselected")
                        else:
                            self.graph.people[self.people.index(person)].selected = True
                            print("person selected")
                        break

        if layout:
            font = pygame.font.Font(None, 36)
            text = font.render("Laying out", 1, (255, 0, 0, ))
            self.surface.blit(text, (0,0))
        return self.surface


class Layout(object):
    def __init__(self, graph):
        self.graph = graph

    def displace(self, person, t):
        person.x = person.x + (person.displacement[0] / self.distance(person.displacement)) * min(
            self.distance(person.displacement), t)
        person.y = person.y + (person.displacement[1] / self.distance(person.displacement)) * min(
            self.distance(person.displacement), t)
        person.x = min(0.95, max(0.05, person.x))
        person.y = min(0.95, max(0.05, person.y))

    def repel(self, k, person):
        person.displacement = [0, 0]
        for other in self.graph.people:
            if not (person is other):
                delta = [person.x - other.x, person.y - other.y]
                distance = self.distance(delta)
                difference = (1 / distance) * self.repulsion(k, distance)
                person.displacement[0] += delta[0] * difference
                person.displacement[1] += delta[1] * difference

    def attract(self, connection, k):
        delta = [connection.between[0].x - connection.between[1].x,
                 connection.between[0].y - connection.between[1].y]
        distance = self.distance(delta)
        difference = (1 / distance) * self.attraction(k, distance)
        connection.between[0].displacement[0] -= delta[0] * difference
        connection.between[0].displacement[1] -= delta[1] * difference
        connection.between[1].displacement[0] += delta[0] * difference
        connection.between[1].displacement[1] += delta[1] * difference

    def force_directed(self):
        k = 1 * math.sqrt(1.0 / len(self.graph.people))
        t = 0.05
        for x in range(0, 2):
            for person in self.graph.people:
                self.repel(k, person)
            for connection in self.graph.connections:
                self.attract(connection, k)
            for person in self.graph.people:
                self.displace(person, t)

    def attraction(self, k, x):
        return (x ** 2) / (k * 1)

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