__author__ = 'Leo'
from Graph import Graph
import random
import math
import numpy as np

class Recommendation(object):

    def __init__(self, graph):
        self.graph = graph
        self.items = ["item1", "item2", "item3"]

    def intialise(self, number):
        for person in self.graph.people:
            person.ratings = []
        for n in range (0, number):
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

class Rating(object):

    def __init__(self, item, rating):
        self.item = item
        self.rating = rating

class Opinion(object):

    def __init__(self, item, opinion):
        self.item = item
        self.opinion = opinion