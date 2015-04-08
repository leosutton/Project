class Person(object):
    def __init__(self, draw_x, draw_y, env_x, env_y, direction, views, sex, name = ""):
        self.draw_x = draw_x
        self.draw_y = draw_y
        self.env_x = env_x
        self.env_y = env_y
        self.direction = direction
        self.wall = []
        self.views = views
        self.sex = sex
        self.name = name


class Relationship(object):
    def __init__(self, first, second, strength):
        self.between = (first, second)
        self.strength = strength
