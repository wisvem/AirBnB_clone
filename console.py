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


class HBNBCommand(cmd.Cmd):
    """
    Command processor class
    """
    prompt = '(hbnb) '
    listclass = ['BaseModel', 'User']
    # Inicializé all_obj acá arriba para poder cambiar el orden en que se
    # evaluan las condiciones del update
    # También cambié donde teniasmos all_obj por self.all_obj
    # E códi pasa pep8, y ahora mismo son las 2.30 y abajo vas a encontrar una
    # historia que la escribi a las 2
    all_objs = storage.all()
    # parser = argparse.ArgumentParser()

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
        elif arg not in self.listclass:
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
        elif mylist[0] not in self.listclass:
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
        elif mylist[0] not in self.listclass:
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
        # mylist = str.split(arg)
        mylist = shlex.split(arg)
        # print(m2)
        # exit()
        """
        Si pude lograrlo, son las 2AM, por si no me ves levantado tan temprano
        Cambie todos los str.split por shlex.split para que no lo hiciera por
        los espacios sino por los argumentos
        y pudiera tener en cuenta las comillas dobles-----

        Dani est de aqui está comentado porque los argumentos no están entrando
        correctamente.
        el metodo ya me actualiza el objeto pero no acepta ls comillas dobles.
        Cuando se usan comillas dobles para el valor del nuevo atributo se
        actualiza el objeto con varios backslash
        el metodo split separa los argumentos por espacio, si se envia un
        "Daniel Cortes" el split devulce "Daniel, Cortes"

        """
        myobj = None
        found_id = False
        if bool(arg) is False:
            print("** class name missing **")
            return
        elif mylist[0] not in self.listclass:
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
                #    setattr(myobj, mylist[2], mylist[3])
                #    myobj.save()
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
            setattr(myobj, mylist[2], mylist[3])
            myobj.save()
            found_id = True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
