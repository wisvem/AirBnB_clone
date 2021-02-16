#!/usr/bin/python3
"""Console Command processor module to control Airbnb Console
"""
import cmd
import json
from models.base_model import BaseModel
from models import storage
import shlex
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from collections import Counter


class HBNBCommand(cmd.Cmd):
    """Console Command processor class to control Airbnb Console
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
        """EOF method to exit cmd program
        """
        print()
        return True

    def do_quit(self, arg):
        """Quit method to exit form cmd program (Usage: quit)
        """
        return True

    def emptyline(self):
        """Method to should not execute anything
        """
        pass

    def do_create(self, arg):
        """Method to create a instance BaseModel and save it in JSON file
        [Usage: create <class name>]
        """
        if bool(arg) is False:
            print("** class name missing **")
        elif arg not in self.clis:
            print("** class doesn't exist **")
        else:
            my_model = eval(arg)()
            my_model.save()
            print("{}".format(my_model.id))

    def do_show(self, arg):
        """Prints string representation of an instance by class name and id
        [Usage: show <class name> <id>]
        or
        [Usage: <class name>.show(<id>)]
        """
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
        """Deletes an instance based on the class name and id
        [Usage: destroy <class name> <id>]
        or
        [Usage: <class name>.destroy(<id>)]
        """
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
        """Prints all string repr of all instances based or not on class name
        [Usage: all <class name>]
        or
        [Usage: all]
        or
        [Usage: <class name>.all()]
        """
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
        """Updates an obj based on the class name and id by adding or updating
        [Usage: update <class name> <id> <attribute name> "<attribute value>]
        or
        [Usage: <class name>.update(<id>, <attribute name>, <attribute value>)]
        """
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
                    myobj = value
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
            #            try:
            if mylist[2] in self.ilist:
                mylist[3] = int(mylist[3])
            elif mylist[2] in self.flist:
                mylist[3] = float(mylist[3])
            setattr(myobj, mylist[2], mylist[3])
            myobj.save()
#            except ValueError as e:
#                print("Attribute {} must be a number(run <help update>)".
#                      format(mylist[2]))
#                pass
#            found_id = True

    def do_count(self, arg):
        """Count objects created by class
        [Usage: <class name>.count()]
        """
        counter = 0
        if bool(arg) is True:
            for key, value in self.all_objs.items():
                key_list = key.split('.')
                cls_name = key_list[0]
            if cls_name == arg:
                counter = counter + 1
            print(counter)

    def precmd(self, line):
        """Method to run same commands as class.method
        """
        # Make a copy of line
        cp = line[:]
        cp2 = line.split('.', 1)
        if len(cp2) < 2:
            return cp
        else:
            count1, count2 = cp.count(')'), cp.count('(')
            endp_p = len(cp)-1

            # Ask if there are more than one parenthesis ocurrence
            if count1 != 1 or count2 != 1 or ')' != cp[endp_p]:
                return cp
            # Check if there no alpha character before (
            idx = cp.index('(')
            if cp[idx-1].isalpha() is False:
                return cp

            # Save "class" name as str
            mycls = cp2[0]

            cp2[1] = cp2[1].replace('(', ', ')

            cp2[1] = cp2[1].replace(')', '')

            # Save "command" as str
            mycmd = cp2[1].split(', ', 1)[0]
            count1, count2 = cp2[1].count('}'), cp2[1].count('{')
            endp_p = len(cp2[1])-1
            if mycmd == "update":
                myargs = cp2[1].split(', ', 1)[1]
                if count1 == 1 and count2 == 1 and '}' == cp2[1][endp_p]:

                    myargs = myargs.split(', ', 1)
                    # Save ID as str
                    myid = myargs[0]
                    mydict = eval(myargs[1])
                    for key, value in mydict.items():
                        ucmd = mycls+' '+myid+' '+key+' '+'\"'+str(value)+'\"'
                        self.do_update(ucmd)
                    return " "

            mycmd += ' '+mycls+' '+cp2[1].split(', ', 1)[1]
            mycmd = mycmd.replace(',', '')

            return mycmd


if __name__ == '__main__':
    #    import sys
    #    if len(sys.argv) > 1:
    # Uses non interactive
    #        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    #    else:
    # Uses interactive mode
    HBNBCommand(stdin=input).cmdloop()
