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

        def advertConfig():
            advertConfig = AdvertMenu(self.root, self.main)
            advertConfig.menu()

        def influenceConfig():
            influenceConfig = InfluenceMenu(self.root, self.menu)
            influenceConfig.menu()

        def recommendationConfig():
            recommendationConfig = RecommendationMenu(self.root, self.menu)
            recommendationConfig.menu()

        self.secondScreen = BooleanVar()
        self.advertActivate = BooleanVar()
        self.influenceActivate = BooleanVar()
        self.recommendationActivate = BooleanVar()

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
        advertActivate = ttk.Checkbutton(content, text="Activate Adverts", variable=self.advertActivate)
        advertConfig = ttk.Button(content, text="Configure Adverts", command=advertConfig)
        influenceActivate = ttk.Checkbutton(content, text="Activate Influence", variable=self.influenceActivate)
        influenceConfig = ttk.Button(content, text="Configure Influence", command=influenceConfig)
        recommendationActivate = ttk.Checkbutton(content, text="Activate Recommendation", variable=self.recommendationActivate)
        recommendationConfig = ttk.Button(content, text="Configure Recommendation", command=recommendationConfig)


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
        advertActivate.grid(column=0, row=8, sticky=(N), pady=5)
        advertConfig.grid(column=1, row=8, sticky=(N), pady=5)
        influenceActivate.grid(column=0, row=9, sticky=(N), pady=5)
        influenceConfig.grid(column=1, row=9, sticky=(N), pady=5)
        recommendationActivate.grid(column=0, row=10, sticky=(N), pady=5)
        recommendationConfig.grid(column=1, row=10, sticky=(N), pady=5)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)

        self.root.mainloop()

    def start(self):
        self.root.destroy()

class AdvertMenu(object):
    def menu(self):
        self.root.title("Advert Configuration")

        def save():
            self.save()

        submit = ttk.Button(self.root, text="save", command=save)
        submit.grid(column=0, row=1)

        seedLabel = ttk.Label(self.root, text="Seed Number")
        seedLabel.grid(column = 0, row=2)
        self.seedVar = StringVar()
        self.seedVar.set(10)
        seedEntry = ttk.Entry(self.root, textvariable = self.seedVar)
        seedEntry.grid(column = 1, row = 2)

        emailLabel = ttk.Label(self.root, text="Email Number")
        emailLabel.grid(column = 0, row=3)
        self.emailVar = StringVar()
        self.emailVar.set(10)
        emailEntry = ttk.Entry(self.root, textvariable = self.emailVar)
        emailEntry.grid(column = 1, row = 3)

        adLabel = ttk.Label(self.root, text="Ad Number")
        adLabel.grid(column = 0, row=4)
        self.adVar = StringVar()
        self.adVar.set(10)
        adEntry = ttk.Entry(self.root, textvariable = self.adVar)
        adEntry.grid(column = 1, row = 4)

        muLabel = ttk.Label(self.root, text="Mu Number")
        muLabel.grid(column = 0, row=5)
        self.muVar = StringVar()
        self.muVar.set(10)
        muEntry = ttk.Entry(self.root, textvariable = self.muVar)
        muEntry.grid(column = 1, row = 5)

        sigmaLabel = ttk.Label(self.root, text="Sigma Number")
        sigmaLabel.grid(column = 0, row=6)
        self.sigmaVar = StringVar()
        self.sigmaVar.set(10)
        sigmaEntry = ttk.Entry(self.root, textvariable = self.sigmaVar)
        sigmaEntry.grid(column = 1, row = 6)

        self.root.mainloop()

    def __init__(self, master, app):
        self.root = Toplevel(master)
        self.app = app

    def save(self):
        self.root.destroy()
        self.app.AdMenuReturn = advertConfiguration(self.seedVar.get(), self.emailVar.get(), self.adVar.get(), self.muVar.get(), self.sigmaVar.get())

class envConfiguration(object):
    def __init__(self, colour, facing, seen):
        self.colour = colour
        self.facing = facing
        self.seen = seen

class advertConfiguration(object):
    def __init__(self, seed, email, ad, mu, sigma):
        self.seed = seed
        self.email = email
        self.ad = ad
        self.mu = mu
        self.sigma = sigma

class influenceMenu(object):
    def menu(self):
        self.root.title("Advert Configuration")

        def save():
            self.save()

        submit = ttk.Button(self.root, text="save", command=save)
        submit.grid(column=0, row=1)

        seedLabel = ttk.Label(self.root, text="Seed Number")
        seedLabel.grid(column = 0, row=2)
        self.seedVar = StringVar()
        self.seedVar.set(10)
        seedEntry = ttk.Entry(self.root, textvariable = self.seedVar)
        seedEntry.grid(column = 1, row = 2)

        modelVar = StringVar()
        select1 = ttk.Radiobutton(self.root, text = "Influence model 1", variable = modelVar, value = "1")
        select1.grid(column = 0, row = 3)
        select2 = ttk.Radiobutton(self.root, text = "Influence model 2", variable = modelVar, value = "2")
        select2.grid(column = 0, row = 4)

        self.root.mainloop()

    def __init__(self, master, app):
        self.root = Toplevel(master)
        self.app = app

    def save(self):
        self.root.destroy()
        self.app.influenceMenuReturn = influenceConfiguration(self.seedVar.get(), self.modelVar.get())

class influenceConfiguration(object):
    def __init__(self, seed, type):
        self.seed = seed
        self.type = type

class RecommendationMenu(object):
    def menu(self):
        self.root.title("Recommendation Configuration")

        def save():
            self.save()

        submit = ttk.Button(self.root, text="save", command=save)
        submit.grid(column=0, row=1)

        seedLabel = ttk.Label(self.root, text="Seed Number")
        seedLabel.grid(column = 0, row=2)
        self.seedVar = StringVar()
        self.seedVar.set(10)
        seedEntry = ttk.Entry(self.root, textvariable = self.seedVar)
        seedEntry.grid(column = 1, row = 2)

        modelVar = StringVar()
        select1 = ttk.Radiobutton(self.root, text = "Influence model 1", variable = modelVar, value = "1")
        select1.grid(column = 0, row = 3)
        select2 = ttk.Radiobutton(self.root, text = "Influence model 2", variable = modelVar, value = "2")
        select2.grid(column = 0, row = 4)

        self.root.mainloop()

    def __init__(self, master, app):
        self.root = Toplevel(master)
        self.app = app

    def save(self):
        self.root.destroy()
        self.app.influenceMenuReturn = influenceConfiguration(self.seedVar.get(), self.modelVar.get())