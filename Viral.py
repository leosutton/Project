__author__ = 'Leo'
import random
import math
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

class Viral(object):
#0 not participated; a recieved seed advert; s recieved seed email; n not going to participate; e recieved email from friend; 1 participated

    def __init__(self, graph, fromSeed, fromAd, fromEmail, mu, sigma):
        self.fromSeed = fromSeed
        self.fromAd = fromAd
        self.fromEmail = fromEmail
        self.participated = 0
        self.mu = mu
        self.sigma = sigma
        for person in graph.people:
            person.status = []

    def makeCampaign(self, graph):
        for person in graph.people:
            person.status.append("0")

    def seedAdvert(self, graph, proportion, campaign):
        for person in graph.people:
            if (person.status[campaign] == "0") and (random.random() < proportion):
                person.status[campaign] = "a"
                if random.random()*(1+person.totalPart*0.5) < self.fromAd:
                    self.participate(person, graph, campaign)


    def decayPart(self, graph):
        for person in graph.people:
            person.totalPart = min(0, person.totalPart - 1)

    def seedEmail(self, graph, number, campaign):
        for n in range(0,number):
            person = random.choice(graph.people)
            if person.status[campaign] == "0":
                person.status[campaign] = "s"
                number += 1

    def checkEmail(self, graph, campaign):
        toParticipate = []
        for person in graph.people:
            if person.status[campaign] == "s":
                if random.random()<self.fromSeed:
                    toParticipate.append(person)
                else:
                    person.participated = 'n'
            elif person.status[campaign] =="e":
                if random.random()*(1+person.totalPart*0.5) < self.fromEmail:
                    toParticipate.append(person)
                else:
                    person.participated = 'n'
        for person in toParticipate:
            self.participate(person, graph, campaign)

    def participate(self, person, graph, campaign):
        person.status[campaign] = "1"
        person.totalPart += 1
        connections = []
        invites = max(0, math.trunc(random.normalvariate(self.mu, self.sigma)))
        for connection in graph.connections:
            if connection.between[0] == person:
                connections.append(connection.between[1])
        for n in range(0, invites):
            if connections:
                invitee = random.choice(connections)
                connections.pop(connections.index(invitee))
                if invitee.status[campaign] == "0":
                    invitee.status[campaign] = "e"

    def record(self, graph, campaign):
        nothing = 0
        seedEmail = 0
        otherEmail = 0
        participated = 0
        rejected = 0
        for person in graph.people:
            if person.status[campaign] == "0":
                nothing += 1
            elif person.status[campaign] == "s":
                seedEmail += 1
            elif person.status[campaign] == "e":
                otherEmail += 1
            elif person.status[campaign] == "1":
                participated += 1
            elif person.status[campaign] == "n":
                rejected += 1
        return Numbers(nothing, seedEmail, otherEmail, participated, rejected)

class Numbers(object):
    def __init__(self, nothing, seedEmail, otherEmail, participated, rejected):
        self.nothing = nothing
        self.seedEmail = seedEmail
        self.otherEmail = otherEmail
        self.participated = participated
        self.rejected = rejected

class Campaign(object):
    def __init__(self, name, status):
        self.name = name
        self.status = status

