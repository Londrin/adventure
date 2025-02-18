from room import Room
from object import Object
from objectholder import ObjectHolder
from objectlist import ObjectList

class Actor(ObjectHolder):
    def __init__(self, name, description, room:Room, inventory:ObjectList):
        super().__init__(name, description, False, inventory)
        self.room = room
    
    