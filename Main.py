from Graph import Graph

from DrawingController import DrawingController
from MenuScreen import Menu
from EnvMenu import envConfiguration
from graphMenu import graphConfiguration
import cProfile
from Loader import Loader
from Clustering import Clustering
from Viral import Viral


class Main(object):
    def run(self):
        loader = Loader()
        graph = loader.load()
        graph.trim(100)
        cluster = Clustering(graph)
        print("clustering " + str(cluster.findTriangles()))

        self.GraphMenuReturn = graphConfiguration("None", "None", 0)
        self.EnvMenuReturn = envConfiguration("None", True, True)
        choices = Menu(self)

        drawing = DrawingController(self.GraphMenuReturn, self.EnvMenuReturn, graph)

        print("return")

if __name__ == '__main__':
    cProfile.run('Main().run()')
    #Main().run()