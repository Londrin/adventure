import tkinter as tk
import tkinter.ttk as ttk
from game import Game
import time


root = tk.Tk()
root.title("Project: Lost")
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
root.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, 0, 0))
root.update_idletasks()
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
MIDDLE_SCREEN = '%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, 0, 0)
root.geometry(MIDDLE_SCREEN)
game = Game(root)
game.config(height=600, width=800)
game.pack()
root.mainloop()