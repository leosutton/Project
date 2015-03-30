__author__ = 'Leo'

class Wall(object):
    contents = []

class photo(object):
    def __init__(self, poster, tagged = []):
        self.poster = poster
        self.tagged = []
        self.likes = []

class status(object):
    def __init__(self, poster, views):
        self.poster = poster
        self.views = views
        self.likes = []