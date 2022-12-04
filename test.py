from flask import Flask
from flask import request
import abc_1
from abc_1 import Field, Account
import random



app = Flask(__name__)

@app.route("/create_user", methods = ['POST'])
def create_user():
    if request.args.get('ID','') != "":         
        pass
    else:
        name = request.args.get('name', '')
        field_1 = Field(
            request.args.get('key1', ''),
            request.args.get('value1', ''),
        )
        field_2 = Field(
            request.args.get('key2', ''),
            request.args.get('value2', ''),
        )
        field_3 = Field(
            request.args.get('key3', ''),
            request.args.get('value3', ''),
        )
        field_4 = Field(
            request.args.get('key4', ''),
            request.args.get('value4', ''),
        )
        field_5 = Field(
            request.args.get('key5', ''),
            request.args.get('value5', ''),
        )
        field_6 = Field(
            request.args.get('key6', ''),
            request.args.get('value6', ''),
        )
        field_7 = Field(
            request.args.get('key7', ''),
            request.args.get('value7', ''),
        )
        field_8 = Field(
            request.args.get('key8', ''),
            request.args.get('value8', ''),
        )
        field_9 = Field(
            request.args.get('key9', ''),
            request.args.get('value9', ''),
        )
        field_10 = Field(
            request.args.get('key10', ''),
            request.args.get('value10', ''),
        )
        with open("suii.csv", "r", encoding = "utf8") as f:
            random_ID = get_true_random(f)
            f.close()
            new_user = Account(
                ID = random_ID,
                name = name,
                field_1 = field_1,
                field_2 = field_2,
                field_3 = field_3,
                field_4 = field_4,
                field_5 = field_5,
                field_6 = field_6,
                field_7 = field_7,
                field_8 = field_8,
                field_9 = field_9,
                field_10 = field_10,
                friendlist = []
                )
            with open("suii.csv", "w", encoding = "utf8") as f:
                    f.write("\n")
                    new_user.text()






def get_true_random(text):
        rand_number = random.randint(0, 99999999)
        for line in text:
            if rand_number != line.split(",")[0]:
                continue
            else:
                return get_true_random(text)          
        return rand_number