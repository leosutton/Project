from Graph import Graph
from GraphDrawrer import GraphDrawrer
from Environment import Environment
import pygame
from MenuScreen import Menu


class Main(object):
    def run(self):
        choices = Menu(self)
        print(self.GraphMenuReturn)
        print(self.EnvMenuReturn)


if __name__ == '__main__':
    Main().run()