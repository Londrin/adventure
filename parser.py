import tkinter as tk
from constants.constants import Direction, CT
from src.commandtype import CommandType

def init_possible_inputs(self):
    self.possible_inputs.update({"n": CT.VERB})
    self.possible_inputs.update({"north": CT.VERB})
    self.possible_inputs.update({"ne": CT.VERB})
    self.possible_inputs.update({"northeast": CT.VERB})
    self.possible_inputs.update({"e": CT.VERB})
    self.possible_inputs.update({"east": CT.VERB})
    self.possible_inputs.update({"se": CT.VERB})
    self.possible_inputs.update({"southeast": CT.VERB})
    self.possible_inputs.update({"s": CT.VERB})
    self.possible_inputs.update({"south": CT.VERB})
    self.possible_inputs.update({"sw": CT.VERB})
    self.possible_inputs.update({"southwest": CT.VERB})
    self.possible_inputs.update({"w": CT.VERB})
    self.possible_inputs.update({"west": CT.VERB})
    self.possible_inputs.update({"nw": CT.VERB})
    self.possible_inputs.update({"northwest": CT.VERB})
    self.possible_inputs.update({"look": CT.VERB})
    self.possible_inputs.update({"drop": CT.VERB})
    self.possible_inputs.update({"get": CT.VERB})
    self.possible_inputs.update({"take": CT.VERB})
    self.possible_inputs.update({"inv": CT.VERB})
    self.possible_inputs.update({"inventory": CT.VERB})
    self.possible_inputs.update({"the": CT.ARTICLE})
    self.possible_inputs.update({"a": CT.ARTICLE})
    self.possible_inputs.update({"an": CT.ARTICLE})
    self.possible_inputs.update({"carrot": CT.NOUN})

def issue_command(self, command_lst):
    output = ""

    if len(command_lst) == 0:
        output = "Please input a command."
    elif len(command_lst) > 2:
        output = "I do not understand your input, please verify your input with HELP"
    else:
        match (len(command_lst)):
            case 1:
                output = self.issue_verb(command_lst)
            case 2:
                output = self.issue_verb_noun(command_lst)
            case _:
                output = "Unknown Command"
    
    return output

def issue_verb(self, command_lst):
    command:CommandType = command_lst[0]
    output = ""

    if command.get_type() != CT.VERB:
        output = f"{command.get_command()} is not a valid command. See HELP for more information."
    else:
        match (command.get_command()):
            case "n" | Direction.North.value:
                output = self.move_player(Direction.North.value)
            case "ne" | Direction.Northeast.value:
                output = self.move_player(Direction.Northeast.value)
            case "e" | Direction.East.value:
                output = self.move_player(Direction.East.value)
            case "se" | Direction.Southeast.value:
                output = self.move_player(Direction.Southeast.value)
            case "s" | Direction.South.value:
                output = self.move_player(Direction.South.value)
            case "sw" | Direction.Southwest.value:
                output = self.move_player(Direction.Southwest.value)
            case "w" | Direction.West.value:
                output = self.move_player(Direction.West.value)
            case "nw" | Direction.Northwest.value:
                output = self.move_player(Direction.Northwest.value)
            case "look":
                output = self.look()
            case "inv" | "inventory":
                output = self._player.get_objects().describe()
                if output == "":
                    output = "nothing"
                output = f"You are carrying: " + output
            case _:
                output = f"Unknown Command: {command.get_command()}"
    
    return output

def issue_verb_noun(self, command_lst):
    command2:CommandType = command_lst.pop()
    command:CommandType = command_lst.pop()
    output = ""

    if (command.get_type() is not CT.VERB):
        output = f"{command.get_command()} is not a valid command. See HELP for more information."
    elif (command2.get_type() is not CT.NOUN):
        output = f"{command2.get_command()} is not a valid object."
    else:
        match (command.get_command()):
            case "get" | "take":
                output = self.take_object(command2.get_command())
            case "drop":
                output = self.drop_object(command2.get_command())
            case _:
                output = f"Unknown Command: {command.get_command()} {command2.get_command()}"
    
    return output


def parse_command(self, user_input_lst):
    command = []
    output = ""
    invalid = ""    

    for input in user_input_lst:        
        if input in self.possible_inputs:
            command_type = self.possible_inputs[input]            
            
            if command_type is not CT.ARTICLE:
                command.append(CommandType(input, command_type))
            
        else:
            invalid = f"Unknown Command: {input}"
            break
    
    if invalid != "":
        output = invalid
    else:
        output = self.issue_command(command)
    return output    

def execute_command(self, command=None):        
    self.text_area.config(state="normal")
    self.text_area.insert(tk.END, f"> {self.input_field.get().strip()}\n\n")
    self.text_area.config(state="disable")
    user_input = self.input_field.get().strip().split()
    self.input_field.delete(0, tk.END)
    update = self.parse_command(user_input)
    self.update_display(update)