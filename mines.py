from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Mines")
mainframe = ttk.Frame(root)
mainframe.grid(column = 0, row = 0, sticky = "N S W E")
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

for i in range(9):
    for j in range(9):
        ttk.Button(mainframe, width = 2).grid(column = i, row = j)

root.mainloop()