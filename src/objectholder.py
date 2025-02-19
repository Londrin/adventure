from src.object import Object
from src.objectlist import ObjectList

class ObjectHolder(Object):
    def __init__(self, name, description, _cantake=True, object_list:ObjectList=[]):
        super().__init__(name, description, _cantake)
        self._object_list:ObjectList = object_list

    def get_objects(self):
        return self._object_list
    
    def set_objects(self, object_list):
        self._object_list = object_list

    def add_object(self, object):
        self._object_list.append(object)
    
    def add_objects(self, objects):
        self._object_list.extend(objects)
    
    def describe(self):
        return f"Name: {self.name}, Description {self.description} which contains: {self._object_list.describeThings()}"