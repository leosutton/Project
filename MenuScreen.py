__author__ = 'Leo'
from tkinter import *
from tkinter import ttk
import pygame
from Graph import Graph
from Environment import Environment
from GraphDrawrer import GraphDrawrer
from DrawingController import DrawingController
from EnvMenu import EnvMenu
from graphMenu import GraphMenu


class Menu:
    def __init__(self, main):
        self.root = Tk()
        self.root.title("Configuration")
        self.main = main

        def start():
            self.start()

        def graphConfig():
            graphConfig = GraphMenu(self.root, self.main)
            graphConfig.menu()

        def envConfig():
            envConfig = EnvMenu(self.root, self.main)
            envConfig.menu()

        self.secondScreen = BooleanVar()

        left = StringVar()
        right = StringVar()

        content = ttk.Frame(self.root, padding=(3, 3, 12, 12))
        title = ttk.Label(content, text="Configuration")
        start = ttk.Button(content, text="start", command=start)
        second = ttk.Checkbutton(content, text="Second screen", variable=self.secondScreen)
        leftHeading = ttk.Label(content, text="First Screen")
        rightHeading = ttk.Label(content, text="Second Screen")
        envMenu = ttk.Button(content, text="Environment Configure", command=envConfig)
        graphMenu = ttk.Button(content, text="Graph Configure", command=graphConfig)

        displays = ['Virtual', 'Actual', 'None']
        for option in displays:
            list1 = ttk.Radiobutton(content, text=option, variable=left, value=option)
            list1.grid(column=0, row=4 + displays.index(option), sticky=(N), pady=5)

        for option in displays:
            list2 = ttk.Radiobutton(content, text=option, variable=right, value=option)
            list2.grid(column=1, row=4 + displays.index(option), sticky=(N), pady=5)

        content.grid(column=0, row=0, sticky=(N, S, E, W))
        title.grid(column=0, row=0, columnspan=2, sticky=(N), pady=5)
        second.grid(column=0, row=1, columnspan=2, sticky=(N), pady=5)
        start.grid(column=0, row=2, columnspan=2, sticky=(N), pady=5)
        leftHeading.grid(column=0, row=3, sticky=(N), pady=5)
        rightHeading.grid(column=1, row=3, sticky=(N), pady=5)
        envMenu.grid(column=0, row=7, sticky=(N), pady=5)
        graphMenu.grid(column=1, row=7, sticky=(N), pady=5)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)

        self.root.mainloop()

    def start(self):
        self.root.destroy()