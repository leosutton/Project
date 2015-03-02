__author__ = 'Leo'
from MenuScreen import influenceConfiguration, inputConfiguration
from graphMenu import graphConfiguration
from EnvMenu import envConfiguration
from GraphDrawrer import GraphDrawrer

class influence:
    def __init__(self, main):
        self.main = main
        self.main.InfluenceMenuReturn = influenceConfiguration('10', '1')
        f = open("graph.gml")
        self.main.InputMenuReturn = inputConfiguration("1", f.read(), "1000", "100", "100")
        self.main.GraphMenuReturn = graphConfiguration("None", "None", '1')
        self.main.EnvMenuReturn = envConfiguration("None", True, True)
        self.graphDrawrer = GraphDrawrer(self.main.graph, self.main.mainConfig, self.main.influenceConfig, self.main.adConfig, self.main.recommendationConfig, self.main.graphConfig, self.main.envConfig)

    def prepareSeperate(self):
        self.main.makeGraph()
        self.main.graph.people[300].adopted = True #James Milne
        self.main.graph.people[226].adopted = True # James Lorenz

    def prepareTogether(self):
        self.main.makeGraph()
        self.main.graph.people[300].adopted = True #James Milne
        self.main.graph.people[48].adopted = True #Josh Wood

