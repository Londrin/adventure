import tkinter as tk
import tkinter.ttk as ttk
from GUI import GUI
import time


root = tk.Tk()
root.title("Project: Lost")
game = GUI(root)
game.config(height=600, width=800)
game.pack()
root.mainloop()