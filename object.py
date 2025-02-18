from baseobject import BaseObject

class Object(BaseObject):
    def __init__(self, name, description, _cantake=True):
        super().__init__(name, description)
        self._cantake = _cantake

    def can_take(self):
        return self._cantake
    
    def set_cantake(self, cantake):
        self._cantake = cantake