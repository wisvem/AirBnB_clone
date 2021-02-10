#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """ Class Storage """
    __file_path = "file.json"
    __objects = {}

#    def __init__(self):
#        """ Class constructor """
#        pass

    def all(self):
        """ returns the dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id """
        
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj.__dict__()


    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        filename = FileStorage.__file_path
        with open(filename, "w") as f:
            f.write(json.dumps(FileStorage.__objects))
       
    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file """
        filename = FileStorage.__file_path
        try:
            with open(filename, "r") as f:
                j_string = f.read()
                FileStorage.__objects = json.loads(j_string)
        except FileNotFoundError:
            pass

