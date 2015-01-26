__author__ = 'Leo'
from Graph import Graph
from Environment import Environment
from GraphDrawrer import GraphDrawrer
import pygame
from EnvMenu import envConfiguration
from graphMenu import graphConfiguration
import EnvMenu
import graphMenu


class DrawingController(object):
    def __init__(self, left, right, graph):
        pygame.init()
        if isinstance(left, graphConfiguration):
            self.left = GraphDrawrer(graph, left)
            print ("left worked")
        else:
            self.left = Environment(graph, left)
            print (type(left))

        if isinstance(right, envConfiguration):
            self.right = Environment(graph, right)
            print ("right worked")
        else:
            self.right = GraphDrawrer(graph, right)
            print (type(right))

        surface = pygame.display.set_mode((1600, 600))

        while True:
            surface.blit(self.left.make_frame(), (0, 0))
            surface.blit(self.right.make_frame(), (800, 0))
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(60)