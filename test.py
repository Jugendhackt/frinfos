class Field:
    def __init__ (self, eins: str, zwei: str):
        self.eins = eins
        self.zwei = zwei

class Person:
    def __init__ (self, ID: int = None, field_1: Field = None):
        self.ID = ID
        self.field_1 = field_1


