

class CommandType():
    def __init__(self, command, type):
        self._command = command
        self._type = type

    def set_command(self, command):
        self._command = command

    def get_command(self):
        return self._command
    
    def set_type(self, type):
        self._type = type
    
    def get_type(self):
        return self._type

