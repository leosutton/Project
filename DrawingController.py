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
from Social import Social
from Intersection import LineIntersection
import random


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
        self.environment = Environment(self.graph, self.envConfig)
        pygame.init()
        surface = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("User Interactions")
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

        if self.mainConfig.social:
            social = Social(self.graph, self.graphDrawrer)

        if int(self.inputConfig.cull) < len(self.graph.connections):
            self.graph.trim(int(self.inputConfig.cull))
            for n in range(0,10):
                for connection in self.graph.connections:
                    if not (connection.between[0] in self.graph.people):
                        self.graph.connections.remove(connection)

                for connection in self.graph.connections:
                    if not (connection.between[1] in self.graph.people):
                        self.graph.connections.remove(connection)

#        LineIntersection(self.graph)

        for n in range(0, 20):
            Layout(self.graph).force_directed()
            if self.mainConfig.second:
                graph = pygame.transform.scale(self.graphDrawrer.make_frame(True), (960 , 1080))
                env = pygame.transform.scale(self.environment.make_frame(), (960, 1080))
                surface.blit(graph, (0, 0))
                surface.blit(env, (960, 0))
            else:
                surface.blit(self.graphDrawrer.make_frame(True), (0,0))
            pygame.display.update()
            clock.tick(60)

#        LineIntersection(self.graph)

        if self.mainConfig.advert:
            viral = Viral(self.graph, float(self.adConfig.seed), float(self.adConfig.email), float(self.adConfig.ad), float(self.adConfig.mu), float(self.adConfig.sigma))
            for person in self.graph.people:
                person.totalPart = 0
            viral.makeCampaign(self.graph)
            viral.seedEmail(self.graph, 5, 0)
            viral.seedAdvert(self.graph, 0.1, 0)
            record[counter] = viral.record(self.graph, 0)

        while self.graphDrawrer.go:
            counter += 1
            if self.mainConfig.social:
                if (counter%60 == 0):
                    for person in self.graph.people:
                        social.checkWall(person)
                        if random.random() < 0.1:
                            social.postPhoto(person)
                        if random.random() < 0.1:
                            social.postStatus(person)
            if self.mainConfig.second:
                graph = pygame.transform.scale(self.graphDrawrer.make_frame(), (960 , 1080))
                env = pygame.transform.scale(self.environment.make_frame(), (960, 1080))
                surface.blit(graph, (0, 0))
                surface.blit(env, (960, 0))
            else:
                surface.blit(self.graphDrawrer.make_frame(), (0,0))
            pygame.display.update()
            clock.tick(60)
            if counter % 5 == 0:
                if self.mainConfig.advert:
                    viral.checkEmail(self.graph, 0)
                    record[counter] = viral.record(self.graph, 0)
                if self.mainConfig.influence:
                    influence.process(counter)

        Plotter(record)