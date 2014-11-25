import math
import random
from Wall import photo, status


class Person():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.wall = []
        self.friends = []
        self.views = random.random()

    def view(node):
        newsfeed = []
        for neighbor in friends:
            if (len(neighbor.wall) > 0):
                for post in neighbor.wall:
                    newsfeed.append(post)
        for post in newsfeed:
            if isinstance(post, photo):
                pass
            elif isinstance(post, status):
                if math.fabs(post.views - g.node[node]['views'] > 20):
                    current_weight = g.edge[node][post.poster]['weight']
                    g.edge[node][post.poster]['weight'] = current_weight - 0.5
                    actions.append(('status', pos[post.poster], pos[node], 0))
                else:
                    current_weight = g.edge[node][post.poster]['weight']
                    g.edge[node][post.poster]['weight'] = current_weight - 0.5
                    actions.append(('status', pos[post.poster], pos[node], 1))