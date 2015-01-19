__author__ = 'Leo'
from tkinter import *
from tkinter import ttk


class EnvMenu(object):
    def menu(self):
        self.root.title("Environment Configuration")
        self.colour = "red"
        self.finished = 0

        def save():
            self.save()

        colour = ttk.Label(self.root, text="Node colour")
        submit = ttk.Button(self.root, text="save", command=save)
        colours = ['red', 'green', 'blue']
        for option in colours:
            list1 = ttk.Radiobutton(self.root, text=option, variable=self.colour, value=option)
            list1.grid(column=0, row=4 + colours.index(option), sticky=(N), pady=5)
        colour.grid(column=0, row=1)
        submit.grid(column=0, row=2)

        self.root.mainloop()

    def __init__(self, master, app):
        self.root = Toplevel(master)
        self.app = app

    def save(self):
        self.root.destroy()
        self.app.EnvMenuReturn = envConfiguration()


class envConfiguration(object):
    def __init__(self):
        self.test = 1