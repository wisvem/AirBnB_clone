#!/usr/bin/python3
import json


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
        """sets in __objects the obj with key <obj class name>.id
        """
        # print("------------>", obj)
        # print("---------------------------- aqui termina")
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
        # print("---------------->dict", obj.to_dict())


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
                FileStorage.__objects = {json.load(j_string)}
        except Exception:
            pass
