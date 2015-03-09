__author__ = 'Leo'
import pygame

from Environment import Environment
from GraphDrawrer import GraphDrawrer, Layout
from EnvMenu import envConfiguration
from graphMenu import graphConfiguration
from Viral import Viral
from Plotter import Plotter
from Influence import Influence1, Influence2
from Recommendation import Recommendation


class DrawingController(object):
    def __init__(self, main, ad, influence, recommendation, input, graph, env, people):
        self.mainConfig = main
        self.influenceConfig = influence
        self.adConfig = ad
        self.recommendationConfig = recommendation
        self.inputConfig = input
        self.graphConfig = graph
        self.envConfig = env
        self.graph = people
        pygame.init()
        surface = pygame.display.set_mode((1920, 1080))
        clock = pygame.time.Clock()

        self.graphDrawrer = GraphDrawrer(self.graph, self.mainConfig, self.influenceConfig, self.adConfig, self.recommendationConfig, self.graphConfig, self.envConfig)

        counter = 0
        record = {}
        if self.mainConfig.influence and self.influenceConfig.type == "1":
            influence = Influence1(self.graph)
            influence.initialiseGraph()
            influence.startingNodes(int(self.influenceConfig.seed))

        if self.mainConfig.influence and self.influenceConfig.type == "2":
            influence = Influence2(self.graph)
            influence.initialiseGraph()
            influence.startingNodes(int(self.influenceConfig.seed))

        if self.mainConfig.recommendation:
            recommendation = Recommendation(self.graph)
            recommendation.intialise(self.recommendationConfig.seed)
            for person in self.graph.people:
                person.item1 = recommendation.getRecommendation(person, "item1")
            for person in self.graph.people:
                person.item2 = recommendation.getRecommendation(person, "item2")
            for person in self.graph.people:
                person.item3 = recommendation.getRecommendation(person, "item3")

        for n in range(0, 50):
            surface.blit(self.graphDrawrer.make_frame(), (0, 0))
            Layout(self.graph).force_directed()
            pygame.display.update()
            clock.tick(60)

        if self.mainConfig.advert:
            viral = Viral(self.graph, float(self.adConfig.seed), float(self.adConfig.email), float(self.adConfig.ad), float(self.adConfig.mu), float(self.adConfig.sigma))
            viral.seedEmail(self.graph, 5)
            viral.seedAdvert(self.graph, 0.1)
            record[counter] = viral.record(self.graph)

        while self.graphDrawrer.go:
            counter += 1
            surface.blit(self.graphDrawrer.make_frame(), (0, 0))
            pygame.display.update()
            clock.tick(60)
            if counter % 5 == 0:
                if self.mainConfig.advert:
                    viral.checkEmail(self.graph)
                    record[counter] = viral.record(self.graph)
                if self.mainConfig.influence:
                    influence.process()

        Plotter(record)