__author__ = 'leo'
from shapely.geometry import LineString
from shapely.geometry.point import Point

class LineIntersection(object):
    def __init__(self, graph):
        self.lines = []
        self.intersections = []
        self.unique_intersections = []
        self.graph = graph
        self.importGraph(self.graph)
        self.intersection_numbers(self.lines)

    def intersection_numbers(self, lines):
        number = 0
        for line in lines:
            print(str(number) + "/" + str(len(lines)))
            number += 1
            for other in lines:
                if not line == other:
                    intersection = line.intersection(other)
                    if type(intersection) is Point:
                        self.intersections.append(intersection)
        # number = 0
        # for intersection in self.intersections:
        #     print(str(number) + "/" + str(len(self.intersections)))
        #     number += 1
        #     if not intersection in self.unique_intersections:
        #         self.unique_intersections.append(intersection)
        print(len(self.intersections))

    def importGraph(self, graph):
        for relationship in graph.connections:
            person_from  = relationship.between[0]
            person_to = relationship.between[1]
            line = LineString([(person_from.x, person_from.y), (person_to.x, person_to.y)])
            self.lines.append(line)