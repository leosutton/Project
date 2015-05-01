from Graph import Graph

from DrawingController import DrawingController
from MenuScreen import Menu, advertConfiguration, influenceConfiguration, recommendationConfiguration, inputConfiguration, mainConfiguration, socialConfiguration
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
        self.MainMenuReturn = mainConfiguration(False, True, True, True, True)
        self.AdMenuReturn = advertConfiguration('0.2', '0.2', '0.7', '7', '2')
        self.InfluenceMenuReturn = influenceConfiguration('10', '1')
        self.RecommendationMenuReturn = recommendationConfiguration(5)
        f = open("graph.gml")
        self.InputMenuReturn = inputConfiguration("1", f.read(), "1000", "100", "100")
        self.GraphMenuReturn = graphConfiguration("None", "None", '1')
        self.EnvMenuReturn = envConfiguration("None", True, True)
        self.SocialMenuReturn = socialConfiguration()

        print(f.read())

        Menu(self)

        self.makeGraph()

        cluster = Clustering(self.graph)
        print("clustering " + str(cluster.findTriangles()))

        DrawingController(self.MainMenuReturn, self.AdMenuReturn, self.InfluenceMenuReturn, self.RecommendationMenuReturn, self.InputMenuReturn, self.GraphMenuReturn, self.EnvMenuReturn, self.graph)

if __name__ == '__main__':
    #cProfile.run('Main().run()')
    Main().run()