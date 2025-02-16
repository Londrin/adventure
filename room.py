
class Room():
    def __init__(self, name, description, exits=None):
        self.name = name
        self.description = description
        self.exits = exits

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_exits(self):
        return self.exits
    
    def set_exits(self, exits):
        self.exits = exits

    