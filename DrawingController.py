__author__ = 'Leo'
from Graph import Graph
from Environment import Environment
from GraphDrawrer import GraphDrawrer
import pygame


class DrawingController(object):
    def __init__(self, left, right):
        graph = Graph()
        environment = Environment(graph)
        graphDrawrer = GraphDrawrer(graph)

        pygame.init()
        surface = pygame.display.set_mode((1600, 600))

        while True:
            surface.blit(environment.make_frame(), (0, 0))
            surface.blit(graphDrawrer.make_frame(), (800, 0))
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(60)