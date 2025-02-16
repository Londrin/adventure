import tkinter as tk
import tkinter.ttk as ttk
from game_world import Game_World

class GUI(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        

        self.grid_propagate(False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.text_area = tk.Text(self, foreground="white", background="black", wrap=tk.WORD)
        self.ys = ttk.Scrollbar(self, orient='vertical', command= self.text_area.yview)
        self.text_area['yscrollcommand'] = self.ys.set

        self.text_area.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
        self.ys.grid(row=0, column=1, sticky='nwes')

        self.input_field = tk.Entry(self)
        self.input_field.bind("<Return>", self.process_input)
        self.input_field.grid(row=1, column=0, sticky='we', padx=2, pady=2)

        self.input_field.focus()

        self.game_world = Game_World()
        
        self.update_display(self.game_world.get_current_location())
    
    def update_display(self, room, message=None):
        if message is not None:
            self.text_area.insert(tk.END, f"{message}\n\n")
            self.text_area.see(tk.END)
            return
        
        exits = room.get_exits().keys()
        if len(exits) == 1:
            self.text_area.insert(tk.END, f"{room.get_name()}\n{room.get_description()}\nExits: {next(iter(exits)).capitalize()}\n\n")
        else:
            rooms = ""
            for key in exits:
                rooms += f" {key.capitalize()},"
            
            rooms = rooms.rstrip(',')            
            self.text_area.insert(tk.END, f"{room.get_name()}\n{room.get_description()}\nExits:{rooms}\n\n")

        self.text_area.see(tk.END)
    
    def process_input(self, event):
        user_input = self.input_field.get().lower()
        self.text_area.insert(tk.END, f"> {user_input}\n\n")
        self.input_field.delete(0, tk.END)
        current = self.game_world.current_location      

        if user_input in current.get_exits():
            self.game_world.set_world_location(current, user_input)
            self.update_display(self.game_world.get_current_location())
        else:
            self.update_display(self.game_world.get_current_location(), "Invalid command.")