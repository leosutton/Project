__author__ = 'Leo'
from scipy.special import binom


class Clustering(object):
    def __init__(self, graph):
        self.graph = graph

    def findTriangles(self):
        triplets = 0
        triangles = 0
        for node in self.graph.people:
            trianglesHere = 0
            connected = []
            for connection in self.graph.connections:
                if connection.between[0] is node:
                    connected.append(connection.between[1])
            triplets += binom(len(connected), 2)
            for connection in self.graph.connections:
                if connection.between[0] in connected:
                    if connection.between[1] in connected:
                        trianglesHere += 1
            triangles += trianglesHere / 2
        print(str(triplets) + " triplets")
        print(str(triangles) + " triangles")
        if triplets == 0:
            print("no triplets found")
            return 0
        else:
            return triangles / triplets