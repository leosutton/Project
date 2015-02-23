__author__ = 'Leo'
import pygame

from Environment import Environment
from GraphDrawrer import GraphDrawrer
from EnvMenu import envConfiguration
from graphMenu import graphConfiguration
from Viral import Viral
from Plotter import Plotter
from Influence import Influence1, Influence2
from Recommendation import Recommendation


class DrawingController(object):
    def __init__(self, main, influence, ad, recommendation, input, graph, env, people):
        self.mainConfig = main
        self.influenceConfig = influence
        self.adConfig = ad
        self.recommendationConfig = recommendation
        self.inputConfig = input
        self.graphConfig = graph
        self.envConfig = env
        self.graph = people
        pygame.init()
        surface = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()

        self.graphDrawrer = GraphDrawrer(self.graph, self.mainConfig, self.influenceConfig, self.adConfig, self.recommendationConfig, self.graphConfig, self.envConfig)

        counter = 0
        record = {}
        if self.mainConfig.influence and self.influenceConfig.type == "1":
            influence = Influence1(graph)
            influence.initialiseGraph()
            influence.startingNodes(self.influenceConfig.seed)

        if self.mainConfig.influence and self.influenceConfig.type == "2":
            influence = Influence2(graph)
            influence.initialiseGraph()
            influence.startingNodes(self.influenceConfig.seed)

        if self.mainConfig.recommendation:
            recommendation = Recommendation(graph)
            recommendation.intialise(self.recommendationConfig.seed)
            for person in graph.people:
                person.item1 = recommendation.getRecommendation(person, "item1")
            for person in graph.people:
                person.item2 = recommendation.getRecommendation(person, "item2")
            for person in graph.people:
                person.item3 = recommendation.getRecommendation(person, "item3")

        for n in range(0, 20):
            surface.blit(self.graphDrawrer.make_frame(), (0, 0))
            pygame.display.update()
            clock.tick(60)

        if self.mainConfig.advert:
            viral = Viral(graph, self.adConfig.seed, self.adConfig.email, self.adConfig.ad, self.adConfig.mu, self.adConfig.sigma)
            viral.seedEmail(graph, 5)
            viral.seedAdvert(graph, 0.1)
            record[counter] = viral.record(graph)
        for n in range(0, 1000):
            counter += 1
            surface.blit(self.graphDrawrer.make_frame(), (0, 0))
            pygame.display.update()
            clock.tick(60)
            if counter % 5 == 0:
                if self.mainConfig.advert == '1':
                    viral.checkEmail(graph)
                    record[counter] = viral.record(graph)
                if self.mainConfig == '1':
                    influence.process()

        if self.mainConfig == '1':
            Plotter(record)