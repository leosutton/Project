__author__ = 'Leo'
from Graph import Graph
import random
import math
import numpy as np

class Recommendation(object):

    def __init__(self, graph):
        self.graph = graph
        self.items = ["item1", "item2", "item3", "item4"]

    def intialise(self, number):
        for person in self.graph.people:
            person.ratings = []
        for n in range (0,number):
            item = random.choice(self.items)
            rating = random.random()
            person = random.choice(self.graph.people)
            person.ratings.append(Rating(item, rating))

    def getRecommendation(self, person, item, level = 0):
        neighbors = []
        weights = []
        opinions = []
        for connection in self.graph.connections:
            if connection.between[0] == person:
                neighbors.append(connection.between[1])
                weights.append(connection.strength)
        for n in range(0, len(neighbors)):
            person = neighbors[n]
            for rating in person.ratings:
                if rating.item == item:
                    opinions.append(rating.rating * weights[n])
                else:
                    if level < 2:
                        opinions.append(self.getRecommendation(person, item, level + 1)* weights[n])
                    else:
                        return 0
        average = 0
        for thing in opinions:
            average += thing
        if len(opinions) > 0:
            average /= len(opinions)
        return average

    def newGraph(self, item):
        connections = self.graph.connections
        for person in self.graph.people:
            if len(person.ratings) > 0:
                for rating in person.ratings:
                    if rating.item == "item1":
                        person.item1 = rating.rating
                    if rating.item == "item2":
                        person.item2 = rating.rating
                    if rating.item == "item3":
                        person.item3 = rating.rating
        if item == "item1":
            for connection in connections:
                connection.strengthOpinion = 1/(connection.between[0].item1-connection.between[1].item1+0.01)**2
        if item == "item2":
            for connection in connections:
                connection.strengthOpinion = 1/(connection.between[0].item2-connection.between[1].item2+0.01)**2
        if item == "item3":
            for connection in connections:
                connection.strengthOpinion = 1/(connection.between[0].item3-connection.between[1].item3+0.01)**2

    def displace(self, person, t):
        [person.draw_x, person.draw_y] = [person.draw_x, person.draw_y] + (person.displacement / self.distance(
            person.displacement)) * min(self.distance(person.displacement), t)
        person.draw_x = min(0.95, max(0.05, person.draw_x))
        person.draw_y = min(0.95, max(0.05, person.draw_y))

    def repel(self, k, person):
        person.displacement = [0, 0]
        for other in self.graph.people:
            if not (person is other):
                delta = np.array([person.draw_x - other.draw_x, person.draw_y - other.draw_y])
                person.displacement += (delta / self.distance(delta)) * self.repulsion(k,
                                                                                       self.distance(
                                                                                           delta))
    def attract(self, connection, k):
        if not (connection.between[0] in self.graph.people):
            self.graph.connections.remove(connection)
            return
        if not (connection.between[1] in self.graph.people):
            self.graph.connections.remove(connection)
            return
        delta = np.array([connection.between[0].draw_x - connection.between[1].draw_x,
                          connection.between[0].draw_y - connection.between[1].draw_y])
        connection.between[0].displacement -= (delta / self.distance(
            delta)) * self.attraction(k, self.distance(delta)) * connection.strengthOpinion
        connection.between[1].displacement += (delta / self.distance(
            delta)) * self.attraction(k, self.distance(delta)) * connection.strengthOpinion

    def layout(self):
        k = 0.7 * math.sqrt(1.0 / len(self.graph.people))
        t = 0.1
        for x in range (0,2):
            for person in self.graph.people:
                self.repel(k, person)
            for connection in self.graph.connections:
                self.attract(connection, k)
            for person in self.graph.people:
                self.displace(person, t)

    def attraction(self, k, x):
        return (x ** 2) / (2*k)

    def repulsion(self, k, x):
        if (x == 0):
            return 0.001
        else:
            return (k ** 2) / (2*x)

    def distance(self, delta):
        dis = math.sqrt(delta[0] ** 2 + delta[1] ** 2)
        if not dis == 0:
            return dis
        else:
            return 0.00001

class Rating(object):

    def __init__(self, item, rating):
        self.item = item
        self.rating = rating

class Opinion(object):

    def __init__(self, item, opinion):
        self.item = item
        self.opinion = opinion