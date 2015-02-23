from Graph import Graph

from DrawingController import DrawingController
from MenuScreen import Menu, advertConfiguration, influenceConfiguration, recommendationConfiguration, inputConfiguration, mainConfiguration
from EnvMenu import envConfiguration
from graphMenu import graphConfiguration
import cProfile
from Loader import Loader
from Clustering import Clustering
from Viral import Viral


class Main(object):

    def makeGraph(self):
        if self.InputMenuReturn.load == "1":
            self.graph = Loader().load(self.InputMenuReturn.file)
            if not self.InputMenuReturn.cull == "0":
                self.graph.trim(int(self.InputMenuReturn.cull))
        else:
            self.graph = Graph()
            self.graph.generatePeople(self.InputMenuReturn.people)
            self.graph.generateFriendships(self.InputMenuReturn.connections)


    def run(self):
        # cluster = Clustering(graph)
        # print("clustering " + str(cluster.findTriangles()))

        self.MainMenuReturn = mainConfiguration(False, True, True, True)
        self.AdMenuReturn = advertConfiguration('0.2', '0.2', '0.7', '7', '2')
        self.InfluenceMenuReturn = influenceConfiguration('10', '1')
        self.RecommendationMenuReturn = recommendationConfiguration(5)
        f = open("graph.gml")
        self.InputMenuReturn = inputConfiguration("1", f.read(), "100", "100", "100")
        self.GraphMenuReturn = graphConfiguration("None", "None", '1')
        self.EnvMenuReturn = envConfiguration("None", True, True)

        Menu(self)

        self.makeGraph()

        drawing = DrawingController(self.MainMenuReturn, self.AdMenuReturn, self.InfluenceMenuReturn, self.RecommendationMenuReturn, self.InputMenuReturn, self.GraphMenuReturn, self.EnvMenuReturn, self.graph)

        print("return")

if __name__ == '__main__':
    #cProfile.run('Main().run()')
    Main().run()