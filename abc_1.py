class Field:
    def __init__ (self, p: str, q: str):
        self.p = p
        self.q = q

    def str(self) -> str:
        return self.p + " : " + self.q
class Account:
    def __init__ (self, ID: int = None, name: Field = None, 
    field_1: Field = None, 
    field_2: Field = None,
    field_3: Field = None, 
    field_4: Field = None, 
    field_5: Field = None, 
    field_6: Field = None, 
    field_7: Field = None, 
    field_8: Field = None,  
    field_9: Field = None, 
    field_10: Field = None, 
    friendlist = []) :
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
        # Hıer kommt spater etwas reın            
        self.friendlist = friendlist
    def tessi(self) :
        with open("suii.txt", "w") as f:
            f.write(self.ID + ", " 
            + self.name + ", " 
            + str(self.field_1) + ", " 
            + str(self.field_2) + ", " 
            + str(self.field_3) + ", " 
            + str(self.field_4) + ", " 
            + str(self.field_5) + ", " 
            + str(self.field_6) + ", " 
            + str(self.field_7) + ", " 
            + str(self.field_8) + ", " 
            + str(self.field_9) + ", " 
            + str(self.field_10) + ", " 
            + "" + self.friendlist.stripe())

