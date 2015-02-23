__author__ = 'Leo'
from Graph import Graph
import random
import math

class Viral(object):
    def __init__(self, graph, fromSeed, fromAd, fromEmail, mu, sigma):
        self.fromSeed = fromSeed
        self.fromAd = fromAd
        self.fromEmail = fromEmail
        self.participated = 0
        self.mu = mu
        self.sigma = sigma
        for person in graph.people:
            person.participated = "0"

    def seedAdvert(self, graph, proportion):
        for person in graph.people:
            if (person.participated == "0") and (random.random() < proportion):
                person.participated = "a"
                if random.random() < self.fromAd:
                    self.participate(person, graph)

    def seedEmail(self, graph, number):
        for n in range(0,number):
            person = random.choice(graph.people)
            if person.participated == "0":
                person.participated = "s"
            else:
                number += 1

    def checkEmail(self, graph):
        toParticipate = []
        for person in graph.people:
            if person.participated == "s":
                if random.random()<self.fromSeed:
                    toParticipate.append(person)
                else:
                    person.participated = 'n'
            elif person.participated =="e":
                if random.random() < self.fromEmail:
                    toParticipate.append(person)
                else:
                    person.participated = 'n'
        for person in toParticipate:
            self.participate(person, graph)

    def participate(self, person, graph):
        person.participated = "1"
        connections = []
        invites = max(0, math.trunc(random.normalvariate(self.mu, self.sigma)))
        for connection in graph.connections:
            if connection.between[0] == person:
                connections.append(connection.between[1])
        for n in range(0, invites):
            if connections:
                invitee = random.choice(connections)
                connections.pop(connections.index(invitee))
                if invitee.participated == "0":
                    invitee.participated = "e"

    def record(self, graph):
        nothing = 0
        seedEmail = 0
        otherEmail = 0
        participated = 0
        rejected = 0
        for person in graph.people:
            if person.participated == "0":
                nothing += 1
            elif person.participated == "s":
                seedEmail += 1
            elif person.participated == "e":
                otherEmail += 1
            elif person.participated == "1":
                participated += 1
            elif person.participated == "n":
                rejected += 1
        return Numbers(nothing, seedEmail, otherEmail, participated, rejected)

class Numbers(object):
    def __init__(self, nothing, seedEmail, otherEmail, participated, rejected):
        self.nothing = nothing
        self.seedEmail = seedEmail
        self.otherEmail = otherEmail
        self.participated = participated
        self.rejected = rejected