#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Class Storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        # print("\n\n\n\n\n")
        # print("############### Objeto solo #########################")
        # print(obj)
        # print("################ Objeto Dict ########################")
        # print(obj.to_dict())
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
        # print("---------------->dict", obj.to_dict())

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
#       print("=====OBJECTS=====\n",self.__objects,"\n=========")
        filename = self.__file_path
        dct = {}
        for key in self.__objects.keys():
            dct[key] = self.__objects[key].to_dict()
        with open(filename, "w") as f:
            f.write(json.dumps(dct))

    def reload(self):
        """ Deserializes the JSON file to __objects (only if the JSON file
        """
        filename = self.__file_path
        try:
            with open(filename, "r") as f:
                j_string = json.load(f)
                for key, value in j_string.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except Exception:
            pass
