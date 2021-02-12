#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
arg =["name", "Juancho"]
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print("==================\n",type(my_model))
setattr(my_model, arg[0], arg[1])
my_model.save()
print(my_model)
