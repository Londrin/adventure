from objectlist import ObjectList
from src.objectholder import ObjectHolder

class Room(ObjectHolder):
    def __init__(self, name, description, exits=None, lst:ObjectList=None):
        super().__init__(name, description, False, lst)
        self.exits = exits
        self.lst = lst

    def get_lst_exits(self):
        return self.exits
    
    def get_exits(self):
        message = ""
        if len(self.exits) == 1:
            for key, value in self.exits.items():
                message += f"Exit: {key}."
            return message
        else:
            message += "Exits: "
            for key, value in self.exits.items():
                message += f"{key.capitalize()}, "
            message = message.strip().rstrip(",")
            return message
    
    def set_exits(self, exits):
        self.exits = exits

    def describe(self):
        if not self.lst.describe() == "":
            return f"{self.get_name()}\n{self.get_description()}\nAlso, you can see: {self.lst.describe()}\n{self.get_exits()}\n\n"
        else:
            return f"{self.get_name()}\n{self.get_description()}\n{self.get_exits()}\n\n"

    