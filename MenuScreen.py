__author__ = 'Leo'
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
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
            influenceConfig = influenceMenu(self.root, self.main)
            influenceConfig.menu()

        def recommendationConfig():
            recommendationConfig = RecommendationMenu(self.root, self.main)
            recommendationConfig.menu()

        def inputConfig():
            inputConfig = InputMenu(self.root, self.main)
            inputConfig.menu()

        def socialConfig():
            socialConfig = SocialMenu(self.root, self.main)
            socialConfig.menu()

        self.secondScreen = BooleanVar()
        self.advertActivate = BooleanVar()
        self.influenceActivate = BooleanVar()
        self.recommendationActivate = BooleanVar()
        self.socialActiavate = BooleanVar()

        content = ttk.Frame(self.root, padding=(3, 3, 12, 12))
        title = ttk.Label(content, text="Configuration")
        start = ttk.Button(content, text="start", command=start)
        second = ttk.Checkbutton(content, text="Second screen", variable=self.secondScreen)
        leftHeading = ttk.Label(content, text="First Screen")
        rightHeading = ttk.Label(content, text="Second Screen")
        inputMenu = ttk.Button(content, text="Configure Input", command=inputConfig)
        envMenu = ttk.Button(content, text="Environment Configure", command=envConfig)
        graphMenu = ttk.Button(content, text="Graph Configure", command=graphConfig)
        advertActivate = ttk.Checkbutton(content, text="Activate Adverts", variable=self.advertActivate)
        advertConfig = ttk.Button(content, text="Configure Adverts", command=advertConfig)
        influenceActivate = ttk.Checkbutton(content, text="Activate Influence", variable=self.influenceActivate)
        influenceConfig = ttk.Button(content, text="Configure Influence", command=influenceConfig)
        recommendationActivate = ttk.Checkbutton(content, text="Activate Recommendation",
                                                 variable=self.recommendationActivate)
        recommendationConfig = ttk.Button(content, text="Configure Recommendation", command=recommendationConfig)
        socialActivate = ttk.Checkbutton(content, text="Activate Social", variable=self.socialActiavate)
        socialConfig = ttk.Button(content, text="Configure Social", command=socialConfig)

        content.grid(column=0, row=0, sticky=(N, S, E, W))
        title.grid(column=0, row=0, columnspan=2, sticky=(N), pady=5)
        second.grid(column=0, row=1, columnspan=2, sticky=(N), pady=5)
        start.grid(column=0, row=2, columnspan=2, sticky=(N), pady=5)
        leftHeading.grid(column=0, row=3, sticky=(N), pady=5)
        rightHeading.grid(column=1, row=3, sticky=(N), pady=5)
        inputMenu.grid(column=0, row=4)
        envMenu.grid(column=0, row=8, sticky=(N), pady=5)
        graphMenu.grid(column=1, row=8, sticky=(N), pady=5)
        advertActivate.grid(column=0, row=9, sticky=(N), pady=5)
        advertConfig.grid(column=1, row=9, sticky=(N), pady=5)
        influenceActivate.grid(column=0, row=10, sticky=(N), pady=5)
        influenceConfig.grid(column=1, row=10, sticky=(N), pady=5)
        recommendationActivate.grid(column=0, row=11, sticky=(N), pady=5)
        recommendationConfig.grid(column=1, row=11, sticky=(N), pady=5)
        socialActivate.grid(column=0, row=12, sticky=(N), pady=5)
        socialConfig.grid(column=1, row=12, sticky=(N), pady=5)


        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)

        self.root.mainloop()

    def start(self):
        self.root.destroy()
        self.main.MainMenuReturn = mainConfiguration(self.secondScreen.get(), self.advertActivate.get(), self.influenceActivate.get(), self.recommendationActivate.get(), self.socialActiavate.get())

class mainConfiguration(object):
    def __init__(self, second, advert, influence, recommendation, social):
        self.second = second
        self.advert = advert
        self.influence = influence
        self.recommendation = recommendation
        self.social = social

class AdvertMenu(object):
    def menu(self):
        self.root.title("Advert Configuration")

        def save():
            self.save()

        submit = ttk.Button(self.root, text="save", command=save)
        submit.grid(column=0, row=1)

        seedLabel = ttk.Label(self.root, text="Seed Number")
        seedLabel.grid(column=0, row=2)
        self.seedVar = StringVar()
        self.seedVar.set(10)
        seedEntry = ttk.Entry(self.root, textvariable=self.seedVar)
        seedEntry.grid(column=1, row=2)

        emailLabel = ttk.Label(self.root, text="Email Number")
        emailLabel.grid(column=0, row=3)
        self.emailVar = StringVar()
        self.emailVar.set(10)
        emailEntry = ttk.Entry(self.root, textvariable=self.emailVar)
        emailEntry.grid(column=1, row=3)

        adLabel = ttk.Label(self.root, text="Ad Number")
        adLabel.grid(column=0, row=4)
        self.adVar = StringVar()
        self.adVar.set(10)
        adEntry = ttk.Entry(self.root, textvariable=self.adVar)
        adEntry.grid(column=1, row=4)

        muLabel = ttk.Label(self.root, text="Mu Number")
        muLabel.grid(column=0, row=5)
        self.muVar = StringVar()
        self.muVar.set(10)
        muEntry = ttk.Entry(self.root, textvariable=self.muVar)
        muEntry.grid(column=1, row=5)

        sigmaLabel = ttk.Label(self.root, text="Sigma Number")
        sigmaLabel.grid(column=0, row=6)
        self.sigmaVar = StringVar()
        self.sigmaVar.set(10)
        sigmaEntry = ttk.Entry(self.root, textvariable=self.sigmaVar)
        sigmaEntry.grid(column=1, row=6)

        self.root.mainloop()

    def __init__(self, master, app):
        print("init advert")
        self.root = Toplevel(master)
        self.app = app

    def __init__(self, app):
        self.app = app
        self.root = Tk()

    def save(self):
        self.root.destroy()
        self.app.AdMenuReturn = advertConfiguration(self.seedVar.get(), self.emailVar.get(), self.adVar.get(),
                                                    self.muVar.get(), self.sigmaVar.get())


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
        seedLabel.grid(column=0, row=2)
        self.seedVar = StringVar()
        self.seedVar.set(10)
        seedEntry = ttk.Entry(self.root, textvariable=self.seedVar)
        seedEntry.grid(column=1, row=2)

        modelVar = StringVar()
        select1 = ttk.Radiobutton(self.root, text="Influence model 1", variable=modelVar, value="1")
        select1.grid(column=0, row=3)
        select2 = ttk.Radiobutton(self.root, text="Influence model 2", variable=modelVar, value="2")
        select2.grid(column=0, row=4)
        self.modelVar = modelVar

        self.root.mainloop()

    def __init__(self, master, app):
        self.root = Toplevel(master)
        self.app = app

    def save(self):
        self.root.destroy()
        self.app.InfluenceMenuReturn = influenceConfiguration(self.seedVar.get(), self.modelVar.get())


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
        seedLabel.grid(column=0, row=2)
        self.seedVar = StringVar()
        self.seedVar.set(10)
        seedEntry = ttk.Entry(self.root, textvariable=self.seedVar)
        seedEntry.grid(column=1, row=2)

        self.root.mainloop()

    def __init__(self, master, app):
        self.root = Toplevel(master)
        self.app = app

    def save(self):
        self.root.destroy()
        self.app.RecommendationMenuReturn = recommendationConfiguration(self.seedVar.get())


class recommendationConfiguration(object):
    def __init__(self, seed):
        self.seed = seed

class InputMenu(object):
    def menu(self):
        self.root.title("Input Configuration")

        def save():
            if not hasattr(self, "input"):
                self.input = ""
            self.save()

        def askopenfile():
            self.input = filedialog.askopenfile(mode='r')

        submit = ttk.Button(self.root, text="save", command=save)
        submit.grid(column=0, row=1)

        loadVar = StringVar()
        select1 = ttk.Radiobutton(self.root, text="Load input", variable=loadVar, value="1")
        select1.grid(column=0, row=3)
        select2 = ttk.Radiobutton(self.root, text="Generate input", variable=loadVar, value="0")
        select2.grid(column=0, row=4)
        self.loadVar = loadVar

        filePick = ttk.Button(self.root, text="Choose input file", command=askopenfile)
        filePick.grid(column=0, row=5)

        cullLabel = ttk.Label(self.root, text="How many vertices to import")
        cullLabel.grid(column=0, row=6)
        self.cullVariable = StringVar()
        cullInput = ttk.Entry(self.root, textvariable=self.cullVariable)
        cullInput.grid(column=1, row=6)

        randomPeopleLabel = ttk.Label(self.root, text="How many people to randomly generate")
        randomPeopleLabel.grid(column=0, row=7)
        self.randomPeopleVariable = StringVar()
        randomPeopleInput = ttk.Entry(self.root, textvariable=self.randomPeopleVariable)
        randomPeopleInput.grid(column=1, row=7)

        randomConnectionsLabel = ttk.Label(self.root, text="How many connections to randomly generate")
        randomConnectionsLabel.grid(column=0, row=8)
        self.randomConnectionsVariable = StringVar()
        randomConnectionsInput = ttk.Entry(self.root, textvariable=self.randomConnectionsVariable)
        randomConnectionsInput.grid(column=1, row=8)

        self.root.mainloop()

    def __init__(self, master, app):
        self.root = Toplevel(master)
        self.app = app

    def save(self):
        self.root.destroy()
        self.app.InputMenuReturn = inputConfiguration(self.loadVar.get(), self.input.get(), self.cullVariable.get(), self.randomPeopleVariable.get(), self.randomConnectionsVariable.get())


class inputConfiguration(object):
    def __init__(self, load, file="", cull="", people="", connections=""):
        self.load = load
        self.file = file
        self.cull = cull
        self.people = people
        self.connections = connections

class SocialMenu(object):
    def menu(self):
        self.root.title("Social Configuration")

        def save():
            self.save()

        submit = ttk.Button(self.root, text="save", command=save)
        submit.grid(column=0, row=1)

        self.root.mainloop()

    def __init__(self, master, app):
        self.root = Toplevel(master)
        self.app = app

    def save(self):
        self.root.destroy()
        self.app.InputMenuReturn = socialConfiguration()


class socialConfiguration(object):
    def __init__(self):
        pass