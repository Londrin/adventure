import tkinter as tk
from constants import Direction

def parse_command(self, user_input):
    commands = ["n", "north", "northwest", "northeast", "e", "east", "southeast", "south", "s", "southwest", "west", "w", "look", "nw", "ne", "se", "sw"]

    input = user_input.lower().split()                

    if input[0] not in commands:
        return self.update_display(f"{user_input} is not a valid command.")
    else:
        match (input[0]):
            case "n" | Direction.North.value:
                return self.move_player(Direction.North.value)
            case "ne" | Direction.Northeast.value:
                return self.move_player(Direction.Northeast.value)
            case "e" | Direction.East.value:
                return self.move_player(Direction.East.value)
            case "se" | Direction.Southeast.value:
                return self.move_player(Direction.Southeast.value)
            case "s" | Direction.South.value:
                return self.move_player(Direction.South.value)
            case "sw" | Direction.Southwest.value:
                return self.move_player(Direction.Southwest.value)
            case "w" | Direction.West.value:
                return self.move_player(Direction.West.value)
            case "nw" | Direction.Northwest.value:
                return self.move_player(Direction.Northwest.value)
            case "look":
                return self.look()

def run_command(self, command=None):        
    self.text_area.config(state="normal")
    self.text_area.insert(tk.END, f"> {self.input_field.get().strip()}\n\n")        
    user_input = self.input_field.get().strip()
    self.input_field.delete(0, tk.END)
    self.update_display(self.parse_command(user_input))  