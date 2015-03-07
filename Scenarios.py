__author__ = 'Leo'
from MenuScreen import influenceConfiguration, inputConfiguration, mainConfiguration, advertConfiguration, recommendationConfiguration
from graphMenu import graphConfiguration
from EnvMenu import envConfiguration
from GraphDrawrer import GraphDrawrer
from Main import Main
from Influence import Influence1, Influence2
from copy import deepcopy
from Recommendation import Recommendation, Rating
import pygame
from Viral import Viral
from Plotter import Plotter


class influenceScen(object):
    def __init__(self, main=Main()):
        self.main = main
        self.main.MainMenuReturn = mainConfiguration(False, False, True, False)
        self.main.InfluenceMenuReturn = influenceConfiguration('10', '2')
        f = open("graph.gml")
        self.main.InputMenuReturn = inputConfiguration("1", f.read(), "1000", "100", "100")
        self.main.AdMenuReturn = advertConfiguration('0.2', '0.2', '0.7', '7', '2')
        self.main.GraphMenuReturn = graphConfiguration("None", "None", '1')
        self.main.EnvMenuReturn = envConfiguration("None", True, True)
        self.main.RecommendationMenuReturn = recommendationConfiguration(5)
        self.main.makeGraph()
        Influence2(self.main.graph, 0.5).initialiseGraph()
        pygame.init()
        surface = pygame.display.set_mode((1920, 1080))
        clock = pygame.time.Clock()
        self.graphDrawrer = GraphDrawrer(self.main.graph, self.main.MainMenuReturn, self.main.InfluenceMenuReturn, self.main.AdMenuReturn, self.main.RecommendationMenuReturn, self.main.GraphMenuReturn, self.main.EnvMenuReturn, (960,1080))
        for n in range(0, 20):
            surface.blit(self.graphDrawrer.make_frame(), (0, 0))
            self.graphDrawrer.force_directed()
            pygame.display.update()
            clock.tick(60)

        self.main.graph1 = deepcopy(self.main.graph)
        self.graphDrawrer1 = GraphDrawrer(self.main.graph1, self.main.MainMenuReturn, self.main.InfluenceMenuReturn, self.main.AdMenuReturn, self.main.RecommendationMenuReturn, self.main.GraphMenuReturn, self.main.EnvMenuReturn, (960,1080))
        self.prepareSeperate(self.main.graph)
        self.prepareTogether(self.main.graph1)

        for n in range(0,100):
            surface.blit(self.graphDrawrer.make_frame(), (0,0))
            surface.blit(self.graphDrawrer1.make_frame(), (960, 0))
            Influence2(self.main.graph, 5).process()
            Influence2(self.main.graph1, 5).process()
            pygame.display.update()
            clock.tick(1)


    def prepareSeperate(self, graph):
        graph.people[301].adopted = True #James Milne
        graph.people[227].adopted = True #James Lorenz

    def prepareTogether(self, graph):
        graph.people[301].adopted = True #James Milne
        graph.people[49].adopted = True #Josh Wood

class AdvertScen(object):
    def __init__(self, main):
        self.main = main
        self.main.MainMenuReturn = mainConfiguration(False, True, False, False)
        self.main.InfluenceMenuReturn = influenceConfiguration('10', '2')
        f = open("graph.gml")
        self.main.InputMenuReturn = inputConfiguration("1", f.read(), "1000", "100", "100")
        self.main.AdMenuReturn = advertConfiguration('0.2', '0.2', '0.7', '7', '2')
        self.main.GraphMenuReturn = graphConfiguration("None", "None", '1')
        self.main.EnvMenuReturn = envConfiguration("None", True, True)
        self.main.RecommendationMenuReturn = recommendationConfiguration(5)
        self.main.makeGraph()
        pygame.init()
        surface = pygame.display.set_mode((1920, 1080))
        clock = pygame.time.Clock()
        self.graphDrawrer = GraphDrawrer(self.main.graph, self.main.MainMenuReturn, self.main.InfluenceMenuReturn, self.main.AdMenuReturn, self.main.RecommendationMenuReturn, self.main.GraphMenuReturn, self.main.EnvMenuReturn, (1920,1080))
        viral = Viral(self.main.graph, float(self.main.AdMenuReturn.seed), float(self.main.AdMenuReturn.email), float(self.main.AdMenuReturn.ad), float(self.main.AdMenuReturn.mu), float(self.main.AdMenuReturn.sigma))
        viral.seedEmail(self.main.graph, 5)
        viral.seedAdvert(self.main.graph, 0.1)
        record = {}
        counter = 0
        record[counter] = viral.record(self.main.graph)
        for n in range(0,20):
            surface.blit(self.graphDrawrer.make_frame(), (0, 0))
            pygame.display.update()
            clock.tick(60)
        while True:
            counter += 1
            viral.checkEmail(self.main.graph)
            record[counter] = viral.record(self.main.graph)

        Plotter(record)

class RecommendationScen(object):
    def __init__(self, main=Main()):
        self.main = main
        self.main.MainMenuReturn = mainConfiguration(False, False, False, True)
        self.main.InfluenceMenuReturn = influenceConfiguration('10', '1')
        f = open("graph.gml")
        self.main.InputMenuReturn = inputConfiguration("1", f.read(), "1000", "100", "100")
        self.main.AdMenuReturn = advertConfiguration('0.2', '0.2', '0.7', '7', '2')
        self.main.GraphMenuReturn = graphConfiguration("None", "None", '1')
        self.main.EnvMenuReturn = envConfiguration("None", True, True)
        self.main.RecommendationMenuReturn = recommendationConfiguration(5)
        self.main.makeGraph()
        for person in self.main.graph.people:
            person.ratings = []
        self.preparePeople(self.main.graph)
        for person in self.main.graph.people:
            person.item1 = Recommendation(self.main.graph).getRecommendation(person, 'item1')
        for person in self.main.graph.people:
            person.item2 = Recommendation(self.main.graph).getRecommendation(person, 'item2')
        for person in self.main.graph.people:
            person.item3 = Recommendation(self.main.graph).getRecommendation(person, 'item3')
        pygame.init()
        surface = pygame.display.set_mode((1920, 1080))
        clock = pygame.time.Clock()
        self.graphDrawrer = GraphDrawrer(self.main.graph, self.main.MainMenuReturn, self.main.InfluenceMenuReturn, self.main.AdMenuReturn, self.main.RecommendationMenuReturn, self.main.GraphMenuReturn, self.main.EnvMenuReturn, (1920,1080))
        for n in range(0, 20):
            surface.blit(self.graphDrawrer.make_frame(), (0, 0))
            self.graphDrawrer.force_directed()
            pygame.display.update()
            clock.tick(60)
        for n in range(0,10):
            surface.blit(self.graphDrawrer.make_frame(), (0, 0))
            pygame.display.update()
            clock.tick(1)
        Recommendation(self.main.graph).newGraph("item1")
        for n in range(0,20):
            surface.blit(self.graphDrawrer.make_frame(), (0, 0))
            Recommendation(self.main.graph).layout()
            pygame.display.update()
            clock.tick(60)


    def preparePeople(self, graph):
        book1 = [230, 3, 249, 303, 224]
        book2 = [88, 41, 229, 22, 153]
        book3 = [292, 102, 338, 135, 142]
        for n in book1:
            graph.people[n].ratings.append(Rating("item1", 0.99))
        for n in book2:
            graph.people[n].ratings.append(Rating("item2", 0.99))
        for n in book3:
            graph.people[n].ratings.append(Rating("item3", 0.99))

RecommendationScen(Main())