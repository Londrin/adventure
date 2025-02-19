import tkinter as tk
import tkinter.ttk as ttk
from constants.constants import RM

from src.room import Room
from src.actor import Actor
from objectlist import ObjectList
from src.object import Object

class Game(ttk.Frame):    
    from parser import parse_command, run_command
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
        self.input_field.bind("<Return>", self.run_command)
        self.input_field.grid(row=1, column=0, sticky='we', padx=2, pady=2)

        self.input_field.focus()

        self.text_area.config(state="disabled")
        self._player:Actor

        self.initialize_game()
        self.start_game()        

    def initialize_game(self):
        docks_esrel = Room("[Esrel Docks]", "You notice the hustle and bustle of the Esrel docks. Glancing around you can see numerous boats moored, rocking to the waves of Lake Esrel. Fresh fish and nature raise to meet you. Along the waters edge you can see a stretching sand lake front and in the distance standing among trees you see stone walls.",
                           {"north": RM.path_esrel, "east": RM.lake_esrel}, ObjectList())
        lake_esrel = Room("[Lake Esrel]", "Water laps at your feet as you peer out across Lake Esrel. The sound of boats echo out aross the busy water with sights of fishing boats on the horizon. The occasional visitor comes and goes heading to and from Esrel and the docks.",
                          {"west": RM.docks_esrel, "northwest": RM.path_esrel}, ObjectList())
        path_esrel = Room("[Path to Esrel]", "A faint cobblestone path navigates from north and south, speckled with grass and moss and forest creeping to the edges of the pathway. The echos of a port are distant with village life intertwined to the North.",
                          {"south": RM.docks_esrel, "southeast": RM.lake_esrel}, ObjectList())
        
        docks_esrel.add_object(Object("Carrot", "Delicious and crunchy"))
                
        self.world = {
            RM.docks_esrel: docks_esrel,
            RM.path_esrel: path_esrel,
            RM.lake_esrel: lake_esrel,
        }

        self._player = Actor("You", "The Player", docks_esrel, ObjectList())        

    def start_game(self):
        self.update_display(self.look())
    
    def update_display(self, message):
        self.text_area.config(state="normal")
        self.text_area.insert(tk.END, message)
        self.text_area.see(tk.END)
        self.text_area.config(state="disabled")      

    def move_player(self, direction):
        if direction in self._player.room.get_lst_exits():
            self._player.room = self.world[self._player.room.get_lst_exits()[direction]]
            return self.look()
        else:
            return f"{direction.capitalize()} is not a valid exit.\n\n"

    def look(self):
        return self._player.room.describe()
