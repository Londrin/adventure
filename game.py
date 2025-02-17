import tkinter as tk
import tkinter.ttk as ttk
from constants import RM, Direction
from room import Room
from actor import Actor

class Game(ttk.Frame):    

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
                           {"north": RM.path_esrel, "east": RM.lake_esrel})
        lake_esrel = Room("[Lake Esrel]", "Water laps at your feet as you peer out across Lake Esrel. The sound of boats echo out aross the busy water with sights of fishing boats on the horizon. The occasional visitor comes and goes heading to and from Esrel and the docks.",
                          {"west": RM.docks_esrel, "northwest": RM.path_esrel})
        path_esrel = Room("[Path to Esrel]", "A faint cobblestone path navigates from north and south, speckled with grass and moss and forest creeping to the edges of the pathway. The echos of a port are distant with village life intertwined to the North.",
                          {"south": RM.docks_esrel, "southeast": RM.lake_esrel})
                
        self.world = {
            RM.docks_esrel: docks_esrel,
            RM.path_esrel: path_esrel,
            RM.lake_esrel: lake_esrel,
        }

        self._player = Actor("You", "The Player", docks_esrel)        

    def start_game(self):
        s = self.update_display()
        self.text_area.insert(tk.END, s)
    
    def update_display(self, message=None):
        self.text_area.config(state="normal")

        if message is not None:
            return f"{message}\n\n"
        
        room = self._player.room
        exits = room.get_exits().keys()
        if len(exits) == 1:
            return f"{room.get_name()}\n{room.get_description()}\nExits: {next(iter(exits)).capitalize()}\n\n"            
        else:
            rooms = ""
            for key in exits:
                rooms += f" {key.capitalize()},"
            
            rooms = rooms.rstrip(',')            
            return f"{room.get_name()}\n{room.get_description()}\nExits:{rooms}\n\n"
    
    def parse_command(self, user_input):
        commands = ["n", "north", "northwest", "northeast", "e", "east", "southeast", "south", "s", "southwest", "west", "w", "look", "nw", "ne", "se", "sw"]

        input = user_input.lower().split()                

        if input[0] not in commands:
            return self.update_display(f"{user_input} is not a valid command.")
        else:
            match (input[0]):
                case "n":
                    if Direction.North.value in self._player.room.get_exits():                        
                        self.move_player(Direction.North.value)
                        return self.update_display()                    
                    return f"{input[0]} is not a valid exit.\n\n"
                case Direction.North.value:
                    if input[0] in self._player.room.get_exits():
                        self.move_player(Direction.North.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case Direction.Northeast.value:
                    if input[0] in self._player.room.get_exits():
                        self.move_player(Direction.Northeast.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case "ne":
                    if Direction.Northeast.value in self._player.room.get_exits():
                        self.move_player(Direction.Northeast.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case Direction.East.value:
                    if input[0] in self._player.room.get_exits():
                        self.move_player(Direction.East.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case "e":
                    if Direction.East.value in self._player.room.get_exits():
                        self.move_player(Direction.East.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case Direction.Southeast.value:
                    if input[0] in self._player.room.get_exits():
                        self.move_player(Direction.Southeast.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case "se":
                    if Direction.Southeast.value in self._player.room.get_exits():
                        self.move_player(Direction.Southeast.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case Direction.South.value:
                    if input[0] in self._player.room.get_exits():
                        self.move_player(Direction.South.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case "s":
                    if Direction.South.value in self._player.room.get_exits():
                        self.move_player(Direction.South.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case Direction.Southwest.value:
                    if input[0] in self._player.room.get_exits():
                        self.move_player(Direction.Southwest.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case "sw":
                    if Direction.Southwest.value in self._player.room.get_exits():
                        self.move_player(Direction.Southwest.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case Direction.West.value:
                    if input[0] in self._player.room.get_exits():
                        self.move_player(Direction.West.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case "w":
                    if Direction.West.value in self._player.room.get_exits():
                        self.move_player(Direction.West.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case Direction.Northwest.value:
                    if input[0] in self._player.room.get_exits():
                        self.move_player(Direction.Northwest.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case "nw":
                    if Direction.Northwest.value in self._player.room.get_exits():
                        self.move_player(Direction.Northwest.value)
                        return self.update_display()
                    return f"{input[0]} is not a valid exit.\n\n"
                case "look":
                    return self.update_display()

    def run_command(self, command=None):        
        self.text_area.config(state="normal")
        self.text_area.insert(tk.END, f"> {self.input_field.get().strip()}\n\n")        
        user_input = self.input_field.get().strip()
        self.input_field.delete(0, tk.END)
        s = self.parse_command(user_input)        
        self.text_area.insert(tk.END, s)
        self.text_area.config(state="disabled")
        self.text_area.see(tk.END)

    def move_player(self, direction):        
        self._player.room = self.world[self._player.room.get_exits()[direction]]
