__author__ = 'Leo'
from MenuScreen import influenceConfiguration, inputConfiguration, mainConfiguration, advertConfiguration, recommendationConfiguration
from graphMenu import graphConfiguration
from EnvMenu import envConfiguration
from GraphDrawrer import GraphDrawrer, Layout
from Main import Main
from Influence import Influence1, Influence2
from copy import deepcopy
from Recommendation import Recommendation, Rating
import pygame
from pygame.locals import *
from Viral import Viral
from Plotter import Plotter
from MenuScreen import advertConfiguration, AdvertMenu


class influenceScen(object):
    def __init__(self, main=Main()):
        self.main = main
        self.main.MainMenuReturn = mainConfiguration(False, False, True, False)
        self.main.InfluenceMenuReturn1 = influenceConfiguration('10', '1')
        self.main.InfluenceMenuReturn2 = influenceConfiguration('10', '2')
        f = open("graph.gml")
        self.main.InputMenuReturn = inputConfiguration("1", f.read(), "1000", "100", "100")
        self.main.AdMenuReturn = advertConfiguration('0.2', '0.2', '0.7', '7', '2')
        self.main.GraphMenuReturn = graphConfiguration("None", "None", '1')
        self.main.EnvMenuReturn = envConfiguration("None", True, True)
        self.main.RecommendationMenuReturn = recommendationConfiguration(5)
        self.main.makeGraph()
        Influence1(self.main.graph).initialiseGraph()
        pygame.init()
        surface = pygame.display.set_mode((1920, 1080))
        clock = pygame.time.Clock()
        self.graphDrawrer = GraphDrawrer(self.main.graph, self.main.MainMenuReturn, self.main.InfluenceMenuReturn1, self.main.AdMenuReturn, self.main.RecommendationMenuReturn, self.main.GraphMenuReturn, self.main.EnvMenuReturn, (1920,1080))
        for n in range(0, 15):
            surface.blit(self.graphDrawrer.make_frame(True), (0, 0))
            Layout(self.main.graph).force_directed()
            pygame.display.update()
            clock.tick(60)
        stay = True
        while stay:
            rectangles = []
            self.graphDrawrer.surface.fill((255, 255, 255))
            for person in self.main.graph.people:
                if person.adopted:
                    rectangles.append(pygame.draw.circle(self.graphDrawrer.surface, (255, 0, 0),
                                       (int(self.graphDrawrer.getx(person.drawx)), int(self.graphDrawrer.gety(person.drawy))),
                                       15, 5))
                else:
                    rectangles.append(pygame.draw.circle(self.graphDrawrer.surface, (0, 255, 0),
                                       (int(self.graphDrawrer.getx(person.drawx)), int(self.graphDrawrer.gety(person.drawy))),
                                       15, 5))
            self.graphDrawrer.drawConnections()
            events = pygame.event.get()
            position = (0,0)
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    position = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                stay = False
            for circle in rectangles:
                if circle.collidepoint(position):
                    if self.main.graph.people[rectangles.index(circle)].adopted == False:
                        self.main.graph.people[rectangles.index(circle)].adopted = True
                        self.main.graph.people[rectangles.index(circle)].adoptedOn = 0
                    else:
                        self.main.graph.people[rectangles.index(circle)].adopted = False
            clock.tick(60)
            surface.blit(self.graphDrawrer.make_frame(), (0, 0))
            pygame.display.update()
        self.main.graph1 = deepcopy(self.main.graph)
        self.main.graph0 = deepcopy(self.main.graph)
        self.graphDrawrer0 = GraphDrawrer(self.main.graph0, self.main.MainMenuReturn, self.main.InfluenceMenuReturn1, self.main.AdMenuReturn, self.main.RecommendationMenuReturn, self.main.GraphMenuReturn, self.main.EnvMenuReturn, (960,1080))
        self.graphDrawrer1 = GraphDrawrer(self.main.graph1, self.main.MainMenuReturn, self.main.InfluenceMenuReturn2, self.main.AdMenuReturn, self.main.RecommendationMenuReturn, self.main.GraphMenuReturn, self.main.EnvMenuReturn, (960,1080))
#        self.prepareSeperate(self.main.graph)
#        self.prepareTogether(self.main.graph1)
        stay = True
        count = 1
        while stay:
            count += 1
            surface.blit(self.graphDrawrer1.make_frame(), (960, 0))
            surface.blit(self.graphDrawrer0.make_frame(), (0,0))
            Influence1(self.main.graph0).process(count)
            Influence2(self.main.graph1, 8).process(count)
            pygame.display.update()
            clock.tick(1)
            keys = pygame.key.get_pressed()
            if keys[K_BACKSPACE]:
                stay = False
        while True:
            multiple = 255/count
            self.graphDrawrer.surface.fill((255, 255, 255))
            for person in self.main.graph.people:
                if person.adopted:
                    if hasattr(person, "adoptedOn"):
                        pygame.draw.circle(self.graphDrawrer.surface, (255*multiple*person.adoptedOn, 0, 0),
                                           (int(self.graphDrawrer.getx(person.drawx)), int(self.graphDrawrer.gety(person.drawy))),
                                           15, 5)
                    else:
                        print("person without adopted On")
                else:
                    pygame.draw.circle(self.graphDrawrer.surface, (0, 255, 0),
                                       (int(self.graphDrawrer.getx(person.drawx)), int(self.graphDrawrer.gety(person.drawy))),
                                       15, 5)
            self.graphDrawrer.drawConnections()
            clock.tick(60)
            surface.blit(self.graphDrawrer.surface, (0, 0))
            pygame.display.update()

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
        for person in self.main.graph.people:
            person.totalPart = 0
        surface = pygame.display.set_mode((1920, 1080))
        clock = pygame.time.Clock()
        self.graphDrawrer = GraphDrawrer(self.main.graph, self.main.MainMenuReturn, self.main.InfluenceMenuReturn, self.main.AdMenuReturn, self.main.RecommendationMenuReturn, self.main.GraphMenuReturn, self.main.EnvMenuReturn, (1920,1080))
        viral = Viral(self.main.graph, float(self.main.AdMenuReturn.seed), float(self.main.AdMenuReturn.email), float(self.main.AdMenuReturn.ad), float(self.main.AdMenuReturn.mu), float(self.main.AdMenuReturn.sigma))
        viral.makeCampaign(self.main.graph)
        viral.seedEmail(self.main.graph, 5, 0)
        viral.seedAdvert(self.main.graph, 0.1, 0)
        record = {}
        counter = 0
        record[counter] = viral.record(self.main.graph, 0)
        for n in range(0, 15):
            Layout(self.main.graph).force_directed()
            surface.blit(self.graphDrawrer.make_frame(True), (0, 0))
            pygame.display.update()
            clock.tick(60)
        stay = True
        notExit = True
        current = 0
        while notExit:
            while stay:
                counter += 1
                viral.checkEmail(self.main.graph, current)
                record[counter] = viral.record(self.main.graph, current)
                surface.blit(self.graphDrawrer.make_frame(current=current), (0,0))
                clock.tick(1)
                pygame.display.update()
                keys = pygame.key.get_pressed()
                if keys[K_BACKSPACE]:
                    stay = False
                if keys[K_ESCAPE]:
                    notExit = False
                if counter % 20 == 0:
                    viral.decayPart(self.main.graph)
            AdvertMenu(self).menu()
            stay = True
            current += 1
            viral.makeCampaign(self.main.graph)
            viral.seedEmail(self.main.graph, 5, current)
            viral.seedAdvert(self.main.graph, 0.1, current)
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
            surface.blit(self.graphDrawrer.make_frame(True), (0, 0))
            Layout(self.main.graph).force_directed()
            pygame.display.update()
            clock.tick(60)
        for n in range(0,60):
            surface.blit(self.graphDrawrer.make_frame(), (0, 0))
            pygame.display.update()
            clock.tick(60)
        self.graphTL = deepcopy(self.main.graph)
        self.graphTR = deepcopy(self.main.graph)
        self.graphBL = deepcopy(self.main.graph)
        self.graphBR = deepcopy(self.main.graph)
        self.graphDrawrerTL = GraphDrawrer(self.graphTL, self.main.MainMenuReturn, self.main.InfluenceMenuReturn, self.main.AdMenuReturn, self.main.RecommendationMenuReturn, self.main.GraphMenuReturn, self.main.EnvMenuReturn, (960,540))
        self.graphDrawrerTR = GraphDrawrer(self.graphTR, self.main.MainMenuReturn, self.main.InfluenceMenuReturn, self.main.AdMenuReturn, self.main.RecommendationMenuReturn, self.main.GraphMenuReturn, self.main.EnvMenuReturn, (960,540))
        self.graphDrawrerBL = GraphDrawrer(self.graphBL, self.main.MainMenuReturn, self.main.InfluenceMenuReturn, self.main.AdMenuReturn, self.main.RecommendationMenuReturn, self.main.GraphMenuReturn, self.main.EnvMenuReturn, (960,540))
        self.graphDrawrerBR = GraphDrawrer(self.graphBR, self.main.MainMenuReturn, self.main.InfluenceMenuReturn, self.main.AdMenuReturn, self.main.RecommendationMenuReturn, self.main.GraphMenuReturn, self.main.EnvMenuReturn, (960,540))
        for n in range(0,20):
            surface.blit(self.graphDrawrerTL.make_frame(), (0, 0), (0, 0, 960, 540))
            surface.blit(self.graphDrawrerTR.make_frame(), (960, 0), (960, 0, 960, 540))
            surface.blit(self.graphDrawrerBL.make_frame(), (0, 540), (0, 540, 960, 540))
            surface.blit(self.graphDrawrerBR.make_frame(), (960, 540), (960, 540, 960, 540))
            Layout(self.graphTL).force_directed()
            for person in self.graphTL.people:
                for rating in person.ratings:
                    if rating.item == "item1":
                        person.draw_x += (rating.rating)-0.5
            Layout(self.graphTR).force_directed()
            for person in self.graphTL.people:
                for rating in person.ratings:
                    if rating.item == "item2":
                        person.draw_x += (rating.rating)-0.5
            Layout(self.graphBL).force_directed()
            for person in self.graphTL.people:
                for rating in person.ratings:
                    if rating.item == "item3":
                        person.draw_x += (rating.rating)-0.5
            Layout(self.graphBR).force_directed()
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