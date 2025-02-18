from object import Object

class ObjectList(list):
    def __init__(self, *args):
        super().__init__(*args)

    def describe(self):
        s = ""
        if len(self) == 0:
            s = ""
        else:
            for object in self:
                s += f"{object.get_name()}, "
        s = s.strip().rstrip(",")
        return s
    
    def get_object(self, name):
        object = None
        object_name = ""
        for obj in self:
            object_name = obj.get_name().lower()
            if name.lower() == object_name:
                object = obj
                break

        return object
        
