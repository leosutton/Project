__author__ = 'Leo'
import random
import math

from Person import Person, Relationship


class Graph:
    def __init__(self):
        self.people = []
        self.connections = []

    def generatePeople(self, number_of_nodes):
        for n in range(0, number_of_nodes):
            draw_x = random.random()
            draw_y = random.random()
            env_x = random.random()
            env_y = random.random()
            direction = random.random() * 2 * math.pi
            views = random.random()
            if random.random <0.5:
                sex = 'm'
            else:
                sex = 'f'
            self.people.append(Person(draw_x, draw_y, env_x, env_y, direction, views, sex))

    def generateFriendships(self, number_of_connections):
        for n in range(0, number_of_connections):
            first = random.choice(self.people)
            to = random.choice(self.people)
            strength = random.random()
            self.connections.append(Relationship(first, to, strength))

    def trim(self, number):
        if number < len(self.people):
            self.people = self.people[:number]
            for connection in self.connections:
                if (not (connection.between[0] in self.people)) or (not (connection.between[1] in self.people)):
                    self.connections.remove(connection)

    def getNeighbors(self, person):
        neighbors = []
        for connection in self.connections:
            if connection.between[0] == person:
                neighbors.append(connection.between[1])
        return neighbors