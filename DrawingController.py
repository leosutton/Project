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

class DrawingController(object):
    def __init__(self, left, right, graph):
        pygame.init()
        if isinstance(left, graphConfiguration):
            self.left = GraphDrawrer(graph, left)
        else:
            self.left = Environment(graph, left)
            print (type(left))

        if isinstance(right, envConfiguration):
            self.right = Environment(graph, right)
        else:
            self.right = GraphDrawrer(graph, right)
            print (type(right))

        surface = pygame.display.set_mode((1600, 600))
        clock = pygame.time.Clock()

        counter = 0
        record = {}

        for n in range(0, 20):
            surface.blit(self.left.make_frame(), (0, 0))
            #surface.blit(self.right.make_frame(), (800, 0))
            pygame.display.update()
            clock.tick(60)

        viral = Viral(graph, 0.2, 0.2, 0.7, 7, 2)
        viral.seedEmail(graph, 5)
        viral.seedAdvert(graph, 0.1)
        record[counter] = viral.record(graph)
        for n in range(0, 100):
            counter += 1
            surface.blit(self.left.make_frame(), (0, 0))
            #surface.blit(self.right.make_frame(), (800, 0))
            pygame.display.update()
            clock.tick(60)
            if counter % 5 == 0:
                viral.checkEmail(graph)
                record[counter] = viral.record(graph)
                print (str(record))

        Plotter(record)
