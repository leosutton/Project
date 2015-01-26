__author__ = 'Leo'
from tkinter import *
from tkinter import ttk


class GraphMenu(object):
    def __init__(self, master, app):
        self.root = Toplevel(master)
        self.app = app

    def menu(self):
        self.root.title("Graph Configuration")

        def save():
            self.save()


        submit = ttk.Button(self.root, text="save", command=save)
        submit.grid(column=0, row=0)

        colourLabel = ttk.Label(self.root, text="Node colour")
        colourLabel.grid(column=0, row=1)
        self.colourVar = StringVar()
        colourSelect = ttk.Combobox(self.root, textvariable=self.colourVar)
        colourSelect['values']=("Age", "Views", "Friends", "None")
        colourSelect.current(3)
        colourSelect.grid(row=2)

        circleLabel = ttk.Label(self.root, text="Circle value")
        circleLabel.grid(row=3)
        self.circleVar = StringVar()
        circleSelect = ttk.Combobox(self.root, textvariable=self.circleVar)
        circleSelect['values']=("Age", "Views", "Friends", "None")
        circleSelect.current(3)
        colourSelect.grid(row=4)

        weightLabel = ttk.Label(self.root, text="Closeness weight on edges")
        weightLabel.grid(row=5)
        self.weightVar = StringVar()
        weightEntry = ttk.Entry(self.root, textvariable=self.weightVar)
        weightEntry.insert(0, "0")
        weightEntry.grid(row=6)

        self.root.mainloop()

    def save(self):
        self.root.destroy()
        self.app.GraphMenuReturn = graphConfiguration(self.colourVar.get(), self.circleVar.get(), self.weightVar.get())


class graphConfiguration(object):
    def __init__(self, colour, circle, weight):
        def is_number(number):
            try:
                float(number)
                return True
            except:
                return False

        self.colour = colour
        self.circle = circle
        if is_number(weight):
            self.weight = weight
        else:
            self.weight = 0