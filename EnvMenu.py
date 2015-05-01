__author__ = 'Leo'
from tkinter import *
from tkinter import ttk


class EnvMenu(object):
    def menu(self):
        self.root.title("Environment Configuration")

        def save():
            self.save()

        submit = ttk.Button(self.root, text="save", command=save)
        submit.grid(column=0, row=1)

        colourLabel = ttk.Label(self.root, text="Point colour")
        colourLabel.grid(row=2)
        self.colourVar = StringVar()
        colourSelect = ttk.Combobox(self.root, textvariable=self.colourVar)
        colourSelect['values']=('Height', 'None')
        colourSelect.current(0)
        colourSelect.grid(row=3)

        self.facingVar = BooleanVar()
        facingCheck = ttk.Checkbutton(self.root, text="Highlight facing", variable=self.facingVar)
        self.facingVar.set(1)
        facingCheck.grid(row=4)

        self.seenVar = BooleanVar()
        seenCheck = ttk.Checkbutton(self.root, text="Hightlight on seeing other person", variable=self.seenVar)
        self.seenVar.set(1)
        seenCheck.grid(row=5)

        self.root.mainloop()

    def __init__(self, master, app):
        self.root = Toplevel(master)
        self.app = app

    def save(self):
        self.root.destroy()
        self.app.EnvMenuReturn = envConfiguration(self.colourVar.get(), self.facingVar.get(), self.seenVar.get())


class envConfiguration(object):
    def __init__(self, colour, facing, seen):
        self.colour = colour
        self.facing = facing
        self.seen = seen