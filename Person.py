class Person(object):
    def __init__(self, x, y, env_x, env_y, direction, views, sex, name = ""):
        self.x = x
        self.y = y
        self.env_x = env_x
        self.env_y = env_y
        self.direction = direction
        self.wall = []
        self.views = views
        self.sex = sex
        self.name = name
        self.selected = False


class Relationship(object):
    def __init__(self, first, second, strength):
        self.between = (first, second)
        self.strength = strength
