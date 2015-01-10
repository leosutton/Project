__author__ = 'Leo'
from tkinter import *
from tkinter import ttk
import pygame
from Graph import Graph
from Environment import Environment
from GraphDrawrer import GraphDrawrer


class Menu:
    def __init__(self):
        self.root = Tk()
        self.root.title = "Configuration"

        def start():
            self.start()
        left = StringVar()
        right = StringVar()

        content = ttk.Frame(self.root, padding =(3,3,12,12))
        title = ttk.Label(content, text="Configuration")
        start = ttk.Button(content, text="start", command=start)
        displays = ['Virtual', 'Actual', 'None']
        for option in displays:
            list1 = ttk.Radiobutton(content, text=option, variable=left, value=option)
            list1.grid(column=0, row=2+displays.index(option), sticky=(N), pady=5)

        for option in displays:
            list2 = ttk.Radiobutton(content, text=option, variable=right, value=option)
            list2.grid(column=1, row=2+displays.index(option), sticky=(N), pady=5)

        content.grid(column=0, row=0, sticky=(N,S,E,W))
        title.grid(column=0, row=0, columnspan=2, sticky=(N), pady=5)
        start.grid(column=0, row=1, columnspan=2, sticky=(N), pady=5)



        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)

        self.root.mainloop()

    def start(self):
        print ('start')
        self.root.destroy()
        self.setup()

    def setup(self):
        graph = Graph()
        environment = Environment(graph)
        graphDrawrer = GraphDrawrer(graph)

        pygame.init()
        surface = pygame.display.set_mode((1600, 600))

        while True:
            surface.blit(environment.make_frame(), (0,0))
            surface.blit(graphDrawrer.make_frame(), (800,0))
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(60)