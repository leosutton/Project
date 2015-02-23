__author__ = 'Leo'
from Graph import Graph
from Environment import Environment
from GraphDrawrer import GraphDrawrer
import pygame
from EnvMenu import envConfiguration
from graphMenu import graphConfiguration
import EnvMenu
import graphMenu
from Viral import Viral
from Viral import Numbers
from Plotter import Plotter
from Influence import Influence1, Influence2
from Recommendation import Recommendation


class DrawingController(object):
    def __init__(self, left, right, graph, mode="recommendation"):
        self.mode = mode
        print(mode)
        pygame.init()
        if isinstance(left, graphConfiguration):
            self.left = GraphDrawrer(graph, left, self.mode)
        else:
            self.left = Environment(graph, left)
            print(type(left))

        if isinstance(right, envConfiguration):
            self.right = Environment(graph, right)
        else:
            self.right = GraphDrawrer(graph, right, self.mode)
            print(type(right))

        surface = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()

        counter = 0
        record = {}
        if self.mode == "influence1":
            print('start')
            influence = Influence1(graph)
            influence.initialiseGraph()
            influence.startingNodes(1)

        if self.mode == "influence2":
            influence = Influence2(graph)
            influence.initialiseGraph()
            influence.startingNodes(5)

        if self.mode == "recommendation":
            recommendation = Recommendation(graph)
            recommendation.intialise(200)
            for person in graph.people:
                person.item1 = recommendation.getRecommendation(person, "item1")
                print(str(person.item1))
            for person in graph.people:
                person.item2 = recommendation.getRecommendation(person, "item2")
                print(str(person.item2))
            for person in graph.people:
                person.item3 = recommendation.getRecommendation(person, "item3")
                print(str(person.item3))

        for n in range(0, 20):
            surface.blit(self.left.make_frame(), (0, 0))
            # surface.blit(self.right.make_frame(), (800, 0))
            pygame.display.update()
            clock.tick(60)

        if self.mode == 'viral':
            viral = Viral(graph, 0.2, 0.2, 0.7, 7, 2)
            viral.seedEmail(graph, 5)
            viral.seedAdvert(graph, 0.1)
            record[counter] = viral.record(graph)
        for n in range(0, 1000):
            counter += 1
            surface.blit(self.left.make_frame(), (0, 0))
            # surface.blit(self.right.make_frame(), (800, 0))
            pygame.display.update()
            clock.tick(60)
            if counter % 5 == 0:
                if self.mode == 'viral':
                    viral.checkEmail(graph)
                    record[counter] = viral.record(graph)
                if self.mode == 'influence1':
                    influence.process()
                if self.mode == 'influence2':
                    influence.process()

        if self.mode == 'viral':
            Plotter(record)