__author__ = 'Leo'
import random

class Influence1(object):
    def __init__(self, graph):
        self.graph = graph

    def initialiseGraph(self):
        for person in self.graph.people:
            person.adoption = random.random() + 1
            person.adopted = False
            person.influence = 0

    def startingNodes(self, number):
        for n in range(0, number):
            person = random.choice(self.graph.people)
            person.adopted = True

    def process(self, count):
        for person in self.graph.people:
            neighbors = []
            weights = []
            weight = 0
            for connection in self.graph.connections:
                if connection.between[0] == person:
                    neighbors.append(connection)
                    weights.append(connection.strength)
            for connection in neighbors:
                weight += connection.strength
            for n in range (0, len(neighbors)):
                if neighbors[n].between[1].adopted:
                    person.influence += weights[n]
            if not weight == 0:
                if person.influence/weight > person.adoption:
                    person.adopted = True
                    person.adoptedOn = count

class Influence2(object):
    def __init__(self, graph, chance = 1):
        self.graph = graph
        self.chance = chance

    def initialiseGraph(self):
        for person in self.graph.people:
            person.adopted = False

    def startingNodes(self, number):
        for n in range(0, number):
            person = random.choice(self.graph.people)
            person.adopted = True


    def process(self, count):
        for person in self.graph.people:
            if person.adopted:
                neighbors = []
                strengths = []
                adopted = []
                for connection in self.graph.connections:
                    if connection.between[0] == person:
                        neighbors.append(connection.between[1])
                        strengths.append(connection.strength)
                for n in range (0, len(neighbors)):
                    if random.random()*self.chance < strengths[n]:
                        adopted.append(neighbors[n])
                for neighbor in adopted:
                    neighbor.adopted = True
                    neighbor.adoptedOn = count