#!/usr/bin/python3
"""
Command processor module
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command processor class
    """
    prompt = '(hbnb) '
    listclass = ['BaseModel']

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
        'Method to create a instance BaseModel and save it in JSON file\n'
        if bool(arg) is False:
            print("** class name missing **")
        elif arg != 'BaseModel':
            print("** class doesn't exist **")
        else:
            my_model = eval(arg)()
            my_model.save()
            print("{}".format(my_model.id))

    def do_show(self, arg):
        'Prints string representation of an instance by class name and id\n'
        listclass = ['BaseModel']
        mylist = str.split(arg)
        found_id = False
        if bool(arg) is False:
            print("** class name missing **")
        elif mylist[0] not in listclass:
            print("** class doesn't exist **")
        elif len(mylist) != 2:
            print("** instance id missing **")
        else:
            search = mylist[0]+'.'+mylist[1]
            all_objs = storage.all()
            for key, value in all_objs.items():
                if key == search:
                    print(value)
                    found_id = True
                    break
            if found_id is False:
                print("** no instance found **")

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id\n'
        mylist = str.split(arg)
        found_id = False
        if bool(arg) is False:
            print("** class name missing **")
        elif mylist[0] not in self.listclass:
            print("** class doesn't exist **")
        elif len(mylist) != 2:
            print("** instance id missing **")
        else:
            search = mylist[0]+'.'+mylist[1]
            all_objs = storage.all()
            for key, value in all_objs.items():
                if key == search:
                    del all_objs[key]
                    storage.save()
                    found_id = True
                    break
            if found_id is False:
                print("** no instance found **")

    def do_all(self, arg):
        'Prints all string repr of all instances based or not on class name\n'
        all_objs = storage.all()
        mylist = []
        found_class = False
        if bool(arg) is False:
            for key, value in all_objs.items():
                obj = all_objs[key]
                mylist.append(str(obj))
            print(mylist)
        else:
            for key, value in all_objs.items():
                if arg == value.__class__.__name__:
                    obj = all_objs[key]
                    mylist.append(str(obj))
                    found_class = True
            if found_class:
                print(mylist)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        'Updates an obj based on the class name and id by adding or updating\n'
        mylist = str.split(arg)
        found_id = False
        if bool(arg) is False:
            print("** class name missing **")
        elif mylist[0] not in self.listclass:
            print("** class doesn't exist **")
        elif len(mylist) != 2:
            print("** instance id missing **")
        else:
            search = mylist[0]+'.'+mylist[1]
            all_objs = storage.all()
            for key, value in all_objs.items():
                if key == search:
                    del all_objs[key]
                    storage.save()
                    found_id = True
                    break
            if found_id is False:
                print("** no instance found **")     

if __name__ == '__main__':
    HBNBCommand().cmdloop()
