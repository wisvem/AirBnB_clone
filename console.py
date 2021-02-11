#!/usr/bin/python3
"""
Command processor module
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command processor class
    """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        'EOF method to exit cmd program\n'
        return True

    def do_quit(self, arg):
        'Quit method to exit form cmd program\n'
        return True

    def emptyline(self):
        'Method to should not execute anything'
        pass

    def do_create(self, arg):
        'Method to create a instance BaseModel and save it in JSON file'
        if bool(arg) is False:
            print("** class name missing **")
        elif arg != 'BaseModel':
            print("** class doesn't exist **")
        else:
            my_model = eval(arg)()
            my_model.save()
            print("{}".format(my_model.id))

    def show(self, arg):
        'Prints string representation of an instance by class name and id'
        all_objs = storage.all()
        for key, value in all_objs.iems():
            if value["id"] == arg:
                obj = all_objs[key]
                print(obj)
                break

if __name__ == '__main__':
    HBNBCommand().cmdloop()
