class Field:
    def __init__ (self, p: str, q: str):
        self.p = p
        self.q = q

    def str(self) -> str:
        return self.p + ":" + self.q

class Friend_request:
    def __init__(self, person: int = None, ):
        pass

class Person:
    def __init__ (self, ID: int = None, name: str = None, field_1: str = None, field_2: str = None, field_3: str = None, field_4: str = None, field_5: str = None, field_6: str = None, field_7: str = None, field_8: str = None, , field_9: str = None, field_10: str = None, friendlist = []) :
        self.ID = ID
        self.name = name
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3
        self.field_4 = field_4
        self.field_5 = field_5
        self.field_6 = field_6
        self.field_7 = field_7
        self.field_8 = field_8
        self.field_9 = field_9
        self.field_10 = field_10
        self.friendlist = friendlist

    def str(self):
        
        return self.ID + ", " + self.name + ", " + self.field_1 + ", " + self.field_2 + ", " + self.field_3 + ", " + self.field_4 + ", " + self.field_5 + ", " + self.field_6 + ", " + self.field_7 + ", " + self.field_8 + ", " + self.field_9 + ", " + self.field_10 + ", " + "" + self.friendlist.stripe()


