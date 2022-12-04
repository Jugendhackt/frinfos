import random
from flask import Flask
from flask import request

class Field:
    def __init__ (self, p: str, q: str):
        self.p = p
        self.q = q

    def str(self) -> str:
        return self.p + " : " + self.q
class Account:
    def __init__ (self, ID: int = None, name: str = None, 
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
    friendlist = []):
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

    def text(self):
        with open("suii.csv", "w", encoding = "utf8") as f:
            if self.ID:
                f.write(str(self.ID) + ", ")
            else:
                f.write("%, ")

            if self.name:
                f.write(self.name + ", ")
            else:
                f.write("%, ")

            if self.field_1:
                f.write(self.field_1.str() + ", ")
            else:
                f.write("%, ")

            if self.field_2 != None:
                f.write(self.field_2.str() + ", ")
            else:
                f.write("%, ")

            if self.field_3:
                f.write(self.field_3.str() + ", ")
            else:
                f.write("%, ")

            if self.field_4:
                f.write(self.field_4.str() + ", ")
            else:
                f.write("%, ")

            if self.field_5:
                f.write(self.field_5.str() + ", ")
            else:
                f.write("%, ")

            if self.field_6:
                f.write(self.field_6.str() + ", ")
            else:
                f.write("%, ")

            if self.field_7:
                f.write(self.field_7.str() + ", ")
            else:
                f.write("%, ")

            if self.field_8:
                f.write(self.field_8.str() + ", ")
            else:
                f.write("%, ")

            if self.field_9:
                f.write(self.field_9.str() + ", ")
            else:
                f.write("%, ")

            if self.field_10:
                f.write(self.field_10.str() + ", ")
            else:
                f.write("%, ")
    def modify_user(self):
        the_ID = request.args.get('ID', '')
        with open("suii.csv", "r", encoding = "utf8") as f:
            for line in f:
                if the_ID == line.split(",")[0]:
                    line.split(",")[1] = request.args.get('name', '')
                    line.split(",")[2] = self.field_1 = Field(
                        request.args.get('key1', ''),
                        request.args.get('value1', ''),
                    ) 
                    line.split(",")[3] = self.field_2 = Field(
                        request.args.get('key2', ''),
                        request.args.get('value2', ''),
                    ) 
                    line.split(",")[4] = self.field_3 = Field(
                        request.args.get('key3', ''),
                        request.args.get('value3', ''),
                    ) 
                    line.split(",")[5] = self.field_4 = Field(
                        request.args.get('key4', ''),
                        request.args.get('value4', ''),
                    ) 
                    line.split(",")[6] = self.field_5 = Field(
                        request.args.get('key5', ''),
                        request.args.get('value5', ''),
                    ) 
                    line.split(",")[7] = self.field_6 = Field(
                        request.args.get('key6', ''),
                        request.args.get('value6', ''),
                    ) 
                    line.split(",")[8] = self.field_7 = Field(
                        request.args.get('key7', ''),
                        request.args.get('value7', ''),
                    ) 
                    line.split(",")[9] = self.field_8 = Field(
                        request.args.get('key8', ''),
                        request.args.get('value8', ''),
                    ) 
                    line.split(",")[10] = self.field_9 = Field(
                        request.args.get('key9', ''),
                        request.args.get('value9', ''),
                    ) 
                    line.split(",")[11] = self.field_10 = Field(
                        request.args.get('key9', ''),
                        request.args.get('value9', ''),
                    )
                else:
                    continue
