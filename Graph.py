__author__ = 'Leo'
import random
import math

from Person import Person, Relationship


class Graph:
    people = []
    connections = []

    def __init__(self):
        self.generatePeople(50)
        self.generateFriendships(50)

    def generatePeople(self, number_of_nodes):
        for n in range(0, number_of_nodes):
            draw_x = random.random()
            draw_y = random.random()
            env_x = random.random()
            env_y = random.random()
            direction = random.random() * 2 * math.pi
            views = random.random()
            self.people.append(Person(draw_x, draw_y, env_x, env_y, direction, views))

    def generateFriendships(self, number_of_connections):
        for n in range(0, number_of_connections):
            first = random.choice(self.people)
            to = random.choice(self.people)
            strength = random.random()
            self.connections.append(Relationship(first, to, strength))

    def decay(self, x):
        for connection in self.connections:
            connection.strength -= x
            if connection.strength < 0:
                self.connections.remove(connection)

    def check(self):
        for connection in self.connections:
            if connection.strength < 1:
                connection.strength = 1