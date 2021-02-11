#!/usr/bin/python3
"""
Command processor module
"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
