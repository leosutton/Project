__author__ = 'Leo'
from tkinter import *
from tkinter import ttk


class GraphMenu(object):
    def __init__(self, master):
        self.root = Toplevel(master)

    @property
    def menu(self):
        self.root.title("Graph Configuration")

        self.colour = StringVar()

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

        sizeHeading = ttk.Label(self.root, text="Node size")
        sizeHeading.grid(column=0, row=7)

        sizeVar = StringVar()
        size = ttk.Combobox(self.root, textvariable=sizeVar)
        size['values']=('age', 'number of connected nodes')
        size.grid(column=0, row=8)

        self.root.mainloop()

        return [self.colour, sizeVar]

    def destroy(self):
        self.root.destroy()

    def save(self):
        self.root.destroy()