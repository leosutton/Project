__author__ = 'Leo'
from Graph import Graph
from Person import Person, Relationship
import random
import math

class Loader(object):
    def __init__(self):
        self.graph = Graph()

    def load(self, input):
        file = input.split("\n")
        self.id = 0
        self.label = ""
        self.sex = ""
        self.source = 0
        self.target = 0
        for line in file:
            if line[2:4] == 'id':
                self.id = int(line[5:])
            if line[2:7] == 'label':
                self.label = line[9:-1]
            if line[2:5] == 'sex':
                if line[7:13] == 'female':
                    self.sex = 'f'
                else:
                    self.sex = 'm'
            if line[2:11] == 'wallcount':
                self.graph.people.append(Person(random.random(), random.random(), random.random(), random.random(), random.random()*2*math.pi, random.random(), self.sex, self.label))
            if line[2:8] == 'source':
                self.source = int(line[9:])
            if line[2:8] == 'target':
                self.target = int(line[9:])
                self.graph.connections.append(Relationship(self.graph.people[self.source], self.graph.people[self.target], random.random()))
                self.graph.connections.append(Relationship(self.graph.people[self.target], self.graph.people[self.source], random.random()))

        return self.graph