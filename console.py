#!/usr/bin/python3
"""
Command processor module
"""
import cmd
from models.base_model import BaseModel
from models import storage
# import argparse
import shlex
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    Command processor class
    """

    prompt = '(hbnb) '
    # Class name list
    clis = ['BaseModel', 'User', 'Place', 'City', 'Amenity', 'Review', 'State']
    # Int attribute name list
    ilist = ['number_rooms', 'number_bathrooms', 'max_guest', 'price_by_night']
    # Float attribute name list
    flist = ['latitude', 'longitude']
    all_objs = storage.all()

    def do_EOF(self, arg):
        'EOF method to exit cmd program\n'
        print()
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
        elif arg not in self.clis:
            print("** class doesn't exist **")
        else:
            my_model = eval(arg)()
            my_model.save()
            print("{}".format(my_model.id))

    def do_show(self, arg):
        'Prints string representation of an instance by class name and id\n'
        mylist = shlex.split(arg)
        found_id = False
        if bool(arg) is False:
            print("** class name missing **")
        elif mylist[0] not in self.clis:
            print("** class doesn't exist **")
        elif len(mylist) != 2:
            print("** instance id missing **")
        else:
            search = mylist[0]+'.'+mylist[1]
            # all_objs = storage.all()
            for key, value in self.all_objs.items():
                if key == search:
                    print(value)
                    found_id = True
                    break
            if found_id is False:
                print("** no instance found **")

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id\n'
        mylist = shlex.split(arg)
        found_id = False
        if bool(arg) is False:
            print("** class name missing **")
        elif mylist[0] not in self.clis:
            print("** class doesn't exist **")
        elif len(mylist) != 2:
            print("** instance id missing **")
        else:
            search = mylist[0]+'.'+mylist[1]
            # all_objs = storage.all()
            for key, value in self.all_objs.items():
                if key == search:
                    del self.all_objs[key]
                    storage.save()
                    found_id = True
                    break
            if found_id is False:
                print("** no instance found **")

    def do_all(self, arg):
        'Prints all string repr of all instances based or not on class name\n'
        # all_objs = storage.all()
        mylist = []
        found_class = False
        if bool(arg) is False:
            for key, value in self.all_objs.items():
                obj = self.all_objs[key]
                mylist.append(str(obj))
                found_class = True
            if found_class is True:
                print(mylist)
        else:
            for key, value in self.all_objs.items():
                if arg == value.__class__.__name__:
                    obj = self.all_objs[key]
                    mylist.append(str(obj))
                    found_class = True
            if found_class:
                print(mylist)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        'Updates an obj based on the class name and id by adding or updating\n'
        mylist = shlex.split(arg)
        myobj = None
        found_id = False
        if bool(arg) is False:
            print("** class name missing **")
            return
        elif mylist[0] not in self.clis:
            print("** class doesn't exist **")
            return
        elif len(mylist) < 2:
            print("** instance id missing **")
            return
        else:
            search = mylist[0]+'.'+mylist[1]
            for key, value in self.all_objs.items():
                if key == search:
                    myobj = self.all_objs[key]
                    found_id = True
                    break
            if found_id is False:
                print("** no instance found **")
                return
        if len(mylist) < 3:
            print("attribute name missing")
        elif len(mylist) < 4:
            print("** value missing **")
        else:
            if mylist[2] in self.ilist:
                mylist[3] = int(mylist[3])
            elif mylist[2] in self.flist:
                mylist[3] = float(mylist[3])
            setattr(myobj, mylist[2], mylist[3])
            myobj.save()
            found_id = True

    def precmd(self, line):
        # Make a copy of line
        cp = line[:]
        mylist = line.split('.', 1)
        if len(mylist) < 2:
            return cp
        else:
            mycls = mylist[0]
            # update("mode", "123-123-123", "name", "juancho")
            # print("Fase 1 ", mylist[1])

            mylist[1] = mylist[1].replace('(', ', ')
            # update, "model", "123-123-123", "name", "juancho")
            # print("Fase 2 ", mylist[1])

            mylist[1] = mylist[1].replace(')', '')
            # update, "model", "123-123-123", "name", "juancho"

            mycmd = mylist[1].split(', ', 1)[0]
            mycmd += ' '+mycls+' '+mylist[1].split(', ', 1)[1]
            mycmd = mycmd.replace(',', '')
            # print(mycmd)
            # exit()
            return mycmd


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        # Uses non interactive
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        # Uses interactive mode
        HBNBCommand(stdin=input).cmdloop()
