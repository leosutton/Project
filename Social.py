__author__ = 'Leo'
from Wall import status, photo
import random
from GraphDrawrer import Transition

class Social(object):
    def __init__(self, graph, graphDrawrer, volatility = 1):
        self.graph = graph
        self.volatility = volatility
        self.graphDrawrer = graphDrawrer

    def initialiseGraph(self):
        for person in self.graph.people:
            pass

    def changeRelationship(self, personFrom, personTo, amount):
        relation = next(relation for relation in self.graph.connections if relation.between[0] == personFrom and relation.between[1] == personTo)
        relation.strength += amount

    def checkWall(self, person):
        neighbors = []
        for relationship in self.graph.connections:
            if relationship.between[0] == person:
                neighbors.append(relationship.between[1])
        newsfeed = []
        for neighbor in neighbors:
            if len(neighbor.wall) > 0:
                newsfeed.append(neighbor.wall[0])
        for post in newsfeed:
            if type(post) is status:
                if abs(post.views - person.views) < 0.5:
                    post.likes.append(person)
                    self.changeRelationship(person, post.poster, 0.1)
                    self.graphDrawrer.transitions.append(Transition(person, post.poster))
                else:
                    self.changeRelationship(person, post.poster, -0.1)
            elif type(post) is photo:
                if self.isTagged(post, person):
                    self.changeRelationship(person, photo.poster, 0.1)

    def isTagged(self, post, person):
        for tag in post.tagged:
            if person == tag:
                return True
        return False

    def postStatus(self, person):
        person.wall.append(status(person, person.views))

    def postPhoto(self, person):
        neighbors = self.graph.getNeighbors(person)
        tagged = []
        if len(neighbors) > 0:
            tagged = random.choice(neighbors)
        person.wall.append(photo(person, tagged))

    def decay(self, x):
        for connection in self.connections:
            connection.strength -= x
            if connection.strength < 0:
                self.connections.remove(connection)

    def check(self):
        for connection in self.connections:
            if connection.strength < 1:
                connection.strength = 1