from src.room import Room
from src.object import Object
from src.objectholder import ObjectHolder
from objectlist import ObjectList

class Actor(ObjectHolder):
    def __init__(self, name, description, room:Room, inventory:ObjectList):
        super().__init__(name, description, False, inventory)
        self.room = room
    
    