from room import Room

class Actor():
    def __init__(self, name, description, room:Room):
        self.name = name
        self.description = description
        self.room = room

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_description(self):
        return self.description
    
    def set_description(self, desc):
        self.description = desc
    
    