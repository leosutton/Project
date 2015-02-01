from Graph import Graph
from GraphDrawrer import GraphDrawrer
from Environment import Environment
import pygame
from DrawingController import DrawingController
from MenuScreen import Menu
from EnvMenu import envConfiguration
from graphMenu import graphConfiguration
import cProfile
from Loader import Loader
from Clustering import Clustering


class Main(object):
    def run(self):
        loader = Loader()
        graph = loader.load()
        #graph.trim(50)
        cluster = Clustering(graph)
        print(cluster.findTriangles())

        self.GraphMenuReturn = graphConfiguration("None", "None", 0)
        self.EnvMenuReturn = envConfiguration("None", True, True)
        choices = Menu(self)

        print(self.GraphMenuReturn.weight)
        print(self.EnvMenuReturn.facing)

        drawing = DrawingController(self.GraphMenuReturn, self.EnvMenuReturn, graph)

if __name__ == '__main__':
    #cProfile.run('Main().run()')
    Main().run()